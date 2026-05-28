# Charts From CSV Or Excel (trimmed reference)

Pipeline: `data/<file>.csv|xlsx → make_charts.py → figures/<name>.png → slide`

## Minimal script
`make_charts.py` beside `slides.md`:
```python
import pandas as pd, matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIG  = ROOT / "figures"; FIG.mkdir(exist_ok=True)

def _save(fig, name):
    fig.tight_layout()
    fig.savefig(FIG / f"{name}.png", dpi=200)
    plt.close(fig)

def revenue():
    df = pd.read_csv(ROOT / "data" / "revenue.csv")
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(df["quarter"], df["revenue"], marker="o", linewidth=3)
    ax.set_title("Quarterly Revenue")
    ax.grid(True, alpha=0.3)
    _save(fig, "revenue-chart")

if __name__ == "__main__":
    revenue()
```

## Excel variants
```python
pd.read_excel("data/report.xlsx", sheet_name="Q4 Summary")     # one tab
pd.read_excel("data/report.xlsx", sheet_name=None)             # all tabs → dict
pd.read_excel("data/report.xlsx", skiprows=2, usecols="A:D")   # trim noise
```

## Reference from a slide
```markdown
## Quarterly Revenue

![width:850px](figures/revenue-chart.png)

Source: `data/revenue.csv`
```

## Refresh
Run `python make_charts.py` after every data or code change — `npx marp` does
NOT regenerate figures.

## Sizing tips
- `figsize=(10, 5.5)` fits a 16:9 slide with room for a title.
- `dpi=200` is sharp on projectors; drop to `dpi=160` if file size matters.
- Use PNG. SVG works if the destination PowerPoint supports it.
