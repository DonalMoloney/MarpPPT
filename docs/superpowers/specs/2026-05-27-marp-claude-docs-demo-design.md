---
name: marp-claude-docs-demo-redo
description: Reposition the Marp repo docs and demo from "Marp → PowerPoint" to "Claude Code + Marp" workflow, covering brainstorm, react, iterate, style, data pipeline, and export stages.
metadata:
  type: project
---

# Design: Marp + Claude Docs & Demo Redo

**Date:** 2026-05-27
**Basis:** [FreeCodeCamp — How to Use Claude Code and Marp to Think Through Presentations](https://www.freecodecamp.org/news/how-to-use-claude-code-and-marp-to-think-through-presentations/)

---

## Goal

Reposition the repo from a "Marp → PowerPoint with CSV charts" tutorial into a "Claude Code + Marp" workflow guide. The docs and demo should show how Claude drives presentation creation — not just how Marp exports files.

---

## Files Changed

| File | Action |
|---|---|
| `README.md` | Rewrite — new positioning, updated one-liner |
| `CLAUDE.md` | Rewrite — Claude-driven workflow, prompting examples, staging guidance |
| `docs/getting-started.md` | Rewrite — six stages with examples |
| `demo/slides.md` | New meta-deck (9 slides) |
| `demo/README.md` | Update to explain the meta-demo |
| `docs/writing-slides.md` | Keep — still accurate reference |
| `docs/cheatsheet.md` | Keep — still accurate reference |
| `docs/charts-from-data.md` | Keep — still accurate reference |

---

## README.md

**Positioning:** "Write presentations in Markdown. Use Claude to find the story."

**Sections:**
- One-line description
- Layout table (demo/, docs/, skills/)
- Six-stage workflow (Brainstorm → React → Iterate → Style → Data → Export)
- One-liner to run the demo
- Links to docs

---

## CLAUDE.md

Replace the current step-by-step Marp tutorial with Claude-focused guidance:

1. **What this repo is** — Claude+Marp workflow, not just a Marp reference
2. **Six stages** — brief description of each with example prompts
3. **Styling** — how to ask Claude for themes, per-slide overrides, section dividers
4. **Data pipeline** — how to describe to Claude what the `data/ → figures/ → slide` pipeline is
5. **Export** — `--pptx` vs `--pptx-editable`, when to use each
6. **Hard rules** — same as current skill SKILL.md hard rules (never `--pptx-editable` without post-processing)

---

## docs/getting-started.md

**Structure:**

1. **Install** — Node 18+, `npm install`, optional pip for charts
2. **Stage 1 — Brainstorm** — invoke `/create-marp-deck [topic]`, Claude interviews you
3. **Stage 2 — React** — Claude generates full draft, eliminate blank-canvas paralysis
4. **Stage 3 — Iterate** — natural language prompts ("split slide 6", "add a two-column layout")
5. **Stage 4 — Style** — themes (`default`/`gaia`/`uncover`), per-slide CSS (`<!-- _class: lead -->`), section dividers, asking Claude to apply styles
6. **Stage 5 — Add Data** — full pipeline shown explicitly:
   ```
   data/revenue.csv
         ↓ python make_charts.py
   figures/revenue-chart.png
         ↓ ![width:850px](figures/revenue-chart.png) in slides.md
   slide
   ```
   Steps: drop CSV → add function to `make_charts.py` → run script → reference PNG → re-export
7. **Stage 6 — Export** — HTML, PDF, PPTX commands; note on presenter notes
8. **Next steps** — links to writing-slides.md, charts-from-data.md, cheatsheet.md

---

## demo/slides.md

**Topic:** Meta-deck — "Build Presentations with Claude Code + Marp"
**Theme:** `default`, `paginate: true`, `16:9`

**9-slide structure:**

| # | Title | Layout | Notes |
|---|---|---|---|
| 1 | Build Presentations with Claude Code + Marp | `![bg]` full background | Subtitle: "Six stages from blank page to export" |
| 2 | The Problem: Blank-Canvas Paralysis | `![bg right:40%]` image | Story-first framing from article |
| 3 | Stage 1 — Brainstorm | Bullets | `/create-marp-deck [topic]`, Claude interviews you |
| 4 | Stage 2 — React | Code block | Show minimal Marp frontmatter + first slide Claude generates |
| 5 | Stage 3 — Iterate | Bullets + example prompts | Natural language edits |
| 6 | Stage 4 — Style | Code block | Theme choice, `<!-- _class: lead -->`, per-slide overrides |
| 7 | Stage 5 — Add Data | Mermaid pipeline diagram | `data/ → make_charts.py → figures/ → slide` |
| 8 | Stage 6 — Export | Code block | `--pptx`, `--pdf`, `--preview` commands |
| 9 | Summary | `<!-- _class: lead -->` | "Start with the story. One idea per slide." |

**Presenter notes** on every slide (HTML comments).

---

## demo/README.md

Update to:
- Explain the meta-demo topic
- Run instructions (same as current: `python make_charts.py` then `npx marp slides.md --pptx`)
- What's in the demo folder table (updated)

---

## Spec Self-Review

- No TBDs or placeholders
- Architecture consistent across all sections
- Scope is focused — six stages, nine slides, five files changed
- No ambiguity: chart pipeline is shown step-by-step; styling is concrete (class names, theme values)

