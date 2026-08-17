"""Design tokens for the Part One diagrams.

Palette is derived from the Relevance AI brand (indigo #5F56FF, purple #9646E5,
navy #0C162F) and validated with the dataviz skill's validate_palette.js:

  ordinal ramp  #949eff,#6e6fff,#4f45dc --ordinal  -> ALL CHECKS PASS
  brand indigo + brand purple as two categorical hues -> FAIL
    (normal-vision dE 10.2, below the 15 floor) => purple is DECORATIVE ONLY,
    never a second meaning-carrying category. One categorical hue: ACCENT.
"""

SURFACE = "#fcfcfb"   # chart surface (explicit, so diagrams read the same in GitHub dark mode)
PANEL   = "#ffffff"
INK     = "#0c162f"   # brand navy, primary ink   17.5:1 on surface
INK2    = "#52514e"   # secondary ink              7.7:1
MUTED   = "#898781"   # axis / meta                3.5:1
GRID    = "#e1e0d9"   # hairline grid
RULE    = "#c3c2b7"   # baseline / axis

ACCENT  = "#5f56ff"   # the single categorical hue  4.9:1
PURPLE  = "#9646e5"   # DECORATIVE ONLY - never carries meaning

# ordinal priority ramp, light -> dark (validated)
Q_LOW   = "#949eff"
Q_MID   = "#6e6fff"
Q_HIGH  = "#4f45dc"
Q_OUT   = "#777a82"   # out of scope, neutral

TINT1   = "#eef2ff"   # panel tints; ink on these is >= 14:1
TINT2   = "#e5ebff"
TINT3   = "#dde4ff"
TINTN   = "#ebedef"

GOOD    = "#0ca30c"   # status - always with icon + label
CRIT    = "#d03b3b"

FONT    = "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"

# ---------------------------------------------------------------- helpers ----

# Inter advance-width factors, calibrated against rendered PNGs (first pass
# under-estimated by ~3-5% and text overran its column, so these run generous).
_CW = {400: 0.545, 500: 0.556, 600: 0.578, 700: 0.596}


def tw(s, size, weight=400):
    """Estimated rendered width of a string."""
    f = _CW.get(weight, 0.52)
    narrow = sum(1 for c in s if c in "iljtfrI.,:;'()[]|! ")
    wide = sum(1 for c in s if c in "MWmw@")
    return (len(s) - narrow - wide) * size * f + narrow * size * f * 0.62 + wide * size * f * 1.32


def wrap(s, size, max_w, weight=400):
    """Greedy word wrap to a pixel width."""
    words, lines, cur = s.split(), [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if cur and tw(cand, size, weight) > max_w:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return lines


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def text(x, y, s, size=15, weight=400, fill=INK, anchor="start", ls="0"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'letter-spacing="{ls}">{esc(s)}</text>')


def para(x, y, s, size=14, weight=400, fill=INK2, max_w=240, lh=1.45, anchor="start"):
    out = []
    for i, line in enumerate(wrap(s, size, max_w, weight)):
        out.append(text(x, y + i * size * lh, line, size, weight, fill, anchor))
    return "\n".join(out)


def para_h(s, size=14, max_w=240, lh=1.45, weight=400):
    """Height a para() call will occupy."""
    return len(wrap(s, size, max_w, weight)) * size * lh


def rect(x, y, w, h, fill=PANEL, stroke=None, rx=10, sw=1, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{rx}" fill="{fill}"{st}{extra}/>')


def line(x1, y1, x2, y2, stroke=GRID, sw=1, dash=None, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')


def arrow(x1, y1, x2, y2, stroke=RULE, sw=2):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" '
            f'marker-end="url(#ah)"/>')


def chip(x, y, label, size=12, fill=INK, bg=TINT1, pad=9, h=24, weight=600, rx=12):
    w = tw(label, size, weight) + pad * 2
    return (rect(x, y, w, h, fill=bg, rx=rx)
            + "\n" + text(x + pad, y + h / 2 + size * 0.36, label, size, weight, fill)), w


def svg_open(w, h, title, desc=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d">
<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>
<defs>
  <marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 9 5 L 0 9 z" fill="{RULE}"/>
  </marker>
  <marker id="ahA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 9 5 L 0 9 z" fill="{ACCENT}"/>
  </marker>
  <linearGradient id="brand" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{ACCENT}"/><stop offset="1" stop-color="{PURPLE}"/>
  </linearGradient>
</defs>
{rect(0, 0, w, h, fill=SURFACE, rx=0)}
'''


def svg_close():
    return "</svg>\n"


def header(w, kicker, title, sub=None, x=56, y=64):
    out = [text(x, y, kicker.upper(), 13, 700, ACCENT, ls="1.4"),
           text(x, y + 34, title, 30, 700, INK)]
    if sub:
        out.append(para(x, y + 66, sub, 16, 400, INK2, max_w=w - x * 2))
    return "\n".join(out)
