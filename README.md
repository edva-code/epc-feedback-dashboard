# EPC 2026 video feedback

Results of the "Feedback for video (EPC 2026)" form, where students rated other teams' videos on biases and fallacies.

**[Open the interactive dashboard →](https://edva-code.github.io/epc-feedback-dashboard/)**

The dashboard has the leaderboard, the score distribution, how strict or lenient reviewers were, and all the written feedback, searchable and filterable by team and score. Click a team to see only its reviews.

## Results

Updated every hour from the form responses.

<!-- results:start -->
Latest response 10/28/2026 20:03:34 · 1844 reviews from 103 reviewers · 21 teams · average 8.83 · 35% rated 10 · 13% rated 7 or lower

| # | Team | Reviews | Avg | Adjusted | 6 | 7 | 8 | 9 | 10 | Share of 10s |
|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | (em)pathetic | 87 | 9.76 | 9.77 | 0 | 1 | 4 | 10 | 72 | 83% |
| 2 | Sisyphus | 92 | 9.70 | 9.71 | 0 | 1 | 7 | 11 | 73 | 79% |
| 3 | weshop@vinted | 90 | 9.66 | 9.62 | 1 | 0 | 6 | 15 | 68 | 76% |
| 4 | Banglai | 87 | 9.63 | 9.61 | 0 | 1 | 6 | 17 | 63 | 72% |
| 5 | Communicators | 89 | 9.31 | 9.31 | 0 | 1 | 13 | 32 | 43 | 48% |
| 6 | Zaibas | 92 | 9.20 | 9.20 | 1 | 0 | 10 | 50 | 31 | 34% |
| 7 | Etikos komisija | 85 | 9.14 | 9.16 | 0 | 0 | 16 | 41 | 28 | 33% |
| 8 | VVT  ඞ⃢ඞ⃢ඞIIIඞ⃢ඞ | 88 | 9.12 | 9.13 | 0 | 4 | 16 | 33 | 35 | 40% |
| 9 | komcon. | 86 | 9.07 | 9.10 | 2 | 2 | 14 | 38 | 30 | 35% |
| 10 | Baziliskai | 88 | 9.07 | 9.04 | 1 | 2 | 17 | 38 | 30 | 34% |
| 11 | Team | 89 | 9.00 | 9.02 | 0 | 5 | 18 | 38 | 28 | 31% |
| 12 | BEAM | 89 | 8.96 | 8.94 | 0 | 5 | 19 | 40 | 25 | 28% |
| 13 | Team name | 86 | 8.80 | 8.78 | 0 | 8 | 22 | 35 | 21 | 24% |
| 14 | Team Builders | 90 | 8.68 | 8.68 | 1 | 9 | 27 | 34 | 19 | 21% |
| 15 | Lasagna | 68 | 8.63 | 8.60 | 0 | 1 | 33 | 24 | 10 | 15% |
| 16 | Reflect | 89 | 8.57 | 8.57 | 5 | 10 | 25 | 27 | 22 | 25% |
| 17 | Tortilla de Patatas | 87 | 8.51 | 8.50 | 0 | 13 | 33 | 25 | 16 | 18% |
| 18 | Komanda 5 | 89 | 8.34 | 8.35 | 2 | 14 | 36 | 26 | 11 | 12% |
| 19 | A Moral Hazard | 94 | 8.33 | 8.33 | 4 | 12 | 41 | 23 | 14 | 15% |
| 20 | Vilkai | 87 | 7.28 | 7.29 | 19 | 37 | 22 | 6 | 3 | 3% |
| 21 | Uranium-235 | 92 | 6.63 | 6.67 | 47 | 34 | 9 | 2 | 0 | 0% |

"Adjusted" removes reviewer luck: each score is compared with that reviewer's own average, then shifted back onto the overall average.
<!-- results:end -->

## Privacy

No student IDs are published. Each reviewer is shown as a number (Reviewer 0000001, 0000002, …), and any student ID typed into a comment is replaced by `[student ID]`. The written feedback, scores, team names and submission times are public.

## How it works

A GitHub Action runs every hour, downloads the form responses, and writes `data.csv` (the responses without student IDs, via `publish.py`) and the results table above (via `results.py`). The dashboard is `index.html`, served by GitHub Pages, which reads `data.csv` in your browser.

For local use, `build.py` builds a single offline HTML file from a CSV export of the sheet, and `update.sh` refreshes it. Keep `data/` and the built HTML private, since they still contain student IDs (both are gitignored).
