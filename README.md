# EPC 2026 video feedback dashboard

A local dashboard for the "Feedback for video (EPC 2026) (Responses)" Google Form, where students rate other teams' videos on biases and fallacies.

The output is one self-contained HTML file with no libraries or network calls. It shows a team leaderboard with a reviewer-adjusted score, the score distribution, how lenient reviewers are, data-quality flags, feedback themes, the lowest-rated teams, and searchable comments.

## Files

- `template.html` is the dashboard source. The data gets injected at the `/*DATA*/` placeholder.
- `build.py` builds `epc-feedback-dashboard.html` from the CSV and the template, and sanity-checks the CSV first.
- `update.sh` loads a fresh Drive export, diffs it against the current CSV, rebuilds, checks the page for JS errors in headless Chromium, prints per-team averages and opens the page.
- `data/responses.csv` is the latest export of the sheet.

## Update from the live sheet

Ask Claude Code to "update" the dashboard. It downloads the sheet as CSV through the Google Drive connector, then runs:

```bash
./update.sh <path to the download_file_content JSON>
```

To do it by hand, export the sheet as CSV to `data/responses.csv` and rebuild:

```bash
python3 -I build.py data/responses.csv template.html epc-feedback-dashboard.html
```

## Privacy

`data/`, the built HTML (it embeds the data) and `shot.png` contain student IDs and personal feedback. They are gitignored, so don't share them.
