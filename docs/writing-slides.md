# Writing Slides

## Slide separator

Three dashes on their own line start a new slide:

```markdown
## Slide One

content

---

## Slide Two
```

## Front matter

The block at the top of every Marp file:

```markdown
---
marp: true
theme: default
paginate: true
---
```

## Images

```markdown
![bg](assets/photo.png)                  Full-slide background
![bg right:45%](assets/photo.png)        Right 45% of the slide
![width:850px](figures/chart.png)        Inline, fixed width
![height:400px](figures/chart.png)       Inline, fixed height
```

Store reusable images in `assets/` and generated charts in `figures/`.

## Presenter notes

HTML comments become speaker notes. They show up in PowerPoint's Notes pane
and never appear on the slide itself.

```markdown
## Quarterly Revenue

![width:850px](figures/revenue-chart.png)

<!--
- Call out the Q2 jump.
- Mention full-year growth was 73%.
-->
```

> Notes are preserved by `npx marp deck.md --pptx`. They are NOT preserved by
> `--pptx-editable`.

## Two images side by side

Add the style once near the top of your deck:

```html
<style>
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }
.columns img { width: 100%; }
</style>
```

Then use it:

```markdown
## Before And After

<div class="columns">
  <div><h3>Before</h3><img src="figures/before.png"></div>
  <div><h3>After</h3><img src="figures/after.png"></div>
</div>
```

## Tables

Standard Markdown tables work. Right-align numbers with `---:`.

```markdown
| Quarter | Revenue | Growth |
| --- | ---: | ---: |
| Q1 | $120k | — |
| Q2 | $146k | 22% |
```
