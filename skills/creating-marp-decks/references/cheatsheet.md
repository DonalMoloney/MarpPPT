# Cheatsheet (trimmed reference)

## Syntax
| Feature | Syntax |
| --- | --- |
| New slide | `---` on its own line |
| Slide numbers | `paginate: true` in front matter |
| Full background | `![bg](image.png)` |
| Right-side background | `![bg right:45%](image.png)` |
| Title-slide style | `<!-- _class: lead -->` |
| Dark slide | `<!-- _backgroundColor: #1a1a2e -->` + `<!-- _color: white -->` |
| Breadcrumb header | `<!-- header: "Section > **Current**" -->` |
| Width-sized image | `![width:800px](image.png)` |
| Height-sized image | `![height:400px](image.png)` |
| Presenter note | `<!-- note text -->` inside the slide body |

## Themes
`default` · `gaia` · `uncover` (set in front matter)

## Commands
```bash
npx marp deck.md --preview      # live browser preview
npx marp deck.md --pptx         # PowerPoint (preserves notes)
npx marp deck.md --pdf          # PDF
npx marp deck.md --html         # standalone HTML
npx marp deck.md --notes        # plain-text notes export
```

## Gotchas
- NEVER use `--pptx-editable` — strips presenter notes.
- Image paths are relative to the `.md` file, not the repo root.
- Re-run `python make_charts.py` after data changes; Marp does not.
- Open the `.pptx` before sharing — spot-check images and Notes pane.
- PowerPoint export needs Chromium (installed automatically with Marp CLI).
