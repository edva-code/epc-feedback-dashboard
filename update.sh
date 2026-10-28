#!/bin/bash
# usage: update.sh <drive download_file_content JSON> — decode, diff vs current CSV, rebuild, summarise, open
set -euo pipefail
S=$(dirname "$(readlink -f "$0")"); D=$S/data2; mkdir -p $D
jq -r .content "$1" | base64 -d > $D/responses.csv
python3 -I - $S/data/responses.csv $D/responses.csv <<'EOF'
import csv,sys
a,b=[list(csv.reader(open(p,newline='',encoding='utf-8'))) for p in sys.argv[1:]]
sa,sb=set(map(tuple,a[1:])),set(map(tuple,b[1:]))
new=[r for r in b[1:] if tuple(r) not in sa]
print('old',len(a)-1,'new',len(b)-1,'header same',a[0]==b[0],'added',len(new),'removed/changed',len(sa-sb))
if new: print('added range',new[0][0],'->',new[-1][0])
EOF
mv $D/responses.csv $S/data/responses.csv && rmdir $D
python3 -I $S/build.py $S/data/responses.csv $S/index.html $S/epc-feedback-dashboard.html
chromium --headless=new --disable-gpu --window-size=1280,1000 --screenshot=$S/shot.png "file://$S/epc-feedback-dashboard.html" 2>&1 | grep -E "CONSOLE" || true
python3 -I - $S/data/responses.csv <<'EOF'
import csv,sys,statistics as st
from collections import defaultdict
rows=list(csv.reader(open(sys.argv[1],newline='',encoding='utf-8')))[1:]
s=[int(r[5].split()[0]) for r in rows]; print('mean %.2f  10s %.0f%%  <=7 %.0f%%  reviewers %d'%(st.mean(s),100*s.count(10)/len(s),100*sum(x<=7 for x in s)/len(s),len({r[1].strip() for r in rows})))
t=defaultdict(list)
for r in rows: t[r[2].strip()].append(int(r[5].split()[0]))
for k,v in sorted(t.items(),key=lambda kv:-st.mean(kv[1])): print(f'{st.mean(v):.2f} {len(v):3d} {k}')
EOF
xdg-open $S/epc-feedback-dashboard.html >/dev/null 2>&1 &
