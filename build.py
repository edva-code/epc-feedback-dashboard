import csv, json, sys
from collections import Counter

csv_path, tpl_path, out_path = sys.argv[1:4]
with open(csv_path, newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))[1:]
rows = [r + [''] * (7 - len(r)) for r in rows if any(c.strip() for c in r)]

# self-check: the form only grows (1019 rows at first pull) and every score is one of the 5 options
scores = Counter(int(r[5].split(' ')[0]) for r in rows)
assert len(rows) >= 1019, len(rows)
assert set(scores) <= {6, 7, 8, 9, 10} and sum(scores.values()) == len(rows), scores
print('scores', dict(sorted(scores.items())), 'teams', len({r[2].strip() for r in rows}))

# escape "<" so a comment containing "</script>" can't break out of the script tag
data = json.dumps(rows, ensure_ascii=False).replace('<', '\\u003c')
tpl = open(tpl_path, encoding='utf-8').read()
assert tpl.count('/*DATA*/') == 1
open(out_path, 'w', encoding='utf-8').write(tpl.replace('/*DATA*/', data))
print('wrote', out_path, len(rows), 'rows')
