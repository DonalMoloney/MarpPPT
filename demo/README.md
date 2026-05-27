# Demo

A nine-slide Marp deck about the workflow used to build it — brainstorm,
react, iterate, style, add data, and export.

## Run it

```bash
# 1. Install Marp (from repo root, once)
npm install

# 2. Generate the chart PNGs
pip install pandas matplotlib openpyxl
python make_charts.py

# 3. Preview in a browser
npx marp slides.md --preview

# 4. Export to PowerPoint
npx marp slides.md --pptx
open slides.pptx
```

Check the Notes pane in PowerPoint — every slide has presenter notes.

## What's in here

| Path | Purpose |
|---|---|
| `slides.md` | Nine-slide meta-deck (the workflow, built with the workflow) |
| `make_charts.py` | Reads `data/` → writes chart PNGs into `figures/` |
| `data/revenue.csv` | Source data for the CSV chart on slide 7 |
| `assets/stock/` | Stock images used in the deck |
| `figures/` | Generated chart PNGs — do not edit by hand |

## Adding your own chart

1. Drop a CSV or Excel file into `data/`.
2. Add a function to `make_charts.py` that reads it and calls `_save(fig, "your-name")`.
3. Reference the PNG from a slide: `![width:850px](figures/your-name.png)`.
4. Run `python make_charts.py`, then re-export: `npx marp slides.md --pptx`.

See [../docs/charts-from-data.md](../docs/charts-from-data.md) for Excel and multi-sheet variants.
