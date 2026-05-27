# Demo

A working Marp deck that exports to PowerPoint, including charts built from
CSV and Excel.

## Run it

```bash
# 1. Install Marp once (run from the repo root)
npm install

# 2. Generate the chart PNGs from data/
pip install pandas matplotlib openpyxl
python make_charts.py

# 3. Preview live in a browser
npx marp slides.md --preview

# 4. Export to PowerPoint
npx marp slides.md --pptx
```

`slides.pptx` lands next to `slides.md`. Open it and check the Notes pane.

## What's in here

| Path | Purpose |
| --- | --- |
| `slides.md` | Main demo deck — stock images, table, CSV chart, Excel chart, notes |
| `project.md` | Second example deck (Philadelphia) showing background-image layouts |
| `data/revenue.csv` | Source data for the CSV chart |
| `data/revenue.xlsx` | Generated on first run of `make_charts.py` |
| `make_charts.py` | Reads `data/` → writes PNGs into `figures/` |
| `assets/` | Stock and project images referenced by the decks |
| `figures/` | Generated chart PNGs (do not edit by hand) |

## Adding your own chart

1. Drop a CSV or XLSX into `data/`.
2. Add a function to `make_charts.py` that reads it and calls `_save(fig, "your-name")`.
3. Reference the PNG from a slide: `![width:850px](figures/your-name.png)`.
4. Re-run `python make_charts.py`, then re-export with `npx marp slides.md --pptx`.
