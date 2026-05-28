---
marp: true
theme: default
paginate: true
size: 16:9
---

<style>
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: center; }
.columns img { width: 100%; }
table { font-size: 0.85em; }
</style>

![bg right:30%](assets/stock/ferrari.png)

# Build Presentations with Claude Code + Marp

Six stages from blank page to export

<!--
Open by explaining that this deck was built using the workflow it describes.
The meta-point: writing the deck first helped organise the article.
-->

---

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

Ask Claude: *"Add a chart slide from data/revenue.csv."*

<!--
Re-run make_charts.py any time the data changes, then re-export.
Claude adds the function, runs the script, and inserts the slide.
-->

---

## Example — Data In, Chart Out

<div class="columns">
<div>

**`data/revenue.csv`** — read in and formatted

| Quarter | Revenue ($k) |
| --- | ---: |
| Q1 | 120 |
| Q2 | 146 |
| Q3 | 171 |
| Q4 | 208 |

*Full-year growth: **73%***

</div>
<div>

![width:100%](figures/revenue-chart.png)

</div>
</div>

<!--
Same numbers, two views. The table proves the chart; the chart sells the story.
Both are generated from one CSV — edit the data and re-run make_charts.py.
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
