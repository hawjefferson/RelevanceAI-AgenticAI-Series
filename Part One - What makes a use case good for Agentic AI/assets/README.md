# assets/

The six figures used in [the article](../README.md), plus their sources.

| File | Figure |
|---|---|
| `01-where-selection-happens.png` | Where use case selection actually happens (the five-stage timeline) |
| `02-value-effort-quadrant.png` | Value vs effort, with eight worked examples plotted |
| `03-five-criteria.png` | The five criteria, the question to ask, and each failure mode |
| `04-scoring-to-quadrant.png` | How the scoring sheet turns weighted inputs into a quadrant |
| `05-scorecard-comparison.png` | A strong use case and a weak one, scored side by side |
| `06-ideation-deck-anatomy.png` | The modular ideation deck: core, swappable middle, appendix |

## PNG vs SVG

The article references the **PNGs** so that what you see on GitHub is identical to what
you upload to LinkedIn (which does not render SVG). Each PNG is 2400px wide — rendered at
2× from a 1200px design, which is the width LinkedIn wants — and losslessly compressed with
`optipng`.

The **SVG sources** are in [`svg/`](./svg/) along with the scripts that generate them:

```
svg/
├── tokens.py     design tokens: palette, type scale, layout helpers
├── gen.py        writes all six SVGs
└── render.py     renders the SVGs to PNG at 2x via headless Chromium
```

To change a figure, edit `gen.py`, then:

```bash
python3 gen.py        # rewrites svg/
python3 render.py     # rewrites the PNGs
optipng -o2 *.png     # optional, ~30% smaller
```

## Palette

Derived from the Relevance AI brand — indigo `#5F56FF`, purple `#9646E5`, navy `#0C162F`.

Two constraints worth knowing before you recolour anything:

- **The brand indigo and the brand purple cannot both carry meaning in one figure.** Measured
  against each other they sit at ΔE 10.2 for normal vision, below the 15 floor for
  distinguishable categories — so readers with full colour vision struggle to tell them apart,
  never mind readers with a colour vision deficiency. The purple is therefore decorative only.
  Every figure uses a **single** categorical hue, and carries identity with numbers, position
  and labels instead.
- **The quadrant priority ramp is ordinal**, one hue light→dark (`#949eff` → `#6e6fff` →
  `#4f45dc`), validated for monotone lightness, adequate step gaps and contrast against the
  surface.

Figures set an explicit off-white surface (`#FCFCFB`) rather than a transparent background, so
they render identically in GitHub's light and dark themes.

## Conventions for new figures

- Lowercase, hyphenated, number-prefixed filenames: `01-thing-being-shown.png`.
- Keep each file under ~500 KB.
- Every figure needs real alt text in the article — describe what the figure *shows*, not that
  it is a diagram.
- Redact API keys, tokens, account emails and customer data before committing screenshots.
