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
