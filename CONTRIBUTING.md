# Contributing / Conventions

This repo is a **series**, so consistency between parts matters more than it would in a normal project. A reader should be able to land on any part and know immediately where the article, the images and the importable artifacts are.

---

## Adding a new part

1. Copy the [`_template/`](./_template/) folder.
2. Rename it: `Part <Number> - <Readable Title>`
   - Number spelled out in words, matching the existing style: `Part One`, `Part Two`, `Part Three`.
   - Separator is a space-hyphen-space: ` - `.
   - Title in sentence case: `Part Two - From use case to agent brief`.
3. Fill in `README.md` — that filename matters, because GitHub renders it automatically when someone opens the folder.
4. Delete the `<placeholder>` markers and the HTML guidance comments.
5. Add a row to the series table in the [root README](./README.md), and move the previous part's status from 🚧 to ✅.
6. Update the previous part's **Next up** section to link to yours.

---

## Folder shape

```
Part <Number> - <Readable Title>/
├── README.md      ← the article
├── linkedin.md    ← the same article, reshaped for the LinkedIn article editor
├── assets/        ← figures, diagrams, screenshots (PNG + SVG sources)
└── build/         ← exported Relevance AI tools, agents, workforces, companion assets
```

Keep `assets/README.md` and `build/README.md` in place — they document the local conventions for anyone browsing the folder.

---

## Every part is dual-purpose

Each article is written to work in two places: as the folder's `README.md` on GitHub, and as a
LinkedIn article. That shapes a few choices.

- **Keep Markdown tables out of the article body.** LinkedIn's editor cannot render them. Use
  bold-led bullets instead, and put genuinely tabular material in a figure.
- **Reference PNGs, not SVGs, from the article.** LinkedIn does not render SVG, so referencing
  the PNG means what a reader sees on GitHub is exactly what gets uploaded to LinkedIn.
- **`linkedin.md` carries the LinkedIn cut**: `[IMAGE n]` markers with the alt text to paste in,
  a punchier opening, no repo-specific sections, and publishing notes (title options, hashtags,
  cover image) at the bottom to be deleted before posting.

## Assets

- Lowercase, hyphenated filenames; number prefix when order matters (`01-create-tool.png`).
- Screenshots as PNG. Diagrams authored as SVG and committed **with their PNG export** — keep
  the generator script beside the SVG so a figure can be edited rather than redrawn.
- Give figures an explicit background colour. A transparent PNG with dark text disappears in
  GitHub's dark theme.
- Every figure needs real alt text in the article: describe what it *shows*, not that it is a
  diagram.
- Crop to the relevant UI. Keep files under ~500 KB (`optipng -o2` is lossless and usually
  saves ~30%).
- **Redact** API keys, tokens, account emails and customer data before committing.

---

## Build exports

- **No secrets.** Strip API keys, tokens, OAuth account IDs and webhook URLs. Use `<YOUR_API_KEY>` placeholders and list what the reader must supply under the article's prerequisites.
- **No real customer data.** Synthetic or fully anonymised only.
- Name files by kind: `tool-<slug>.json`, `agent-<slug>.json`, `workforce-<slug>.json`, `data-<slug>.csv`.
- If an export only imports cleanly in a particular Relevance AI region or plan tier, say so in the article.

---

## Writing style

- **Lead with the reader's problem**, not with the product. The Relevance AI specifics come after the concept is clear.
- **Be concrete.** Real numbers, real failure modes, real screenshots beat abstractions.
- **Keep the "What to watch out for" section honest.** It is the highest-value part of any hands-on article — write down what actually broke.
- Second person ("you"), active voice, short paragraphs.
- Define a term the first time it appears; assume nothing about prior agent experience in early parts.

---

## Git conventions

- Work on a branch: `part/<number>-<slug>` for new parts, `chore/<slug>` or `fix/<slug>` for everything else.
- One part per pull request where practical.
- Commit messages in the imperative: `Add Part Two walkthrough`, not `Added...`.
- `.DS_Store` and friends are covered by [`.gitignore`](./.gitignore) — don't commit editor or OS cruft.

---

## Before you open a PR

- [ ] Every `<placeholder>` filled in and guidance comments deleted
- [ ] No Markdown tables in the article body (LinkedIn cannot render them)
- [ ] Every figure has alt text, and the article references the PNG not the SVG
- [ ] All relative links resolve (part links from the root README, asset links inside the article)
- [ ] No secrets or customer data in `assets/` or `build/`
- [ ] Root README series table updated
- [ ] Previous part's **Next up** links to this one
