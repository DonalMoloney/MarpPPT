# Writing Slides (trimmed reference)

## Slide separator
`---` on its own line starts a new slide.

## Front matter (required, every deck)
```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
---
```

## Images
```markdown
![bg](path.png)                  Full-slide background
![bg right:45%](path.png)        Right 45% of the slide
![width:850px](path.png)         Inline, fixed width
![height:400px](path.png)        Inline, fixed height
```
Paths are relative to the `.md` file.

## Presenter notes
HTML comments inside a slide body become PowerPoint Notes:
```markdown
## Slide title

content

<!--
- Call out the Q2 jump.
- Full-year growth: 73%.
-->
```
Preserved by `--pptx`. Stripped by `--pptx-editable`.

## Two columns
Add once near the top of the deck:
```html
<style>
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }
.columns img { width: 100%; }
</style>
```
Use anywhere:
```markdown
<div class="columns">
  <div><h3>Before</h3><img src="figures/before.png"></div>
  <div><h3>After</h3><img src="figures/after.png"></div>
</div>
```

## Tables
Standard Markdown. Right-align numbers with `---:`.
```markdown
| Quarter | Revenue | Growth |
| --- | ---: | ---: |
| Q1 | $120k | — |
| Q2 | $146k | 22% |
```
