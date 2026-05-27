# Marp → PowerPoint

Write presentations in Markdown. Export to `.pptx`. Optionally build charts
from CSV or Excel.

## Layout

```
Marp/
├── demo/        Working example deck — start here
├── docs/        Short guides for new users
└── skills/      Agent skill for creating decks in this repo
```

## Start here

- **New?** Read [`docs/getting-started.md`](docs/getting-started.md).
- **Want to see it working?** `cd demo && cat README.md`.
- **Writing slides?** [`docs/writing-slides.md`](docs/writing-slides.md).
- **Charts from data?** [`docs/charts-from-data.md`](docs/charts-from-data.md).
- **Quick reference?** [`docs/cheatsheet.md`](docs/cheatsheet.md).

## One-liner

```bash
npm install
cd demo
python make_charts.py
npx marp slides.md --pptx
open slides.pptx
```
