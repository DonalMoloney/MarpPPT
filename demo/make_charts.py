"""Generate chart PNGs from CSV and Excel sources for the demo deck."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)


def _save(fig, name: str) -> None:
    fig.tight_layout()
    fig.savefig(FIGURES / f"{name}.png", dpi=200)
    plt.close(fig)
    print(f"  saved figures/{name}.png")


def revenue_from_csv() -> None:
    df = pd.read_csv(DATA / "revenue.csv")
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(df["quarter"], df["revenue"], marker="o", linewidth=3)
    ax.set_title("Quarterly Revenue (from CSV)")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Revenue ($k)")
    ax.grid(True, alpha=0.3)
    _save(fig, "revenue-chart")


def revenue_from_excel() -> None:
    xlsx = DATA / "revenue.xlsx"
    if not xlsx.exists():
        # First run: build the Excel sample from the CSV so the demo is self-contained.
        pd.read_csv(DATA / "revenue.csv").to_excel(xlsx, index=False, sheet_name="Revenue")
        print(f"  created data/revenue.xlsx")
    df = pd.read_excel(xlsx, sheet_name="Revenue")
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.bar(df["quarter"], df["revenue"], color="#4C72B0")
    ax.set_title("Quarterly Revenue (from Excel)")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Revenue ($k)")
    ax.grid(axis="y", alpha=0.3)
    _save(fig, "revenue-excel-chart")


if __name__ == "__main__":
    revenue_from_csv()
    revenue_from_excel()
