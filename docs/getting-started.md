# Getting Started

You describe the presentation. Claude builds it. You refine it.

## Install (once)

```bash
node --version            # need Node 18+
npm install               # installs Marp CLI from package.json
```

For chart slides (optional):

```bash
pip install pandas matplotlib openpyxl
```

---

## Stage 1 — Brainstorm

Tell Claude what you need and invoke the skill:

```
/create-marp-deck quarterly business review
```

Claude interviews you before writing a single slide:

- Who is the audience?
- What is the one thing they should leave knowing?
- How many slides?
- Any data or visuals to include?

The interview forces you to find the story before the slides exist.

---

## Stage 2 — React

Claude generates a complete Marp Markdown file — a concrete first draft.
No blank canvas. Push it around, then refine.

Every deck starts with this front matter:

```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
---
```

Slides are separated by `---` on its own line.

---

## Stage 3 — Iterate

Refine through conversation or direct editing.

**Ask Claude:**

```
Split slide 4 — it has two ideas.
Add a two-column layout: bullets left, image right.
Slide 6 is too dense — cut it to three bullets.
```

**Edit directly in VS Code:**

Install the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
extension → click the preview icon → live preview updates as you type.

Preview in a browser at any time:

```bash
npx marp slides.md --preview
```

---

## Stage 4 — Style

Set the theme in front matter:

```yaml
theme: default    # clean, minimal
theme: gaia       # bold, high-contrast
theme: uncover    # wide, modern
```

Override style on individual slides with HTML comment directives:

```markdown
<!-- _class: lead -->

# Big Centred Title

This slide uses the lead style — large, centred, no page number.

---

<!-- _backgroundColor: #1a1a2e -->
<!-- _color: white -->

## Dark Slide

Use sparingly — section dividers or dramatic reveals.
```

Add a breadcrumb header to help audiences track where they are:

```markdown
<!-- header: "Q3 Review > Revenue > **Detail**" -->
```

Bold text inside the header renders in the theme accent colour.

Ask Claude for styling: *"Make slide 3 dark with white text and use it as a section divider."*

See [writing-slides.md](writing-slides.md) for layout patterns (images, two-column, tables).

---

## Stage 5 — Add Data

Charts are PNGs. A Python script reads `data/` and writes them to `figures/`.
Slides reference the PNGs like any other image.

```
data/revenue.csv
      │
      ▼  python make_charts.py
figures/revenue-chart.png
      │
      ▼  ![width:850px](figures/revenue-chart.png)
slide
```

**Steps:**

1. Drop your CSV or Excel file into `data/`.
2. Add a function to `make_charts.py`:

```python
def my_chart() -> None:
    df = pd.read_csv(DATA / "my-data.csv")
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.bar(df["label"], df["value"])
    ax.set_title("My Chart")
    ax.grid(axis="y", alpha=0.3)
    _save(fig, "my-chart")
```

3. Call it at the bottom of `make_charts.py`:

```python
if __name__ == "__main__":
    revenue_from_csv()
    revenue_from_excel()
    my_chart()           # ← add this
```

4. Run the script:

```bash
python make_charts.py   # figures/my-chart.png is written
```

5. Reference the PNG in a slide:

```markdown
## My Data

![width:850px](figures/my-chart.png)

Source: `data/my-data.csv`
```

6. Re-export. Re-run `python make_charts.py` any time the data changes.

Ask Claude: *"Add a chart slide from data/my-data.csv."* — Claude adds the
function, runs the script, and inserts the slide.

See [charts-from-data.md](charts-from-data.md) for Excel, multiple sheets, and other variants.

---

## Stage 6 — Export

```bash
npx marp slides.md --preview    # live browser preview while editing
npx marp slides.md --pptx       # PowerPoint (preserves presenter notes)
npx marp slides.md --pdf        # PDF
```

> Use `--pptx`, not `--pptx-editable`. The editable variant strips presenter notes.

Open the `.pptx` before sharing — check the Notes pane if you added presenter notes.

The `.md` source file is version-controlled. The `.pptx` is generated output — you
can regenerate it any time.

---

## Next steps

- [writing-slides.md](writing-slides.md) — images, two-column layouts, tables, presenter notes
- [charts-from-data.md](charts-from-data.md) — full chart pipeline, Excel variants
- [cheatsheet.md](cheatsheet.md) — one-page syntax and CLI reference
- `demo/slides.md` — the complete working meta-deck (built with this workflow)
