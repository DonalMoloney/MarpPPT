# Cheatsheet

## Marp syntax

| Feature | Syntax |
| --- | --- |
| New slide | `---` on its own line |
| Slide numbers | `paginate: true` in front matter |
| Full background | `![bg](image.png)` |
| Right-side background | `![bg right:45%](image.png)` |
| Title-slide style | `<!-- _class: lead -->` |
| Size image by width | `![width:800px](image.png)` |
| Size image by height | `![height:400px](image.png)` |
| Presenter note | `<!-- note text -->` |

## Commands

```bash
npx marp deck.md --preview      # live browser preview
npx marp deck.md --pptx         # export PowerPoint (preserves notes)
npx marp deck.md --notes        # export notes as plain text
npx marp deck.md --pdf          # export PDF
```

## Gotchas

- `--pptx-editable` strips presenter notes. Use plain `--pptx`.
- PowerPoint export needs Chromium — installed automatically with Marp CLI.
- Always open the `.pptx` before sharing — a few Markdown features don't translate perfectly.
- Use PNG for charts; SVG works if the target PowerPoint supports it.
