# Charts From CSV Or Excel

Charts are PNGs. A Python script reads `data/` and writes them into `figures/`.
Slides reference the PNGs like any other image.

## The pattern

```
data/your-file.csv  ──►  make_charts.py  ──►  figures/your-name.png  ──►  slide
```

## From a CSV

`data/revenue.csv`:

```csv
quarter,revenue
Q1,120
Q2,146
Q3,171
Q4,208
```

`make_charts.py`:

```python
import pandas as pd, matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "data" / "revenue.csv")

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.plot(df["quarter"], df["revenue"], marker="o", linewidth=3)
ax.set_title("Quarterly Revenue")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(ROOT / "figures" / "revenue-chart.png", dpi=200)
```

Run it, then drop the PNG into a slide:

```markdown
## Quarterly Revenue

![width:850px](figures/revenue-chart.png)

Source: `data/revenue.csv`
```

## From Excel

Same script, swap the reader:

```python
df = pd.read_excel(ROOT / "data" / "revenue.xlsx", sheet_name="Revenue")
```

Useful variants:

```python
pd.read_excel("data/report.xlsx", sheet_name="Q4 Summary")          # one tab
pd.read_excel("data/report.xlsx", sheet_name=None)                  # all tabs → dict
pd.read_excel("data/report.xlsx", skiprows=2, usecols="A:D")        # trim noise
```

## Refresh workflow

Every time your data changes:

```bash
python make_charts.py
npx marp slides.md --pptx
```

See [demo/make_charts.py](../demo/make_charts.py) for a complete working script
that handles both CSV and Excel sources.
