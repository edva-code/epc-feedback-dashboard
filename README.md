# EPC 2026 video feedback dashboard

A local dashboard for the "Feedback for video (EPC 2026) (Responses)" Google Form, where students rate other teams' videos on biases and fallacies.

The output is one self-contained HTML file with no libraries or network calls. It shows a team leaderboard with a reviewer-adjusted score, the score distribution, how lenient reviewers are, data-quality flags, feedback themes, the lowest-rated teams, and searchable comments.

## Results

Team results from the feedback form, refreshed from the sheet every hour by a GitHub Action. Only team-level numbers are shown here; the full feedback is in the [interactive dashboard](https://edva-code.github.io/epc-feedback-dashboard/).

<!-- results:start -->
Latest response 10/28/2026 19:15:39 · 1717 reviews from 101 reviewers · 21 teams · average 8.83 · 35% rated 10 · 13% rated 7 or lower

| # | Team | Reviews | Avg | Adjusted | 6 | 7 | 8 | 9 | 10 | Share of 10s |
|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | (em)pathetic | 80 | 9.75 | 9.77 | 0 | 1 | 4 | 9 | 66 | 82% |
| 2 | Sisyphus | 88 | 9.69 | 9.71 | 0 | 1 | 7 | 10 | 70 | 80% |
| 3 | weshop@vinted | 85 | 9.65 | 9.62 | 1 | 0 | 6 | 14 | 64 | 75% |
| 4 | Banglai | 81 | 9.63 | 9.62 | 0 | 1 | 6 | 15 | 59 | 73% |
| 5 | Communicators | 87 | 9.30 | 9.29 | 0 | 1 | 13 | 32 | 41 | 47% |
| 6 | Zaibas | 83 | 9.18 | 9.20 | 1 | 0 | 10 | 44 | 28 | 34% |
| 7 | Etikos komisija | 78 | 9.15 | 9.16 | 0 | 0 | 14 | 38 | 26 | 33% |
| 8 | komcon. | 77 | 9.12 | 9.13 | 1 | 2 | 12 | 34 | 28 | 36% |
| 9 | VVT  ඞ⃢ඞ⃢ඞIIIඞ⃢ඞ | 81 | 9.11 | 9.12 | 0 | 4 | 16 | 28 | 33 | 41% |
| 10 | Baziliskai | 87 | 9.08 | 9.06 | 1 | 2 | 16 | 38 | 30 | 34% |
| 11 | BEAM | 87 | 8.97 | 8.97 | 0 | 5 | 18 | 39 | 25 | 29% |
| 12 | Team | 79 | 8.94 | 8.96 | 0 | 5 | 18 | 33 | 23 | 29% |
| 13 | Team name | 84 | 8.80 | 8.78 | 0 | 8 | 21 | 35 | 20 | 24% |
| 14 | Team Builders | 88 | 8.67 | 8.68 | 1 | 9 | 26 | 34 | 18 | 20% |
| 15 | Lasagna | 53 | 8.72 | 8.64 | 0 | 1 | 23 | 19 | 10 | 19% |
| 16 | Reflect | 86 | 8.59 | 8.58 | 4 | 10 | 24 | 27 | 21 | 24% |
| 17 | Tortilla de Patatas | 80 | 8.47 | 8.49 | 0 | 12 | 31 | 24 | 13 | 16% |
| 18 | A Moral Hazard | 88 | 8.39 | 8.40 | 2 | 11 | 40 | 21 | 14 | 16% |
| 19 | Komanda 5 | 77 | 8.30 | 8.30 | 2 | 13 | 32 | 20 | 10 | 13% |
| 20 | Vilkai | 81 | 7.27 | 7.29 | 17 | 36 | 20 | 5 | 3 | 4% |
| 21 | Uranium-235 | 87 | 6.60 | 6.60 | 45 | 34 | 6 | 2 | 0 | 0% |

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
