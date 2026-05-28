# Getting Started (trimmed reference)

The six-stage workflow this skill drives.

## Install (once)
```bash
node --version            # need Node 18+
npm install               # installs Marp CLI from package.json
pip install pandas matplotlib openpyxl   # only if using chart slides
```

## The six stages
1. **Brainstorm** — interview the user (audience, takeaway, length, setting,
   material, tone) and agree an outline before drafting.
2. **Draft** — generate a complete first-pass `slides.md` with the required
   front matter. One idea per slide.
3. **Iterate** — apply natural-language edit requests; preview with
   `npx marp slides.md --preview`.
4. **Style** — pick a theme; apply per-slide directives (`_class: lead`,
   `_backgroundColor`, `header`, `footer`); add the `.columns` style if needed.
5. **Data** — only if the user has data. `data/` → `make_charts.py` →
   `figures/*.png` → slide.
6. **Export** — `--pptx` (preserves notes) or `--pdf`. Open the output before
   reporting done.

## Required front matter
```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
---
```

## Themes
`default` (clean) · `gaia` (bold) · `uncover` (wide, modern)

## VS Code preview
Install the "Marp for VS Code" extension → click the preview icon → live
preview updates as you type. Useful while iterating.
