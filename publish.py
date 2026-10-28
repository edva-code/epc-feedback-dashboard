import csv, re, sys

# public copy of the responses for the GitHub Pages dashboard: student IDs become reviewer numbers, everything else stays
src, dst = sys.argv[1:3]
with open(src, newline='', encoding='utf-8') as f:
    head, *rows = list(csv.reader(f))
assert head[1] == 'Your student ID' and len(head) == 7, f'unexpected columns: {head}'
rows = [r + [''] * (7 - len(r)) for r in rows if any(c.strip() for c in r)]

# numbered by first appearance, so a reviewer keeps their number as the sheet grows; 7-digit IDs stay 7 digits
# so the page's "isn't 7 digits" typo check still works without showing the ID
ids = {}
for r in rows:
    k = r[1].strip()
    ids.setdefault(k, f'{len(ids) + 1:07d}' if re.fullmatch(r'\d{7}', k) else f'x{len(ids) + 1}')

# someone may have typed their own or a classmate's ID into a comment
real = sorted((k for k in ids if len(k) >= 5), key=len, reverse=True)
scrub = (lambda c: re.sub('|'.join(map(re.escape, real)), '[student ID]', c)) if real else (lambda c: c)
out = [[r[0], ids[r[1].strip()], *map(scrub, r[2:7])] for r in rows]

assert not set(ids.values()) & set(ids), 'a reviewer number equals a real ID'
assert not any(k in c for r in out for c in [r[0], *r[2:]] for k in real), 'a student ID survived'
with open(dst, 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows([[head[0], 'Reviewer', *head[2:]], *out])
print('published', len(out), 'rows from', len(ids), 'reviewers')
