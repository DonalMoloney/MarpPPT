# Claude Code + Marp

Build presentations in Markdown. Let Claude find the story, draft the slides,
and generate charts from your data — then export to PowerPoint or PDF.

---

## Why this repo

Slide decks fail at the *thinking* stage, not the layout stage. This repo pairs
[Marp](https://marp.app) (Markdown → slides) with a Claude Code skill that
**interviews you before writing anything**, then drives a repeatable
six-stage workflow from blank file to a polished `.pptx`.

- **Version-controlled decks.** Your source is plain Markdown — diffable,
  reviewable, mergeable.
- **Data-driven slides.** CSV or Excel → Python chart → PNG → slide.
  Re-run one script when the data changes.
- **Presenter notes preserved.** Exports to `.pptx` with the Notes pane
  populated.
- **One command to preview, one to export.** No GUI required.

---

## Requirements

| Tool | Version | Purpose |
| --- | --- | --- |
| Node.js | 18+ | Runs the Marp CLI |
| Python | 3.10+ | Optional — only for chart slides |
| Claude Code | latest | Drives the workflow via the skill |

---

## Install

```bash
git clone <this-repo> && cd Marp
npm install                                  # Marp CLI
pip install pandas matplotlib openpyxl       # only if using chart slides
```

---

## Quick start

```bash
cd demo
python make_charts.py            # regenerate figures from data/
npx marp slides.md --preview     # live browser preview
npx marp slides.md --pptx        # export PowerPoint (with presenter notes)
open slides.pptx
```

Or, in Claude Code:

```
/create-marp-deck quarterly business review
```

Claude will interview you (audience, takeaway, length, theme, speaker notes),
propose an outline, draft the deck, and iterate with you.

---

## The six-stage workflow

| # | Stage | What happens |
| --- | --- | --- |
| 1 | **Brainstorm** | Claude interviews you — audience, takeaway, length, tone, theme, notes. Outline approved before any slide is written. |
| 2 | **Draft** | Full first-pass `slides.md` with required front matter. One idea per slide. |
| 3 | **Iterate** | Natural-language edits — split, merge, reorder, condense. Live preview via `npx marp ... --preview`. |
| 4 | **Style** | Theme (`default` / `gaia` / `uncover`), per-slide directives, two-column layouts, custom CSS. |
| 5 | **Add Data** | `data/*.csv\|xlsx` → `make_charts.py` → `figures/*.png` → slide. |
| 6 | **Export** | `--pptx` (preserves notes), `--pdf`, or `--html`. |

Full walkthrough: [`docs/getting-started.md`](docs/getting-started.md).

---

## Repository layout

```
Marp/
├── README.md                     This file
├── CLAUDE.md                     Project-level instructions for Claude
├── package.json                  Marp CLI dependency
├── demo/                         Working meta-deck — built with the workflow it describes
│   ├── slides.md                 The deck source
│   ├── make_charts.py            Generates figures/ from data/
│   ├── data/                     CSV / Excel sources
│   ├── figures/                  Generated PNGs (do not hand-edit)
│   └── assets/                   Static images
├── docs/                         User-facing guides
│   ├── getting-started.md        Six-stage walkthrough
│   ├── writing-slides.md         Layout, image, and column patterns
│   ├── charts-from-data.md       Full data-to-chart pipeline
│   └── cheatsheet.md             Syntax and CLI reference
└── skills/
    └── creating-marp-decks/      Claude Code skill
        ├── SKILL.md              Skill definition
        └── references/           Trimmed, skill-local copies of the docs
```

---

## Common commands

```bash
npx marp slides.md --preview     # live browser preview
npx marp slides.md --pptx        # PowerPoint (preserves presenter notes)
npx marp slides.md --pdf         # PDF
npx marp slides.md --html        # standalone HTML
python make_charts.py            # rebuild figures/ from data/
```

> Always use `--pptx`. **Never** `--pptx-editable` — it strips presenter notes.

---

## Documentation

- [Getting started](docs/getting-started.md) — full six-stage walkthrough
- [Writing slides](docs/writing-slides.md) — layouts, images, columns, tables
- [Charts from data](docs/charts-from-data.md) — CSV and Excel pipeline
- [Cheatsheet](docs/cheatsheet.md) — syntax and CLI reference
- [`demo/slides.md`](demo/slides.md) — complete working deck

---

## License

MIT.
