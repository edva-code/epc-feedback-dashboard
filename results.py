import csv, sys
from collections import Counter, defaultdict
from statistics import mean

# writes team-level results only into the README; no student IDs or feedback text leave the CSV
csv_path, readme_path = sys.argv[1:3]
with open(csv_path, newline='', encoding='utf-8') as f:
    rows = [r + [''] * (7 - len(r)) for r in list(csv.reader(f))[1:] if any(c.strip() for c in r)]
rows = [(r[0], r[1].strip(), r[2].strip(), int(r[5].split(' ')[0])) for r in rows]
assert rows and {s for *_, s in rows} <= {6, 7, 8, 9, 10}, 'not the feedback form export'

# same maths as index.html: adjusted = grand mean + mean of (score - that reviewer's own mean)
grand = mean(s for *_, s in rows)
by_rev, by_team = defaultdict(list), defaultdict(list)
for ts, rid, team, s in rows:
    by_rev[rid].append(s)
rev_mean = {k: mean(v) for k, v in by_rev.items()}
for ts, rid, team, s in rows:
    by_team[team].append((s, s - rev_mean[rid]))
teams = sorted(((t, [s for s, _ in v], grand + mean(d for _, d in v)) for t, v in by_team.items()), key=lambda t: -t[2])
assert sum(len(s) for _, s, _ in teams) == len(rows)

esc = lambda t: t.replace('|', '\\|').replace('<', '&lt;')
pct = lambda n, d: f'{100 * n / d:.0f}%'
all_s = Counter(s for *_, s in rows)
out = [
    f'Latest response {rows[-1][0]} · {len(rows)} reviews from {len(by_rev)} reviewers · {len(teams)} teams · '
    f'average {grand:.2f} · {pct(all_s[10], len(rows))} rated 10 · {pct(all_s[6] + all_s[7], len(rows))} rated 7 or lower',
    '',
    '| # | Team | Reviews | Avg | Adjusted | 6 | 7 | 8 | 9 | 10 | Share of 10s |',
    '|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|',
]
for i, (t, s, adj) in enumerate(teams, 1):
    c = Counter(s)
    out.append(f'| {i} | {esc(t)} | {len(s)} | {mean(s):.2f} | {adj:.2f} | ' + ' | '.join(str(c[k]) for k in (6, 7, 8, 9, 10)) + f' | {pct(c[10], len(s))} |')
out += ['', '"Adjusted" removes reviewer luck: each score is compared with that reviewer\'s own average, then shifted back onto the overall average.']

START, END = '<!-- results:start -->', '<!-- results:end -->'
readme = open(readme_path, encoding='utf-8').read()
assert readme.count(START) == readme.count(END) == 1
head, rest = readme.split(START)
open(readme_path, 'w', encoding='utf-8').write(head + START + '\n' + '\n'.join(out) + '\n' + END + rest.split(END)[1])
print('results for', len(teams), 'teams,', len(rows), 'reviews')
