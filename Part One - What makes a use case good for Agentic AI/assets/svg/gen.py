#!/usr/bin/env python3
"""Generate the Part One diagrams as SVG."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tokens import *  # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)


def write(name, body):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"  {name}  ({len(body)/1024:.1f} KB)")


# ══════════════════════════════════════════════════ 1. where selection happens
def d1():
    W, H = 1200, 600
    s = [svg_open(W, H, "Where agentic use case selection actually happens",
                  "A five-stage timeline from presales to build. Presales produces a direction; "
                  "ideation and pressure-testing after kickoff produce the committed use cases.")]
    s.append(header(W, "Part One - figure 1",
                    "Where use case selection actually happens",
                    "Presales gives you a direction. The decision gets made after kickoff, "
                    "with the champion and the executive buyer in the room."))

    stages = [
        ("01", "Presales", "Candidate use cases surfaced while the deal is being won.",
         "AE + solutions engineer", "A direction", False),
        ("02", "Kickoff", "Champion and executive buyer aligned on what success means.",
         "Champion + exec buyer", "Shared definition of done", False),
        ("03", "Ideation", "Widen the list before you narrow it. Score every candidate.",
         "Champion + team leads", "A scored long list", True),
        ("04", "Pressure-test", "Challenge feasibility and value. Kill what does not hold up.",
         "Exec buyer + delivery", "1-2 committed use cases", True),
        ("05", "Build", "Implementation planning against a locked scope.",
         "Delivery + technical owner", "A plan with dates", False),
    ]

    x0, cw, gap = 56, 190, 34.5
    top, ch = 232, 196

    # phase bands
    s.append(text(x0, 200, "PRESALES", 11, 700, MUTED, ls="1.3"))
    s.append(line(x0, 208, x0 + cw, 208, GRID, 2))
    bx = x0 + cw + gap
    s.append(text(bx, 200, "IMPLEMENTATION", 11, 700, MUTED, ls="1.3"))
    s.append(line(bx, 208, x0 + 5 * cw + 4 * gap, 208, GRID, 2))

    for i, (num, title, body, owner, out, hot) in enumerate(stages):
        x = x0 + i * (cw + gap)
        fill = TINT3 if hot else PANEL
        stroke = None if hot else GRID
        s.append(rect(x, top, cw, ch, fill=fill, stroke=stroke, rx=12))
        s.append(rect(x, top, 4, ch, fill=(Q_HIGH if hot else RULE), rx=2))
        s.append(text(x + 18, top + 34, num, 13, 700, (Q_HIGH if hot else MUTED), ls="1"))
        s.append(text(x + 18, top + 62, title, 19, 700, INK))
        s.append(para(x + 18, top + 88, body, 13, 400, INK2, max_w=cw - 36, lh=1.42))
        s.append(line(x + 18, top + ch - 62, x + cw - 18, top + ch - 62, GRID, 1))
        s.append(text(x + 18, top + ch - 42, "WHO", 9.5, 700, MUTED, ls="1.1"))
        s.append(para(x + 18, top + ch - 27, owner, 11.5, 500, INK2, max_w=cw - 36, lh=1.3))
        s.append(text(x + 18, top + ch + 26, "OUTPUT", 9.5, 700, MUTED, ls="1.1"))
        s.append(para(x + 18, top + ch + 42, out, 12.5, 600, INK, max_w=cw - 30, lh=1.32))
        if i < 4:
            ax = x + cw + 6
            s.append(arrow(ax, top + ch / 2, ax + gap - 12, top + ch / 2,
                           ACCENT if i in (1, 2) else RULE, 2))
            if i in (1, 2):
                s.append(f'<line x1="{ax:.1f}" y1="{top+ch/2:.1f}" x2="{ax+gap-12:.1f}" '
                         f'y2="{top+ch/2:.1f}" stroke="{ACCENT}" stroke-width="2" '
                         f'stroke-linecap="round" marker-end="url(#ahA)"/>')

    y = top + ch + 78
    s.append(rect(x0, y, W - 2 * x0, 52, fill=TINT1, rx=10))
    s.append(rect(x0, y, 4, 52, fill=ACCENT, rx=2))
    s.append(text(x0 + 20, y + 32, "Stages 03 and 04 are the ones teams skip. Skipping them is how a "
                                   "presales slide becomes a six-month build nobody sponsors.",
                  14.5, 500, INK))
    s.append(svg_close())
    write("01-where-selection-happens.svg", "\n".join(s))


# ═════════════════════════════════════════════════════ 2. value/effort quadrant
def d2():
    W, H = 1200, 1070
    L, R, T, B = 186, 1144, 214, 726
    MX, MY = (L + R) / 2, (T + B) / 2
    s = [svg_open(W, H, "The value versus effort quadrant",
                  "A quadrant with business value rising up the y-axis and ease of delivery rising "
                  "to the right, so the top-right quadrant is high value and low effort. Eight "
                  "numbered example use cases are plotted and keyed below the chart.")]
    s.append(header(W, "Part One - figure 2", "Value vs effort: pick the top-right",
                    "Note the x-axis: it runs from harder to easier, left to right. That puts "
                    "high value and low effort together in the top-right corner."))

    quads = [
        (L, T, MX - L, MY - T, TINT2, Q_MID, "SEQUENCE LATER",
         "High value, high effort", "Worth doing. Not first - it will outrun your sponsorship."),
        (MX, T, R - MX, MY - T, TINT3, Q_HIGH, "BUILD FIRST",
         "High value, low effort", "One or two of these. This is the whole game."),
        (L, MY, MX - L, B - MY, TINTN, Q_OUT, "DECLINE",
         "Low value, high effort", "Say no out loud, early, and in front of the exec buyer."),
        (MX, MY, R - MX, B - MY, TINT1, Q_LOW, "FILL CAPACITY",
         "Low value, low effort", "Fine once the team has slack. Never the flagship."),
    ]
    for qx, qy, qw, qh, fill, accent, name, meaning, verdict in quads:
        s.append(rect(qx + 3, qy + 3, qw - 6, qh - 6, fill=fill, rx=12))

    # the target quadrant gets a visible ring, not colour alone
    s.append(f'<rect x="{MX+3:.1f}" y="{T+3:.1f}" width="{R-MX-6:.1f}" height="{MY-T-6:.1f}" '
             f'rx="12" fill="none" stroke="{Q_HIGH}" stroke-width="2.5"/>')

    for qx, qy, qw, qh, fill, accent, name, meaning, verdict in quads:
        tx = qx + 26
        ty = qy + 42
        s.append(text(tx, ty, name, 12.5, 700, accent, ls="1.5"))
        s.append(text(tx, ty + 27, meaning, 17, 700, INK))
        s.append(para(tx, ty + 52, verdict, 13.5, 400, INK2, max_w=qw - 52, lh=1.42))

    # axes
    s.append(line(L, MY, R, MY, RULE, 1.5))
    s.append(line(MX, T, MX, B, RULE, 1.5))
    s.append(f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="{RULE}" stroke-width="2"/>')
    s.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{B}" stroke="{RULE}" stroke-width="2"/>')

    s.append(text((L + R) / 2, B + 44, "EASE OF DELIVERY  \u2192", 12, 700, MUTED,
                  anchor="middle", ls="1.6"))
    s.append(text(L, B + 44, "harder", 12.5, 500, MUTED))
    s.append(text(R, B + 44, "easier", 12.5, 500, MUTED, anchor="end"))
    s.append(f'<g transform="translate({L-46},{(T+B)/2}) rotate(-90)">'
             + text(0, 0, "BUSINESS VALUE", 12, 700, MUTED, anchor="middle", ls="1.6") + '</g>')
    s.append(f'<g transform="translate({L-46},{T+34}) rotate(-90)">'
             + text(0, 0, "higher", 12.5, 500, MUTED, anchor="start") + '</g>')
    s.append(f'<g transform="translate({L-46},{B-34}) rotate(-90)">'
             + text(0, 0, "lower", 12.5, 500, MUTED, anchor="end") + '</g>')

    # numbered examples - identity is the number, not the colour
    pts = [
        (1, 0.80, 0.74, "Inbound lead qualification and routing"),
        (2, 0.91, 0.62, "Support ticket triage, tagging and routing"),
        (3, 0.66, 0.56, "First-draft RFP and security questionnaire answers"),
        (4, 0.30, 0.75, "End-to-end contract negotiation"),
        (5, 0.14, 0.58, "Autonomous month-end financial close"),
        (6, 0.86, 0.24, "Tidying up meeting notes"),
        (7, 0.68, 0.12, "Reformatting the weekly report"),
        (8, 0.20, 0.20, "Ad-hoc analysis nobody has written down"),
    ]
    for n, fx, fy, _lbl in pts:
        cx = L + fx * (R - L)
        cy = B - fy * (B - T)
        s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="16" fill="{ACCENT}" '
                 f'stroke="{SURFACE}" stroke-width="2.5"/>')
        s.append(text(cx, cy + 5, str(n), 14, 700, "#ffffff", anchor="middle"))

    # key
    ky = B + 96
    s.append(text(56, ky, "THE EIGHT EXAMPLES", 11.5, 700, MUTED, ls="1.4"))
    s.append(line(56, ky + 14, W - 56, ky + 14, GRID, 1))
    verdicts = {1: "Build first", 2: "Build first", 3: "Build first", 4: "Sequence later",
                5: "Sequence later", 6: "Fill capacity", 7: "Fill capacity", 8: "Decline"}
    vcol = {"Build first": Q_HIGH, "Sequence later": Q_MID,
            "Fill capacity": Q_LOW, "Decline": Q_OUT}
    for i, (n, _fx, _fy, lbl) in enumerate(pts):
        col = i % 2
        row = i // 2
        x = 56 + col * 566
        y = ky + 48 + row * 46
        s.append(f'<circle cx="{x+13:.1f}" cy="{y-5:.1f}" r="13" fill="{ACCENT}"/>')
        s.append(text(x + 13, y, str(n), 12, 700, "#ffffff", anchor="middle"))
        s.append(text(x + 38, y, lbl, 14.5, 500, INK))
        v = verdicts[n]
        s.append(text(x + 38, y + 19, v.upper(), 10.5, 700, vcol[v], ls="1.2"))
    s.append(svg_close())
    write("02-value-effort-quadrant.svg", "\n".join(s))


# ═══════════════════════════════════════════════════════════ 3. five criteria
def d3():
    W = 1200
    rows = [
        ("01", "High volume",
         "How many times a week does this happen, and who counts it?",
         "Low volume means the payback never arrives. A perfect agent run 40 times a "
         "year is a demo, not a business case."),
        ("02", "A documented process",
         "Can you show me the SOP, the checklist, or the recording?",
         "If the process only lives in someone's head, you are not automating a "
         "process - you are inventing one, on a deadline."),
        ("03", "Owners already in place",
         "Who owns this in the business, and who owns the systems it touches?",
         "No business owner means no one to accept the output. No technical owner "
         "means access requests stall for weeks."),
        ("04", "System and knowledge context",
         "What must the agent read to be right, and can we reach it?",
         "An agent with no grounding guesses confidently. That is worse than no "
         "agent, because people believe it."),
        ("05", "Measurable business impact",
         "What number moves, by how much, and who already reports it?",
         "If impact cannot be measured with a metric that already exists, renewal "
         "becomes an argument about vibes."),
    ]
    hdr_h, row_h = 232, 92
    H = hdr_h + row_h * len(rows) + 130
    s = [svg_open(W, H, "The five criteria for a high-probability agentic use case",
                  "Five criteria in a table: high volume, a documented process, owners already in "
                  "place, system and knowledge context, and measurable business impact. Each row "
                  "gives the question to ask and the failure mode when the criterion is missing.")]
    s.append(header(W, "Part One - figure 3", "The five criteria - all of them, not most of them",
                    "These are pass/fail gates, not a weighted average. A use case that misses one "
                    "is not 80% ready; it has a specific hole you can go and fill."))

    cx1, cx2, cx3 = 132, 400, 770
    s.append(text(cx1, hdr_h - 16, "CRITERION", 10.5, 700, MUTED, ls="1.3"))
    s.append(text(cx2, hdr_h - 16, "THE QUESTION TO ASK", 10.5, 700, MUTED, ls="1.3"))
    s.append(text(cx3, hdr_h - 16, "WHAT HAPPENS WHEN IT IS MISSING", 10.5, 700, MUTED, ls="1.3"))
    s.append(line(56, hdr_h - 4, W - 56, hdr_h - 4, RULE, 1.5))

    for i, (num, title, q, fail) in enumerate(rows):
        y = hdr_h + i * row_h
        if i % 2 == 0:
            s.append(rect(56, y, W - 112, row_h, fill=TINT1, rx=8))
        s.append(f'<circle cx="90" cy="{y + 40:.1f}" r="19" fill="{ACCENT}"/>')
        s.append(text(90, y + 45.5, num, 14.5, 700, "#ffffff", anchor="middle"))
        s.append(para(cx1, y + 34, title, 17, 700, INK, max_w=250, lh=1.28))
        s.append(para(cx2, y + 32, q, 13.5, 500, INK, max_w=306, lh=1.44))
        s.append(para(cx3, y + 32, fail, 13.5, 400, INK2, max_w=352, lh=1.44))
        if i < len(rows) - 1:
            s.append(line(56, y + row_h, W - 56, y + row_h, GRID, 1))

    y = hdr_h + row_h * len(rows) + 34
    s.append(rect(56, y, W - 112, 60, fill=TINT3, rx=10))
    s.append(rect(56, y, 4, 60, fill=Q_HIGH, rx=2))
    s.append(text(76, y + 26, "Five for five is the bar.", 15, 700, INK))
    s.append(text(76, y + 46, "Four out of five is not a green light - it is a named piece of "
                              "work to do before the build starts.", 14, 400, INK2))
    s.append(svg_close())
    write("03-five-criteria.svg", "\n".join(s))


# ══════════════════════════════════════════════════════ 4. scoring -> quadrant
def d4():
    W, H = 1200, 830
    s = [svg_open(W, H, "How the scoring sheet turns criteria into a quadrant",
                  "Value inputs and effort inputs are scored one to five, weighted and summed, then "
                  "a single rule places each use case in one of the four quadrants automatically.")]
    s.append(header(W, "Part One - figure 4", "How the sheet turns judgement into a quadrant",
                    "Score each input 1-5. The sheet weights them, sums them and places the use "
                    "case for you, so the argument is about scores, not about placement."))

    cw = 512
    lx, rx_ = 56, W - 56 - cw
    top, ch = 214, 268

    def card(x, kicker, title, items, accent):
        o = [rect(x, top, cw, ch, fill=PANEL, stroke=GRID, rx=12),
             rect(x, top, cw, 4, fill=accent, rx=2),
             text(x + 24, top + 38, kicker, 11.5, 700, accent, ls="1.4"),
             text(x + 24, top + 66, title, 20, 700, INK)]
        for j, (label, weight) in enumerate(items):
            yy = top + 104 + j * 40
            o.append(text(x + 24, yy, label, 14.5, 500, INK))
            o.append(rect(x + cw - 24 - 54, yy - 15, 54, 22, fill=TINT1, rx=6))
            o.append(text(x + cw - 24 - 27, yy, weight, 12.5, 700, accent, anchor="middle"))
            if j < len(items) - 1:
                o.append(line(x + 24, yy + 16, x + cw - 24, yy + 16, GRID, 1))
        return "\n".join(o)

    s.append(card(lx, "INPUTS TO VALUE", "Value score", [
        ("Annual hours or cost released", "x 3"),
        ("Volume of the process", "x 2"),
        ("Strategic pull from the exec buyer", "x 2"),
        ("Quality or risk upside", "x 1"),
    ], Q_HIGH))
    s.append(card(rx_, "INPUTS TO EFFORT", "Effort score", [
        ("Process documentation maturity", "x 3"),
        ("System access and integration count", "x 3"),
        ("Knowledge and data readiness", "x 2"),
        ("Owner availability", "x 1"),
    ], Q_MID))

    # converge
    my = top + ch
    s.append(arrow(lx + cw / 2, my + 12, W / 2 - 30, my + 62, RULE, 2))
    s.append(arrow(rx_ + cw / 2, my + 12, W / 2 + 30, my + 62, RULE, 2))

    by, bh = my + 78, 116
    s.append(rect(200, by, W - 400, bh, fill=TINT3, rx=12))
    s.append(rect(200, by, 4, bh, fill=Q_HIGH, rx=2))
    s.append(text(224, by + 32, "THE ONE RULE THE SHEET APPLIES", 11.5, 700, Q_HIGH, ls="1.4"))
    s.append(text(224, by + 62, "Value >= midpoint  AND  Effort <= midpoint", 19, 700, INK))
    s.append(text(224, by + 92, "Everything else falls out of the same comparison. "
                                "No one places their own use case by hand.", 13.5, 400, INK2))

    # outputs
    oy = by + bh + 54
    s.append(text(56, oy - 18, "WHERE IT LANDS", 11.5, 700, MUTED, ls="1.4"))
    outs = [("Build first", "high value, low effort", Q_HIGH, TINT3),
            ("Sequence later", "high value, high effort", Q_MID, TINT2),
            ("Fill capacity", "low value, low effort", Q_LOW, TINT1),
            ("Decline", "low value, high effort", Q_OUT, TINTN)]
    ow, ogap = 254, 18
    for i, (name, sub, accent, fill) in enumerate(outs):
        x = 56 + i * (ow + ogap)
        s.append(rect(x, oy, ow, 76, fill=fill, rx=10))
        s.append(rect(x, oy, 4, 76, fill=accent, rx=2))
        s.append(text(x + 18, oy + 32, name, 16.5, 700, INK))
        s.append(text(x + 18, oy + 55, sub, 12.5, 400, INK2))
    s.append(svg_close())
    write("04-scoring-to-quadrant.svg", "\n".join(s))


# ═══════════════════════════════════════════════════════ 5. scorecard compare
def d5():
    W, H = 1200, 840
    s = [svg_open(W, H, "A strong use case and a weak one, scored against the same five criteria",
                  "Two scorecards side by side. Inbound lead qualification passes all five criteria "
                  "and is a build-first candidate. Make our strategy process AI-powered fails four "
                  "of five and should be declined.")]
    s.append(header(W, "Part One - figure 5", "The same five criteria, two very different answers",
                    "Both of these were real asks in the same kickoff. The criteria are what "
                    "separated them - in twenty minutes, not two months."))

    crit = ["High volume", "Documented process", "Owners in place",
            "System / knowledge context", "Measurable impact"]
    good_case = [
        ("PASS", "1,800 inbound leads a month, already reported"),
        ("PASS", "Routing rules written down in the sales playbook"),
        ("PASS", "Sales ops owns it; RevOps owns the CRM"),
        ("PASS", "CRM, enrichment tool and ICP definition all reachable"),
        ("PASS", "Speed to first touch, already on the exec dashboard"),
    ]
    weak_case = [
        ("FAIL", "A handful of cycles a year"),
        ("FAIL", "No two leaders describe it the same way"),
        ("PASS", "The exec buyer is personally interested"),
        ("FAIL", "The context is in people's heads and old decks"),
        ("FAIL", "No metric anyone currently reports"),
    ]

    cw = 528
    top = 216
    CARD_H = 404
    for side, (title, sub, rowsx, verdict, vcol, vfill, score) in enumerate([
        ("Inbound lead qualification", "Requested by the sales ops lead", good_case,
         "BUILD FIRST", Q_HIGH, TINT3, "5 of 5"),
        ("Make our strategy process AI-powered", "Requested at the end of the kickoff",
         weak_case, "DECLINE - FOR NOW", Q_OUT, TINTN, "1 of 5"),
    ]):
        x = 56 + side * (cw + 32)
        s.append(rect(x, top, cw, CARD_H, fill=PANEL, stroke=GRID, rx=12))
        s.append(rect(x, top, cw, 4, fill=vcol, rx=2))
        s.append(para(x + 24, top + 44, title, 20, 700, INK, max_w=cw - 48, lh=1.25))
        s.append(text(x + 24, top + 70, sub, 13, 400, MUTED))
        s.append(line(x + 24, top + 88, x + cw - 24, top + 88, GRID, 1))
        for j, (verd, note) in enumerate(rowsx):
            yy = top + 118 + j * 62
            ok = verd == "PASS"
            col = GOOD if ok else CRIT
            # icon + label, never colour alone
            s.append(f'<circle cx="{x+38}" cy="{yy-4:.1f}" r="11" fill="none" '
                     f'stroke="{col}" stroke-width="2"/>')
            if ok:
                s.append(f'<path d="M {x+32} {yy-4} l 4.2 4.4 l 8-9" fill="none" '
                         f'stroke="{col}" stroke-width="2.2" stroke-linecap="round" '
                         f'stroke-linejoin="round"/>')
            else:
                s.append(f'<path d="M {x+33.5} {yy-9.5} l 9 11 M {x+42.5} {yy-9.5} l -9 11" '
                         f'fill="none" stroke="{col}" stroke-width="2.2" stroke-linecap="round"/>')
            s.append(text(x + 60, yy, crit[j], 14.5, 600, INK))
            s.append(text(x + 60, yy + 19, note, 12.5, 400, INK2))
            s.append(text(x + cw - 24, yy, verd, 10.5, 700, col, anchor="end", ls="1.2"))
        vy = top + CARD_H + 20
        s.append(rect(x, vy, cw, 62, fill=vfill, rx=10))
        s.append(rect(x, vy, 4, 62, fill=vcol, rx=2))
        s.append(text(x + 20, vy + 26, verdict, 15.5, 700, INK))
        s.append(text(x + 20, vy + 48, f"{score} criteria met", 13, 400, INK2))

    y = top + CARD_H + 20 + 62 + 42
    s.append(text(56, y + 4, "\"Decline - for now\" is not a no. It is a list of the four things that "
                             "have to be true before it earns a slot.", 14.5, 500, INK2))
    s.append(svg_close())
    write("05-scorecard-comparison.svg", "\n".join(s))


# ══════════════════════════════════════════════════════════ 6. deck anatomy
def d6():
    W, H = 1200, 760
    s = [svg_open(W, H, "Anatomy of a modular use case ideation deck",
                  "A deck split into a fixed core, an audience-swappable middle, and an appendix "
                  "of rarer team-specific use cases, with audience variants listed underneath.")]
    s.append(header(W, "Part One - figure 6", "The ideation deck is modular on purpose",
                    "One deck, three layers: a core that never changes, a middle swapped for the "
                    "audience in the room, and a long tail that lives in an appendix."))

    layers = [
        ("ALWAYS IN", "The core", Q_HIGH, TINT3,
         ["The agent menu - what agents can actually do",
          "How we score and prioritise use cases",
          "Two ROI spotlights with real numbers"],
         "Sets the frame. Cutting any of this is why ideation sessions drift."),
        ("SWAP FOR THE ROOM", "Worked examples by team", Q_MID, TINT1,
         ["Sales pack", "Marketing pack", "Customer success pack", "Operations pack",
          "Finance pack"],
         "Bring one pack. Leaving the sales examples in front of a marketing audience "
         "is the fastest way to lose the room."),
        ("ON REQUEST", "Appendix: the long tail", Q_OUT, PANEL,
         ["Rarer team-specific use cases",
          "Edge cases people ask about",
          "Things we have seen fail, and why"],
         "Never presented linearly. It exists so you can answer \"what about us?\" "
         "with a slide instead of a promise."),
    ]

    top = 212
    cw, gap = 358, 27
    ch = 340
    for i, (kicker, title, accent, fill, bullets, note) in enumerate(layers):
        x = 56 + i * (cw + gap)
        s.append(rect(x, top, cw, ch, fill=fill,
                      stroke=(GRID if fill == PANEL else None), rx=12))
        if i == 0:
            s.append(f'<rect x="{x}" y="{top}" width="{cw}" height="{ch}" rx="12" '
                     f'fill="none" stroke="{Q_HIGH}" stroke-width="2.5"/>')
        s.append(rect(x, top, 4, ch, fill=accent, rx=2))
        s.append(text(x + 22, top + 36, kicker, 11, 700, accent, ls="1.4"))
        s.append(text(x + 22, top + 64, title, 19, 700, INK))
        yy = top + 96
        for b in bullets:
            s.append(f'<circle cx="{x+28}" cy="{yy-4:.1f}" r="3" fill="{accent}"/>')
            lines = wrap(b, 13.5, cw - 74)
            for k, ln in enumerate(lines):
                s.append(text(x + 42, yy + k * 19, ln, 13.5, 500, INK))
            yy += max(1, len(lines)) * 19 + 9
        s.append(line(x + 22, top + ch - 84, x + cw - 22, top + ch - 84, RULE, 1))
        s.append(para(x + 22, top + ch - 62, note, 12.5, 400, INK2, max_w=cw - 44, lh=1.4))

    y = top + ch + 52
    s.append(text(56, y, "TAILOR BEFORE YOU SEND, NOT DURING THE CALL", 11.5, 700, MUTED, ls="1.4"))
    s.append(line(56, y + 14, W - 56, y + 14, GRID, 1))
    steps = ["Ask who is in the room", "Delete the packs that do not apply",
             "Reorder so their team is slide three", "Move the rest to the appendix"]
    xx = 56
    for i, st in enumerate(steps):
        c, w = chip(xx, y + 34, f"{i+1}.  {st}", size=13, bg=PANEL, fill=INK)
        s.append(f'<rect x="{xx}" y="{y+34}" width="{w:.1f}" height="24" rx="12" '
                 f'fill="none" stroke="{GRID}" stroke-width="1"/>')
        s.append(c)
        xx += w + 12
        if i < len(steps) - 1:
            s.append(text(xx - 6, y + 51, "→", 13, 400, MUTED))
            xx += 14

    y2 = y + 92
    s.append(rect(56, y2, W - 112, 52, fill=TINT1, rx=10))
    s.append(rect(56, y2, 4, 52, fill=ACCENT, rx=2))
    s.append(text(76, y2 + 32, "The same deck works earlier in the cycle. Nothing in the core "
                               "assumes a signed contract.", 14.5, 500, INK))
    s.append(svg_close())
    write("06-ideation-deck-anatomy.svg", "\n".join(s))


if __name__ == "__main__":
    print("Generating SVG diagrams:")
    for fn in (d1, d2, d3, d4, d5, d6):
        fn()
    print("Done.")
