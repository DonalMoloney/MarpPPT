# Getting Started

You write slides in Markdown. Marp turns them into a PowerPoint file.

## 1. Install once

```bash
node --version            # need Node 18+
npm install               # installs Marp from package.json
```

If you want the chart demo too:

```bash
pip install pandas matplotlib openpyxl
```

## 2. Try the demo

```bash
cd demo
python make_charts.py                  # generates the chart PNGs
npx marp slides.md --preview           # live preview in your browser
npx marp slides.md --pptx              # writes slides.pptx
```

Open `demo/slides.pptx`. That's it.

## 3. Make your own deck

Create a file `mydeck.md` anywhere:

```markdown
---
marp: true
theme: default
paginate: true
---

# My Deck
Author · Date

---

## First Slide

- One idea per slide
- Separate slides with `---`
```

Then:

```bash
npx marp mydeck.md --preview
npx marp mydeck.md --pptx
```

## Next steps

- [writing-slides.md](writing-slides.md) — layouts, images, presenter notes
- [charts-from-data.md](charts-from-data.md) — turn a CSV or Excel file into a chart slide
- [cheatsheet.md](cheatsheet.md) — one-page syntax reference
