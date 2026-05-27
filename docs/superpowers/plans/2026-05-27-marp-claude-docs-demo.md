# Marp + Claude Docs & Demo Redo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reposition the Marp repo docs and demo from "Marp → PowerPoint" to a six-stage Claude Code + Marp workflow covering brainstorm, react, iterate, style, data pipeline, and export.

**Architecture:** Five files are rewritten (README.md, CLAUDE.md, docs/getting-started.md, demo/slides.md, demo/README.md). Three reference docs (writing-slides.md, cheatsheet.md, charts-from-data.md) are kept as-is. The demo deck is a meta-deck about the workflow it demonstrates.

**Tech Stack:** Marp CLI, Markdown, Python (make_charts.py already exists), VS Code Marp extension.

---

## File Map

| File | Action |
|---|---|
| `README.md` | Rewrite |
| `CLAUDE.md` | Rewrite |
| `docs/getting-started.md` | Rewrite |
| `demo/slides.md` | Rewrite (meta-deck, 9 slides) |
| `demo/README.md` | Rewrite |
| `docs/writing-slides.md` | Keep |
| `docs/cheatsheet.md` | Keep |
| `docs/charts-from-data.md` | Keep |

---

## Task 1: Rewrite README.md

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace README.md with this exact content**

```markdown
# Claude Code + Marp

Write presentations in Markdown. Use Claude to find the story.

## Layout

```
Marp/
├── demo/        Meta-deck: built with the workflow it describes
├── docs/        Guides for each stage of the workflow
└── skills/      Agent skill for creating decks in this repo
```

## Six-stage workflow

1. **Brainstorm** — `/create-marp-deck [topic]` — Claude interviews you
2. **React** — Claude generates a full draft, no blank canvas
3. **Iterate** — refine by prompt or edit in VS Code with the Marp extension
4. **Style** — theme, per-slide CSS overrides, section dividers
5. **Add Data** — CSV/Excel → Python chart → PNG → slide
6. **Export** — HTML, PDF, PPTX

## Quick start

```bash
npm install
cd demo
python make_charts.py
npx marp slides.md --pptx
open slides.pptx
```

## Docs

- [Getting started](docs/getting-started.md) — full six-stage walkthrough
- [Writing slides](docs/writing-slides.md) — layouts and image patterns
- [Charts from data](docs/charts-from-data.md) — CSV and Excel pipeline
- [Cheatsheet](docs/cheatsheet.md) — syntax and CLI reference
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: reposition README to Claude Code + Marp workflow"
```

---

## Task 2: Rewrite CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Replace CLAUDE.md with this exact content**

```markdown
# Marp + Claude — Project Instructions

This repo helps users build presentations in Markdown using Claude Code and Marp.
The workflow has six stages. Follow them when a user asks to create or edit a deck.

---

## Six-Stage Workflow

### 1 — Brainstorm
Invoke the `creating-marp-decks` skill (in `skills/creating-marp-decks/SKILL.md`).
Interview the user before writing any slides:
- Who is the audience?
- What is the one thing they should leave knowing?
- How many slides?
- Any data or images to include?

### 2 — React
Generate a complete Marp Markdown file as a first draft.
Start every deck with this front matter — no exceptions:

```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
---
```

One idea per slide. Separate slides with `---` on its own line.

### 3 — Iterate
Accept natural-language edit requests and apply them directly:
- "Split slide 4 — it has two ideas"
- "Add a two-column layout: bullets left, image right"
- "Slide 6 is too dense — cut to three bullets"

Preview command: `npx marp slides.md --preview`

### 4 — Style
Apply theme and per-slide overrides when asked.

**Themes** (set in front matter):
```yaml
theme: default    # clean, minimal
theme: gaia       # bold, high-contrast
theme: uncover    # wide, modern
```

**Per-slide directives** (HTML comment at top of slide):
```markdown
<!-- _class: lead -->                  ← large centred title
<!-- _backgroundColor: #1a1a2e -->     ← dark background
<!-- _color: white -->                 ← white text
<!-- header: "Section > **Current**" --> ← breadcrumb (bold = blue)
```

**Two-column layout** — add this `<style>` block once near the top of the deck,
then use `<div class="columns">` anywhere:
```html
<style>
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }
.columns img { width: 100%; }
</style>
```

### 5 — Add Data
Use the pipeline in `demo/` as the canonical pattern:

```
data/your-file.csv
      │
      ▼  python make_charts.py
figures/your-name.png
      │
      ▼  ![width:850px](figures/your-name.png) in slides.md
slide
```

Steps:
1. Drop the file into `data/`.
2. Add a function to `make_charts.py` that reads it and calls `_save(fig, "name")`.
3. Run `python make_charts.py` — confirm the PNG appears in `figures/`.
4. Add the image reference to the slide.
5. Re-export.

### 6 — Export
```bash
npx marp slides.md --preview    # live preview while editing
npx marp slides.md --pptx       # PowerPoint (preserves presenter notes)
npx marp slides.md --pdf        # PDF
```

---

## Hard Rules

- Use `--pptx`. NEVER use `--pptx-editable` — it strips presenter notes.
- Image paths in `slides.md` are relative to `slides.md`, not the repo root.
- Always re-run `python make_charts.py` after data changes.
- Speaker notes are HTML comments inside the slide body: `<!-- ... -->`.
- Do not hand-edit anything in `figures/`. It is generated output.

---

## Reference Files

- `demo/slides.md` — complete working meta-deck
- `demo/make_charts.py` — chart generation script (CSV + Excel)
- `docs/getting-started.md` — six-stage walkthrough for users
- `docs/writing-slides.md` — layout and image patterns
- `docs/charts-from-data.md` — full chart pipeline
- `docs/cheatsheet.md` — syntax and CLI reference
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: rewrite CLAUDE.md as Claude-focused workflow instructions"
```

---

## Task 3: Rewrite docs/getting-started.md

**Files:**
- Modify: `docs/getting-started.md`

- [ ] **Step 1: Replace docs/getting-started.md with this exact content**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add docs/getting-started.md
git commit -m "docs: rewrite getting-started as six-stage Claude workflow"
```

---

## Task 4: Rewrite demo/slides.md

**Files:**
- Modify: `demo/slides.md`

Note: The existing stock images (`assets/stock/workspace-charts.png`, `assets/stock/team-workshop.png`) are reused. The existing `figures/revenue-chart.png` is reused (generated by `make_charts.py`).

- [ ] **Step 1: Replace demo/slides.md with this exact content**

````markdown
---
marp: true
theme: default
paginate: true
size: 16:9
---

![bg](assets/stock/workspace-charts.png)

# Build Presentations with Claude Code + Marp

Six stages from blank page to export

<!--
Open by explaining that this deck was built using the workflow it describes.
The meta-point: writing the deck first helped organise the article.
-->

---

![bg right:40%](assets/stock/team-workshop.png)

## The Problem: Blank-Canvas Paralysis

- The hard part of a presentation is **finding the story**
- A blank slide deck is just a blank page
- Claude interviews you first — story before slides

<!--
Don't start in PowerPoint. Start by answering questions about what you want to say.
-->

---

## Stage 1 — Brainstorm

Tell Claude what you need. It interviews you before writing anything.

```
/create-marp-deck quarterly business review
```

Claude asks:
- Who is the audience?
- What is the one thing they should leave knowing?
- What data or visuals do you have?
- How many slides?

<!--
The interview is the real work. The slides are just the output.
-->

---

## Stage 2 — React

Claude generates a complete first draft. No blank canvas.

```markdown
---
marp: true
theme: default
paginate: true
---

# Q3 Business Review
Finance · 2026

---

## Revenue Grew 22% Quarter-on-Quarter
- Strongest growth in Q2 and Q4
- Driven by new enterprise accounts
```

Edit it directly or ask Claude to change it — both work.

<!--
A concrete draft is something you can push around and reshape. That's the point.
-->

---

## Stage 3 — Iterate

Refine through conversation or direct editing.

**Ask Claude:**
- "Split slide 4 — it has two ideas"
- "Add a two-column layout: bullets left, image right"
- "Slide 6 is too dense — cut to three bullets"

**In VS Code:** install the Marp extension → live preview updates as you type.

```bash
npx marp slides.md --preview   # live browser preview
```

<!--
Use Claude for structural changes. Use VS Code for fine-tuning wording.
-->

---

## Stage 4 — Style

Set the theme in front matter. Override style per slide.

```markdown
---
theme: gaia        # default | gaia | uncover
---

<!-- _class: lead -->          ← big centred title slide

<!-- _backgroundColor: #1a1a2e -->
<!-- _color: white -->         ← dark section divider

<!-- header: "Q3 Review > **Revenue** > Detail" -->
```

Ask Claude: *"Make slide 3 dark with white text — use it as a section divider."*

<!--
CSS class annotations let you vary style without editing the theme file.
Bold text in the header renders in the theme accent colour.
-->

---

## Stage 5 — Add Data

```
data/revenue.csv
      │
      ▼  python make_charts.py
figures/revenue-chart.png
      │
      ▼  ![width:850px](figures/revenue-chart.png)
slide
```

![width:680px](figures/revenue-chart.png)

Ask Claude: *"Add a chart slide from data/revenue.csv."*

<!--
Re-run make_charts.py any time the data changes, then re-export.
Claude adds the function, runs the script, and inserts the slide.
-->

---

## Stage 6 — Export

```bash
npx marp slides.md --preview    # live preview while editing
npx marp slides.md --pptx       # PowerPoint — preserves presenter notes
npx marp slides.md --pdf        # PDF
```

The `.md` source is version-controlled.  
The `.pptx` is generated output — regenerate any time.

> Use `--pptx`, not `--pptx-editable`. The editable variant strips presenter notes.

<!--
Show the Notes pane in PowerPoint before sharing. Presenter notes transfer.
-->

---

<!-- _class: lead -->

## Start with the story.

One idea per slide.  
Let Claude find the structure.

<!--
The workflow is not about Marp. It is about thinking before writing.
-->
````

- [ ] **Step 2: Commit**

```bash
git add demo/slides.md
git commit -m "demo: rewrite slides.md as nine-slide Claude+Marp meta-deck"
```

---

## Task 5: Rewrite demo/README.md

**Files:**
- Modify: `demo/README.md`

- [ ] **Step 1: Replace demo/README.md with this exact content**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add demo/README.md
git commit -m "demo: update README to describe meta-deck and six-stage workflow"
```

---

## Task 6: Verify the demo renders

**Files:** None modified — verification only.

- [ ] **Step 1: Generate chart PNGs**

```bash
cd /Users/donalmoloney/PycharmProjects/Marp/demo
python make_charts.py
```

Expected output:
```
  saved figures/revenue-chart.png
  saved figures/revenue-excel-chart.png
```

- [ ] **Step 2: Export the deck to PowerPoint**

```bash
npx marp slides.md --pptx
```

Expected: exits 0, `slides.pptx` created next to `slides.md`.

- [ ] **Step 3: Confirm PNG reference resolves**

```bash
ls figures/revenue-chart.png
```

Expected: file exists (slide 7 references it as `figures/revenue-chart.png`).

- [ ] **Step 4: Commit verification note (no code change needed if all passed)**

If any step fails, fix the path or content in `demo/slides.md` and re-run.

---

## Self-Review

**Spec coverage:**
- ✅ README.md — rewritten (Task 1)
- ✅ CLAUDE.md — rewritten (Task 2)
- ✅ docs/getting-started.md — rewritten (Task 3)
- ✅ demo/slides.md — nine-slide meta-deck (Task 4)
- ✅ demo/README.md — updated (Task 5)
- ✅ Styling — covered in Task 2 (CLAUDE.md), Task 3 (getting-started Stage 4), Task 4 (slide 6)
- ✅ Data pipeline — shown step-by-step with ASCII diagram in Task 3 and Task 4 (slide 7)
- ✅ Charts connected — pipeline diagram in demo slide 7 shows `data/ → make_charts.py → figures/ → slide`
- ✅ Export — covered in Task 3 (Stage 6) and Task 4 (slide 8)
- ✅ reference docs untouched — writing-slides.md, cheatsheet.md, charts-from-data.md kept

**Placeholder scan:** No TBDs, no TODOs, no vague steps. All file content is complete.

**Consistency:** Image paths in `demo/slides.md` use `assets/stock/` and `figures/` — both match the existing directory structure. The `figures/revenue-chart.png` reference on slide 7 is generated by the existing `make_charts.py`.
