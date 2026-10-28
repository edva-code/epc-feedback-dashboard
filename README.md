# EPC 2026 video feedback

Results of the "Feedback for video (EPC 2026)" form, where students rated other teams' videos on biases and fallacies.

**[Open the interactive dashboard →](https://edva-code.github.io/epc-feedback-dashboard/)**

The dashboard has the leaderboard, the score distribution, how strict or lenient reviewers were, and all the written feedback, searchable and filterable by team and score. Click a team to see only its reviews.

## Results

Updated every hour from the form responses.

<!-- results:start -->
Latest response 10/28/2026 19:46:21 · 1807 reviews from 103 reviewers · 21 teams · average 8.83 · 35% rated 10 · 13% rated 7 or lower

| # | Team | Reviews | Avg | Adjusted | 6 | 7 | 8 | 9 | 10 | Share of 10s |
|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | (em)pathetic | 86 | 9.76 | 9.76 | 0 | 1 | 4 | 10 | 71 | 83% |
| 2 | Sisyphus | 90 | 9.69 | 9.70 | 0 | 1 | 7 | 11 | 71 | 79% |
| 3 | weshop@vinted | 88 | 9.65 | 9.62 | 1 | 0 | 6 | 15 | 66 | 75% |
| 4 | Banglai | 86 | 9.63 | 9.61 | 0 | 1 | 6 | 17 | 62 | 72% |
| 5 | Communicators | 89 | 9.31 | 9.31 | 0 | 1 | 13 | 32 | 43 | 48% |
| 6 | Zaibas | 89 | 9.17 | 9.18 | 1 | 0 | 10 | 50 | 28 | 31% |
| 7 | Etikos komisija | 82 | 9.16 | 9.18 | 0 | 0 | 14 | 41 | 27 | 33% |
| 8 | VVT  ඞ⃢ඞ⃢ඞIIIඞ⃢ඞ | 86 | 9.13 | 9.14 | 0 | 4 | 16 | 31 | 35 | 41% |
| 9 | komcon. | 84 | 9.06 | 9.08 | 2 | 2 | 14 | 37 | 29 | 35% |
| 10 | Baziliskai | 88 | 9.07 | 9.04 | 1 | 2 | 17 | 38 | 30 | 34% |
| 11 | Team | 86 | 8.98 | 8.99 | 0 | 5 | 18 | 37 | 26 | 30% |
| 12 | BEAM | 89 | 8.96 | 8.95 | 0 | 5 | 19 | 40 | 25 | 28% |
| 13 | Team name | 86 | 8.80 | 8.78 | 0 | 8 | 22 | 35 | 21 | 24% |
| 14 | Team Builders | 89 | 8.69 | 8.68 | 1 | 9 | 26 | 34 | 19 | 21% |
| 15 | Lasagna | 61 | 8.69 | 8.65 | 0 | 1 | 27 | 23 | 10 | 16% |
| 16 | Reflect | 88 | 8.60 | 8.59 | 4 | 10 | 25 | 27 | 22 | 25% |
| 17 | Tortilla de Patatas | 85 | 8.49 | 8.49 | 0 | 13 | 32 | 25 | 15 | 18% |
| 18 | A Moral Hazard | 91 | 8.36 | 8.37 | 3 | 11 | 41 | 22 | 14 | 15% |
| 19 | Komanda 5 | 85 | 8.33 | 8.34 | 2 | 14 | 34 | 24 | 11 | 13% |
| 20 | Vilkai | 87 | 7.28 | 7.28 | 19 | 37 | 22 | 6 | 3 | 3% |
| 21 | Uranium-235 | 92 | 6.63 | 6.66 | 47 | 34 | 9 | 2 | 0 | 0% |

"Adjusted" removes reviewer luck: each score is compared with that reviewer's own average, then shifted back onto the overall average.
<!-- results:end -->

## Privacy

No student IDs are published. Each reviewer is shown as a number (Reviewer 0000001, 0000002, …), and any student ID typed into a comment is replaced by `[student ID]`. The written feedback, scores, team names and submission times are public.

## How it works

A GitHub Action runs every hour, downloads the form responses, and writes `data.csv` (the responses without student IDs, via `publish.py`) and the results table above (via `results.py`). The dashboard is `index.html`, served by GitHub Pages, which reads `data.csv` in your browser.

For local use, `build.py` builds a single offline HTML file from a CSV export of the sheet, and `update.sh` refreshes it. Keep `data/` and the built HTML private, since they still contain student IDs (both are gitignored).
