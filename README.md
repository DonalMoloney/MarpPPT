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
