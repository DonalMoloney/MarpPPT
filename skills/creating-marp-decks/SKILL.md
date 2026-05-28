---
name: creating-marp-decks
description: Use when the user wants to create, edit, or export a Marp Markdown presentation — drives a brainstorm-first workflow that interviews the user before writing slides, then iterates, styles, and exports to PowerPoint or PDF.
---

# Creating Marp Decks

A deck is only as good as the thinking behind it. Do not start writing slides
until you understand who the deck is for and what it needs to do. This skill
encodes a six-stage workflow: **Brainstorm → Draft → Iterate → Style → Data →
Export**.

## When this applies

- "make a deck / presentation / slides / pptx"
- "help me put together a talk on X"
- "add a slide about X" / "rework slide N"
- "turn this CSV/Excel into a chart slide"
- "export to PowerPoint / PDF"
- The user opens or edits a `*.md` file with `marp: true` in the front matter.

---

## Stage 1 — Brainstorm (do this FIRST, every time)

Before writing a single slide, ask the user. Do not skip this step even if they
hand you a topic. A one-line topic is not a spec.

Ask, in one message, at minimum:

1. **Audience.** Who is in the room? What do they already know?
2. **The one takeaway.** If they remember only one sentence, what is it?
3. **Length.** How many slides, or how many minutes?
4. **Setting.** Live talk, async share, leave-behind PDF, projector vs. laptop?
5. **Material on hand.** Any data files, images, existing notes, or brand?
6. **Tone.** Formal / playful / technical / executive?
7. **Theme or style.** Offer three paths — let the user pick any:
   - **Built-in theme.** Pick one of:
     - `default` — clean, minimal (safe default for most decks)
     - `gaia` — bold, high-contrast (keynote / marketing feel)
     - `uncover` — wide, modern (tech talks, product demos)
   - **Bring your own theme.** A path or URL to a Marp theme CSS file. Wire it
     in by adding `<!-- theme: <name> -->` plus the CSS via `--theme-set` at
     export, or by referencing it from the deck folder.
   - **Describe a style.** Free-form description (e.g. "dark, serif, muted
     orange accents, lots of whitespace"). Translate it into a starting theme
     (closest of the three) plus a `<style>` block at the top of the deck
     overriding fonts, colours, accent, and spacing. Restate the style choices
     back to the user before drafting so they can correct you.
   If the user has no preference, pick a built-in based on tone + setting and
   say which you chose and why.
8. **Speaker notes.** Ask: "Do you want speaker notes for each slide?" If yes,
   add a `<!-- ... -->` notes block to every content slide during drafting and
   export with `--pptx` (never `--pptx-editable`). If no, skip the notes blocks
   entirely — don't add empty ones.

Wait for answers. Then propose a short outline (slide-by-slide titles, one
line each) and get a thumbs-up before drafting. Outlines are cheap; rewriting
ten styled slides is not.

If the user pushes back ("just make it"), ask the single most important
question only — usually audience + takeaway — and proceed.

---

## Stage 2 — Draft

Create the deck file. Default location: a new folder at the repo root named
after the topic, containing `slides.md`. If the user already has a deck folder,
use it.

Every deck starts with this front matter — exactly:

```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
---
```

Rules for the first draft:

- **One idea per slide.** If a slide has two ideas, it is two slides.
- Separate slides with `---` on its own line.
- Title slide first: large title, subtitle, presenter name if given.
- End with a clear closing slide (recap, call to action, or Q&A).
- Speaker notes go in HTML comments inside the slide body: `<!-- ... -->`.
- Keep bullets short — aim for ≤6 bullets, ≤10 words each.

Show the user the draft and explicitly invite edits.

---

## Stage 3 — Iterate

Accept natural-language edit requests and apply them directly to `slides.md`.
Examples and how to handle them:

| Request | Action |
|---|---|
| "Split slide 4 — two ideas" | Cut the slide at the natural seam, add `---`. |
| "Slide 6 is too dense" | Reduce to ≤3 bullets, push detail into speaker notes. |
| "Add a two-column layout" | Use the `.columns` pattern (see Stage 4). |
| "Reorder — move the demo before the results" | Move the slide block, keep titles consistent. |
| "Make slide 2 the title slide" | Move it to the top, apply `<!-- _class: lead -->`. |

Preview while iterating: `npx marp slides.md --preview`

---

## Stage 4 — Style

Only style after the content is settled. Styling broken content wastes effort.

**Theme** — set in front matter:

```yaml
theme: default    # clean, minimal
theme: gaia       # bold, high-contrast
theme: uncover    # wide, modern
```

**Per-slide directives** — HTML comment at the top of the slide:

```markdown
<!-- _class: lead -->                    ← large centred title
<!-- _backgroundColor: #1a1a2e -->       ← dark background
<!-- _color: white -->                   ← white text
<!-- header: "Section > **Current**" --> ← breadcrumb (bold = blue)
<!-- footer: "Your Name · 2026" -->      ← footer line
```

**Two-column layout** — add this `<style>` block once near the top of the deck,
then use `<div class="columns">` anywhere:

```html
<style>
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }
.columns img { width: 100%; }
</style>
```

**Images** — Marp supports sizing directives in the alt text:

```markdown
![width:850px](path/to/image.png)
![bg right:40%](path/to/image.png)   ← right-side background
![bg](path/to/image.png)             ← full-bleed background
```

Image paths are relative to `slides.md`, not the repo root.

---

## Stage 5 — Add Data (only if the user has data)

Pipeline:

```
data/<file>.csv|xlsx ──► make_charts.py ──► figures/<name>.png ──► slide
```

Steps:

1. Drop the data file into a `data/` folder beside `slides.md`.
2. Create or extend `make_charts.py` with a function that reads the file
   (`pd.read_csv` or `pd.read_excel(..., sheet_name=...)`), builds a matplotlib
   figure, and saves it to `figures/<name>.png` at presentation resolution
   (e.g. `dpi=160`, figsize sized for a 16:9 slide).
3. Run `python make_charts.py`. Confirm the PNG appears.
4. Reference it from a slide: `![width:850px](figures/<name>.png)`.
5. Re-preview.

Re-run `make_charts.py` after every data or code change — `npx marp` does NOT
regenerate figures.

---

## Stage 6 — Export

```bash
npx marp slides.md --preview    # live preview (keep open while editing)
npx marp slides.md --pptx       # PowerPoint (preserves presenter notes)
npx marp slides.md --pdf        # PDF
npx marp slides.md --html       # standalone HTML
```

Open the exported file and spot-check before reporting done.

---

## Hard rules

- **Always brainstorm first.** A topic is not a spec.
- Use `--pptx`. NEVER use `--pptx-editable` — it strips presenter notes.
- Image paths in `slides.md` are relative to `slides.md`. If you move the deck,
  fix the paths.
- Always re-run `python make_charts.py` after data changes.
- Speaker notes are HTML comments inside the slide body — not in front matter.
- Do not hand-edit anything in `figures/`. It is generated output.
- One idea per slide. If you are tempted to add a second, add a slide instead.

---

## Verification before claiming done

- The deck previews without Marp warnings (`npx marp slides.md` exits 0).
- The exported `.pptx` / `.pdf` exists and opens.
- Every `![...](...)` path resolves — no broken images in the export.
- If presenter notes were requested, open the `.pptx` and confirm the Notes
  pane is populated.
- The deck answers the brainstorm: audience fit, single takeaway, right length.

---

## Reference files

Trimmed, skill-local copies live in `references/` (load these — they are scoped
to what the skill needs):

- `references/getting-started.md` — six-stage workflow summary + install.
- `references/writing-slides.md` — layout, image, and column patterns.
- `references/charts-from-data.md` — minimal data-to-chart pipeline.
- `references/cheatsheet.md` — syntax and CLI reference.

Full user-facing versions of these docs live at the repo root under `docs/`.
