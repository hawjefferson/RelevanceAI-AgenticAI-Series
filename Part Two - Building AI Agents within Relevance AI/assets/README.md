# assets/

The seven figures used in [the article](../README.md), plus their sources.

| File | Figure |
|---|---|
| `01-ai-platform-landscape.png` | Point solutions vs embedded AI vs horizontal platforms |
| `02-four-levels-of-autonomy.png` | The four autonomy levels, and where Relevance AI sits |
| `03-context-before-agents.png` | The four systems this use case needs, and who connects them |
| `04-richard-anatomy.png` | What the agent is made of, read from the live config |
| `05-richard-decision-flow.png` | The SOP as the agent runs it, including both stop branches |
| `06-end-to-end-run.png` | One successful run, step by step, with real values |
| `07-iteration-log.png` | Four runs of iteration, two of them failures |

## PNG vs SVG

The article references the **PNGs** so that what you see on GitHub is identical to what you
upload to LinkedIn (which does not render SVG). Each is 1200px wide at 2× and losslessly
compressed with `optipng`.

The **SVG sources** are in [`svg/`](./svg/) with the scripts that generate them:

```
svg/
├── tokens.py     design tokens - the same file as Part One, so the series reads as one system
├── gen.py        writes all seven SVGs
└── render.py     renders the SVGs to PNG at 2x via headless Chromium
```

To change a figure, edit `gen.py`, then:

```bash
python3 gen.py        # rewrites the SVGs
python3 render.py     # rewrites the PNGs into ../
optipng -o2 ../*.png  # optional, lossless, ~30% smaller
```

`gen.py` also carries a geometry check worth keeping: after generating, nothing should render
past the 56px side margins. Text overrunning its column is the failure mode these figures hit
most often, because line widths are estimated rather than measured.

## Palette

Identical to Part One, derived from the Relevance AI brand — indigo `#5F56FF`, purple `#9646E5`,
navy `#0C162F`. Two constraints carry over:

- **The brand indigo and the brand purple cannot both carry meaning in one figure.** They measure
  ΔE 10.2 against each other for normal vision, below the 15 floor for distinguishable
  categories. Purple stays decorative; every figure uses one categorical hue and carries identity
  through position, numbering and labels.
- **The priority ramp is ordinal** — one hue light→dark (`#949eff` → `#6e6fff` → `#4f45dc`).

Figure 2 uses a dashed border plus a "NOT YET" label for Level 4 rather than colour alone, and
figure 5 keeps its yes/no branch labels in neutral ink — a "no" branch that routes to a valid
alternative path is not an error, and colouring it red would say otherwise.

Figures set an explicit off-white surface (`#FCFCFB`) so they render identically in GitHub's
light and dark themes.

## Conventions for new figures

- Lowercase, hyphenated, number-prefixed filenames: `01-thing-being-shown.png`.
- Keep each file under ~500 KB.
- Every figure needs real alt text in the article — describe what it *shows*, not that it is a diagram.
- Redact API keys, tokens, account emails, channel IDs and customer data before committing.
