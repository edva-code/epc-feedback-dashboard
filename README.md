# EPC 2026 video feedback dashboard

A local dashboard for the "Feedback for video (EPC 2026) (Responses)" Google Form, where students rate other teams' videos on biases and fallacies.

The output is one self-contained HTML file with no libraries or network calls. It shows a team leaderboard with a reviewer-adjusted score, the score distribution, how lenient reviewers are, data-quality flags, feedback themes, the lowest-rated teams, and searchable comments.

## Results

Team results from the feedback form, refreshed from the sheet every hour by a GitHub Action. Only team-level numbers are shown here; the full feedback is in the [interactive dashboard](https://edva-code.github.io/epc-feedback-dashboard/).

<!-- results:start -->
Latest response 10/28/2026 19:42:02 · 1794 reviews from 103 reviewers · 21 teams · average 8.82 · 35% rated 10 · 13% rated 7 or lower

| # | Team | Reviews | Avg | Adjusted | 6 | 7 | 8 | 9 | 10 | Share of 10s |
|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | (em)pathetic | 85 | 9.75 | 9.75 | 0 | 1 | 4 | 10 | 70 | 82% |
| 2 | Sisyphus | 89 | 9.69 | 9.70 | 0 | 1 | 7 | 11 | 70 | 79% |
| 3 | weshop@vinted | 87 | 9.64 | 9.62 | 1 | 0 | 6 | 15 | 65 | 75% |
| 4 | Banglai | 85 | 9.62 | 9.61 | 0 | 1 | 6 | 17 | 61 | 72% |
| 5 | Communicators | 89 | 9.31 | 9.31 | 0 | 1 | 13 | 32 | 43 | 48% |
| 6 | Zaibas | 87 | 9.17 | 9.19 | 1 | 0 | 10 | 48 | 28 | 32% |
| 7 | Etikos komisija | 82 | 9.16 | 9.18 | 0 | 0 | 14 | 41 | 27 | 33% |
| 8 | VVT  ඞ⃢ඞ⃢ඞIIIඞ⃢ඞ | 86 | 9.13 | 9.14 | 0 | 4 | 16 | 31 | 35 | 41% |
| 9 | komcon. | 84 | 9.06 | 9.08 | 2 | 2 | 14 | 37 | 29 | 35% |
| 10 | Baziliskai | 88 | 9.07 | 9.04 | 1 | 2 | 17 | 38 | 30 | 34% |
| 11 | Team | 86 | 8.98 | 8.99 | 0 | 5 | 18 | 37 | 26 | 30% |
| 12 | BEAM | 89 | 8.96 | 8.95 | 0 | 5 | 19 | 40 | 25 | 28% |
| 13 | Team name | 86 | 8.80 | 8.78 | 0 | 8 | 22 | 35 | 21 | 24% |
| 14 | Team Builders | 89 | 8.69 | 8.68 | 1 | 9 | 26 | 34 | 19 | 21% |
| 15 | Lasagna | 58 | 8.69 | 8.63 | 0 | 1 | 26 | 21 | 10 | 17% |
| 16 | Reflect | 88 | 8.60 | 8.58 | 4 | 10 | 25 | 27 | 22 | 25% |
| 17 | Tortilla de Patatas | 85 | 8.49 | 8.49 | 0 | 13 | 32 | 25 | 15 | 18% |
| 18 | A Moral Hazard | 90 | 8.36 | 8.36 | 3 | 11 | 41 | 21 | 14 | 16% |
| 19 | Komanda 5 | 83 | 8.34 | 8.36 | 2 | 14 | 32 | 24 | 11 | 13% |
| 20 | Vilkai | 87 | 7.28 | 7.28 | 19 | 37 | 22 | 6 | 3 | 3% |
| 21 | Uranium-235 | 91 | 6.62 | 6.65 | 47 | 34 | 8 | 2 | 0 | 0% |

"Adjusted" removes reviewer luck: each score is compared with that reviewer's own average, then shifted back onto the overall average.
<!-- results:end -->

## Files

- `index.html` is the dashboard source and the public page. With no data it asks for the CSV; `build.py` injects the rows at the `null/*DATA*/` placeholder for the local copy.
- `build.py` builds `epc-feedback-dashboard.html` from the CSV and `index.html`, and sanity-checks the CSV first.
- `update.sh` loads a fresh Drive export, diffs it against the current CSV, rebuilds, checks the page for JS errors in headless Chromium, prints per-team averages and opens the page.
- `publish.py` writes `data.csv`, the public copy of the responses with student IDs swapped for reviewer numbers.
- `results.py` writes the results table into this README.
- `data/responses.csv` is the latest export of the sheet (local only).

## Interactive dashboard

https://edva-code.github.io/epc-feedback-dashboard/ has everything: the leaderboard, charts, reviewer leniency, data-quality flags and all the written feedback, searchable. It reads `data.csv`, which the same hourly Action writes from the sheet with every student ID replaced by a reviewer number (and any ID typed into a comment replaced by `[student ID]`).

To skip the hourly delay, share it as `https://edva-code.github.io/epc-feedback-dashboard/#<sheet id>/<gid>`, taking both from the sheet's own URL (`/d/<sheet id>/edit...#gid=<gid>`). The page then loads the latest responses straight from Google in the visitor's browser on every visit. The part after `#` is never sent to GitHub, so the repo and the bare page hold no data and no link to the sheet; anyone with the full link can see the sheet, the same as with the sheet link itself.

If `data.csv` can't be loaded, the page asks for the CSV instead (File → Download → Comma-separated values in the sheet), which is read in the browser and never uploaded.

## Update from the live sheet

Ask Claude Code to "update" the dashboard. It downloads the sheet as CSV through the Google Drive connector, then runs:

```bash
./update.sh <path to the download_file_content JSON>
```

To do it by hand, export the sheet as CSV to `data/responses.csv` and rebuild:

```bash
python3 -I build.py data/responses.csv index.html epc-feedback-dashboard.html
```

## Privacy

`data.csv` is public: timestamps, teams, scores and the written feedback, with no student IDs. `data/`, the built HTML (it embeds the data) and `shot.png` still contain the real student IDs. They are gitignored, so don't share them.
