# Marp Tutorial — Building Slides with Claude

This is a tutorial for using **Claude** to build presentations with **Marp**. Read top-to-bottom the first time; after that, jump to the section you need.

---

## 1. What is Marp?

Marp (Markdown Presentation Ecosystem) turns plain Markdown files into slide decks. You write `.md`, export to HTML / PDF / PPTX.

### Why Marp instead of PowerPoint?

- **Plain text** — version control with git, diff slides like code
- **Fast** — no dragging boxes, just type
- **Reusable** — one source → HTML, PDF, PPTX
- **AI-friendly** — Claude edits `.md` directly; no binary files to wrestle with
- **Themeable** — CSS-based styling, consistent look across decks
- **Portable** — works in any editor; live preview in VS Code

---

## 2. Install (one-time setup)

Pick one path:

### Option A — VS Code (easiest)
1. Install [VS Code](https://code.visualstudio.com/)
2. Install the **Marp for VS Code** extension (search "Marp" in Extensions)
3. Open any `.md` with `marp: true` in the frontmatter → click the Marp preview icon (top-right)

### Option B — CLI (for exporting PDF/PPTX)
Requires Node.js (`brew install node` on macOS).

```bash
npm install -g @marp-team/marp-cli
marp --version            # verify
```

You can use both — VS Code for authoring, CLI for export.

---

## 3. Your first deck

Create `hello.md`:

```markdown
---
marp: true
theme: default
paginate: true
---

# Hello, Marp!

Built with Claude.

---

# Why this is cool

- Plain Markdown
- Version-controlled
- AI editable
```

Preview in VS Code, or run:
```bash
marp hello.md --preview
```

`---` separates slides. The block at the top is **frontmatter** — it configures the whole deck.

---

## 4. How to ask Claude

Talk to Claude in plain English. Examples:

- "Add a title slide for a Q3 review"
- "Turn this README into a 10-slide deck"
- "Split this slide — too much text"
- "Add a two-column layout: bullets on left, image on right"
- "Add a Mermaid flowchart showing login flow"
- "Make slide 3 use a dark background"
- "Export this to PDF"

Claude edits `hello.md` directly. You preview, iterate, repeat.

**Tip:** point Claude at the file ("edit `hello.md`") and describe the *outcome*, not the Markdown syntax. Claude knows Marp.

---

## 5. Frontmatter — deck-wide config

```yaml
---
marp: true
theme: default        # default | gaia | uncover
paginate: true        # show slide numbers
size: 16:9            # or 4:3
backgroundColor: '#fff'
header: 'My Talk'     # appears on every slide
footer: '2026'
---
```

### Per-slide overrides
Put these at the top of a slide (note the leading `_`):

```markdown
<!-- _class: lead -->
<!-- _backgroundColor: black -->
<!-- _color: white -->
```

---

## 6. Adding content

### Text & lists
Standard Markdown — `#` headers, `-` bullets, **bold**, *italic*, `code`.

### Images
```markdown
![width:400px](logo.png)           # sized inline image
![bg right:40%](photo.jpg)         # background filling right 40% of slide
![bg](cover.jpg)                   # full-slide background
![bg opacity:.3](cover.jpg)        # dim a background
```

### Code blocks
Triple-backtick + language → syntax highlighting:

    ```python
    def hello():
        print("hi")
    ```

### Tables
```markdown
| Tool | Speed | Notes      |
|------|-------|------------|
| Marp | Fast  | Text-based |
| PPT  | Slow  | Binary     |
```

### Math (KaTeX, built in)
`$E = mc^2$` inline, or `$$ ... $$` for a block.

---

## 7. Layouts

### Two columns

```markdown
<div class="columns">
<div>

### Left
- point 1
- point 2

</div>
<div>

### Right
![](chart.png)

</div>
</div>

<style>
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
</style>
```

You can also ask Claude: *"Make this a two-column slide with text on left, image on right"* — it'll write the HTML+CSS for you.

### Lead/title slide
```markdown
<!-- _class: lead -->

# Big centered title
```

---

## 8. Charts & diagrams

Three approaches, in order of simplicity:

### 8a. Pre-rendered image (most reliable)
Make a PNG/SVG anywhere (Excel, matplotlib, Excalidraw, Figma) and embed it:
```markdown
![width:600px](sales-chart.png)
```
Best for complex or branded visuals.

### 8b. Mermaid (live diagrams)
Works in Marp setups that enable Mermaid (the VS Code extension does, with the Mermaid plugin):

    ```mermaid
    graph LR
      A[User] --> B[Login]
      B --> C{Valid?}
      C -->|Yes| D[Dashboard]
      C -->|No| E[Error]
    ```

Good for flowcharts, sequence diagrams, gantt charts. Ask Claude: *"Draw a sequence diagram of the auth flow"*.

### 8c. Markdown tables
For tabular data, just use a table — clean and editable.

---

## 9. Exporting

```bash
marp slides.md                 # → slides.html
marp slides.md --pdf           # → slides.pdf
marp slides.md --pptx          # → slides.pptx (editable in PowerPoint)
marp slides.md --images png    # → one PNG per slide
marp slides.md --preview       # live-reloading preview window
```

Watch mode while editing:
```bash
marp -w slides.md
```

---

## 10. Working with Claude — recipes

**Build from scratch**
> "Create `pitch.md` — a 6-slide investor pitch for a SaaS that does X. Use the gaia theme, paginate."

**Convert existing content**
> "Read `notes.md` and turn it into a Marp deck — one slide per H2 section."

**Style pass**
> "Add a dark theme to `slides.md`, make headers blue, and set a consistent footer."

**Fix a single slide**
> "Slide 4 is too crowded — split it into two slides."

**Add a visual**
> "On the architecture slide, add a Mermaid diagram showing API → queue → worker → DB."

**Export**
> "Export `slides.md` to PDF."

---

## 11. Power-up: Claude Code subagents

For bigger decks, ask Claude to **dispatch subagents** (experimental "teams" feature). Each agent runs in its own context and reports back — useful when slide content needs research, or when you want to build sections in parallel.

### Useful agents for slide-building

- **`Explore`** — fast read-only search. Use to mine your repo for content: *"Use Explore to find every README in this monorepo and summarize what each service does."*
- **`general-purpose`** — multi-step research/tasks. Good for: *"Research the top 5 competitors to X and draft a comparison slide."*
- **`Plan`** — architect a deck before writing it: *"Plan a 15-slide deck about our Q4 roadmap — outline only."*

### How to ask

> "Spin up three subagents in parallel: one to draft the intro slides, one to build the technical-architecture slides with a Mermaid diagram, one to draft the closing/Q&A slides. Then merge them into `talk.md`."

> "Use the Explore agent to find all `*.py` files that touch billing, then summarize them into a 3-slide overview."

Claude will dispatch them concurrently and stitch the results into your deck. Faster than doing it serially in one context, and keeps the main conversation clean.

---

## 12. Tips

- **One idea per slide** — if it doesn't fit, split it
- **Turn on `paginate: true`** for any deck over ~5 slides
- **Keep code samples short** — 10 lines max, otherwise screenshot
- **Pre-render complex charts** to PNG/SVG rather than fighting Mermaid config
- **Commit the `.md`**, gitignore generated `.html` / `.pdf` / `.pptx`
- **Use the VS Code preview** while iterating — instant feedback

---

## 13. Reference

- Marp site: https://marp.app/
- Marpit Markdown syntax: https://marpit.marp.app/markdown
- Themes & directives: https://marpit.marp.app/directives
- CLI options: https://github.com/marp-team/marp-cli
