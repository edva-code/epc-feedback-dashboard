# EPC 2026 video feedback dashboard

A local dashboard for the "Feedback for video (EPC 2026) (Responses)" Google Form, where students rate other teams' videos on biases and fallacies.

The output is one self-contained HTML file with no libraries or network calls. It shows a team leaderboard with a reviewer-adjusted score, the score distribution, how lenient reviewers are, data-quality flags, feedback themes, the lowest-rated teams, and searchable comments.

## Results

Team results from the feedback form, refreshed from the sheet every hour by a GitHub Action. Only team-level numbers are shown here; the full feedback is in the [interactive dashboard](https://edva-code.github.io/epc-feedback-dashboard/).

<!-- results:start -->
Latest response 10/28/2026 18:26:45 · 1503 reviews from 99 reviewers · 21 teams · average 8.82 · 35% rated 10 · 14% rated 7 or lower

| # | Team | Reviews | Avg | Adjusted | 6 | 7 | 8 | 9 | 10 | Share of 10s |
|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | (em)pathetic | 70 | 9.73 | 9.72 | 0 | 1 | 4 | 8 | 57 | 81% |
| 2 | Sisyphus | 77 | 9.66 | 9.66 | 0 | 1 | 7 | 9 | 60 | 78% |
| 3 | Banglai | 69 | 9.65 | 9.63 | 0 | 1 | 4 | 13 | 51 | 74% |
| 4 | weshop@vinted | 75 | 9.65 | 9.61 | 0 | 0 | 6 | 14 | 55 | 73% |
| 5 | Communicators | 84 | 9.29 | 9.27 | 0 | 1 | 13 | 31 | 39 | 46% |
| 6 | Zaibas | 75 | 9.19 | 9.19 | 0 | 0 | 10 | 41 | 24 | 32% |
| 7 | komcon. | 58 | 9.12 | 9.18 | 0 | 2 | 10 | 25 | 21 | 36% |
| 8 | Etikos komisija | 61 | 9.13 | 9.17 | 0 | 0 | 13 | 27 | 21 | 34% |
| 9 | VVT  ඞ⃢ඞ⃢ඞIIIඞ⃢ඞ | 73 | 9.10 | 9.08 | 0 | 4 | 14 | 26 | 29 | 40% |
| 10 | Baziliskai | 82 | 9.09 | 9.07 | 1 | 2 | 15 | 35 | 29 | 35% |
| 11 | Team | 69 | 8.97 | 8.97 | 0 | 4 | 15 | 29 | 21 | 30% |
| 12 | BEAM | 84 | 8.95 | 8.96 | 0 | 5 | 18 | 37 | 24 | 29% |
| 13 | Team name | 79 | 8.80 | 8.80 | 0 | 8 | 19 | 33 | 19 | 24% |
| 14 | Team Builders | 83 | 8.64 | 8.65 | 1 | 9 | 26 | 30 | 17 | 20% |
| 15 | Lasagna | 33 | 8.73 | 8.64 | 0 | 1 | 15 | 9 | 8 | 24% |
| 16 | Reflect | 78 | 8.60 | 8.59 | 4 | 8 | 22 | 25 | 19 | 24% |
| 17 | Tortilla de Patatas | 70 | 8.49 | 8.46 | 0 | 12 | 25 | 20 | 13 | 19% |
| 18 | A Moral Hazard | 80 | 8.39 | 8.40 | 2 | 9 | 37 | 20 | 12 | 15% |
| 19 | Komanda 5 | 58 | 8.14 | 8.19 | 2 | 12 | 25 | 14 | 5 | 9% |
| 20 | Vilkai | 65 | 7.28 | 7.30 | 16 | 26 | 15 | 5 | 3 | 5% |
| 21 | Uranium-235 | 80 | 6.62 | 6.63 | 40 | 32 | 6 | 2 | 0 | 0% |

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
