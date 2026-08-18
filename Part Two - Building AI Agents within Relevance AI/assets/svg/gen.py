#!/usr/bin/env python3
"""Generate the Part Two diagrams as SVG.

Design tokens are shared with Part One (tokens.py is the same file), so the
series reads as one system. Extra primitives specific to these figures -
column cards, table rows, flow nodes, decision diamonds - live here.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tokens import *  # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUT, exist_ok=True)
KICK = "Part Two"


def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)
    print(f"  {name}  ({len(body)/1024:.1f} KB)")


# ── extra primitives ─────────────────────────────────────────────────────────
def callout_lines(text_, w, size=14.5):
    return wrap(text_, size, w - 44, 500)


def callout_h(text_, w, size=14.5):
    """Height a wrapping callout needs. Never smaller than a single-line box."""
    return max(52, len(callout_lines(text_, w, size)) * size * 1.5 + 30)


def callout(x, y, w, text_, accent=ACCENT, fill=TINT1, h=None, size=14.5):
    lines = callout_lines(text_, w, size)
    h = h or callout_h(text_, w, size)
    o = [rect(x, y, w, h, fill=fill, rx=10), rect(x, y, 4, h, fill=accent, rx=2)]
    y0 = y + (h - (len(lines) - 1) * size * 1.5) / 2 + size * 0.36
    for i, ln in enumerate(lines):
        o.append(text(x + 20, y0 + i * size * 1.5, ln, size, 500, INK))
    return "\n".join(o)


def status_icon(x, y, ok, r=11):
    col = GOOD if ok else CRIT
    o = [f'<circle cx="{x}" cy="{y:.1f}" r="{r}" fill="none" stroke="{col}" stroke-width="2"/>']
    if ok:
        o.append(f'<path d="M {x-6} {y} l 4.2 4.4 l 8-9" fill="none" stroke="{col}" '
                 f'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    else:
        o.append(f'<path d="M {x-4.5} {y-5.5} l 9 11 M {x+4.5} {y-5.5} l -9 11" fill="none" '
                 f'stroke="{col}" stroke-width="2.2" stroke-linecap="round"/>')
    return "\n".join(o), col


def pill(x, y, label, size=11.5, fg=INK, bg=PANEL, stroke=GRID, h=23, weight=600):
    w = tw(label, size, weight) + 20
    return ("\n".join([rect(x, y, w, h, fill=bg, stroke=stroke, rx=11.5),
                       text(x + 10, y + h / 2 + size * 0.36, label, size, weight, fg)]), w)


def pill_row(x, y, labels, size=11.5, fg=INK, bg=PANEL, gap=7, max_x=None):
    """Wrapping row of pills. Returns (svg, height)."""
    out, cx, cy, rows = [], x, y, 1
    for lb in labels:
        w = tw(lb, size, 600) + 20
        if max_x and cx + w > max_x and cx > x:
            cx, cy, rows = x, cy + 30, rows + 1
        s, w = pill(cx, cy, lb, size, fg, bg)
        out.append(s)
        cx += w + gap
    return "\n".join(out), rows * 30


# ══════════════════════════════════════════════════════ 1. platform landscape
def d1():
    W = 1200
    cols = [
        ("POINT SOLUTIONS", "One task, one industry", Q_LOW, TINT1,
         "Software that solves a single, specific problem very deeply for one vertical.",
         ["Heidi Health - clinical documentation"],
         "Fastest time to value when your use case is exactly the one it was built for. "
         "Nothing horizontal will match its depth on that job.",
         "The second use case. You buy another tool. Then another."),
        ("EMBEDDED AI", "Inside the tools you already own", Q_MID, TINT2,
         "AI features shipped as part of a product already in your stack.",
         ["Notion agents", "CRM copilots", "Helpdesk suggest-reply"],
         "No procurement, no onboarding, and the context is already sitting in the product.",
         "It can only see its own product. Anything that crosses systems is out of scope."),
        ("HORIZONTAL PLATFORMS", "Any use case, any business unit", Q_HIGH, TINT3,
         "A platform you build on rather than a feature you switch on.",
         ["Relevance AI", "Wonderful", "Anthropic", "OpenAI"],
         "One platform, many use cases, many departments. Work that crosses four systems is "
         "the normal case, not the exception.",
         "It will not out-depth a vertical tool on that tool's one job. And it asks you to build."),
    ]
    cw, gap = 344, 28
    top, ch = 214, 400
    H = top + ch + 156
    s = [svg_open(W, H, "Three shapes of AI in the market",
                  "Point solutions, embedded AI and horizontal platforms compared on what they "
                  "are, examples, where each wins and where each runs out.")]
    s.append(header(W, f"{KICK} - figure 1", "The market sells AI with one paintbrush",
                    "There are three different shapes on offer, and they fail in different "
                    "places. Knowing which is which is most of the platform decision."))
    # emphasis rises left to right: the article proceeds with the third column
    styles = [(PANEL, GRID, False), (TINT1, None, False), (TINT3, None, True)]
    for i, (kicker, title, accent, fill, what, examples, wins, limit) in enumerate(cols):
        x = 56 + i * (cw + gap)
        bg, stroke, ring = styles[i]
        s.append(rect(x, top, cw, ch, fill=bg, stroke=stroke, rx=12))
        if ring:
            s.append(f'<rect x="{x}" y="{top}" width="{cw}" height="{ch}" rx="12" '
                     f'fill="none" stroke="{Q_HIGH}" stroke-width="2.5"/>')
        s.append(rect(x, top, 4, ch, fill=accent, rx=2))
        s.append(text(x + 22, top + 36, kicker, 11, 700, accent, ls="1.4"))
        s.append(text(x + 22, top + 63, title, 17.5, 700, INK))
        y = top + 92
        s.append(para(x + 22, y, what, 13.5, 400, INK2, max_w=cw - 44, lh=1.45))
        y += para_h(what, 13.5, cw - 44, 1.45) + 18
        s.append(text(x + 22, y, "EXAMPLES", 9.5, 700, MUTED, ls="1.2"))
        pr, ph = pill_row(x + 22, y + 10, examples, bg=(TINT1 if bg == PANEL else PANEL),
                          max_x=x + cw - 18)
        s.append(pr)
        y += 12 + ph + 14
        s.append(line(x + 22, y, x + cw - 22, y, RULE, 1))
        y += 22
        s.append(text(x + 22, y, "WHERE IT WINS", 9.5, 700, GOOD, ls="1.2"))
        s.append(para(x + 22, y + 20, wins, 13, 400, INK2, max_w=cw - 44, lh=1.45))
        y += 20 + para_h(wins, 13, cw - 44, 1.45) + 20
        s.append(text(x + 22, y, "WHERE IT RUNS OUT", 9.5, 700, CRIT, ls="1.2"))
        s.append(para(x + 22, y + 20, limit, 13, 400, INK2, max_w=cw - 44, lh=1.45))
    y = top + ch + 44
    s.append(callout(56, y, W - 112, "Most organisations end up with all three. The useful "
                                     "question is not which one wins - it is which layer owns "
                                     "which use case."))
    s.append(svg_close())
    write("01-ai-platform-landscape.svg", "\n".join(s))


# ══════════════════════════════════════════════════ 2. four levels of autonomy
def d2():
    W = 1200
    levels = [
        ("LEVEL 1", "AI assistant", Q_LOW, TINT1,
         "Answers when asked. Every step is a prompt.",
         "The human drives. Nothing happens between questions.",
         ["ChatGPT"], False),
        ("LEVEL 2", "Co-pilot", Q_MID, TINT2,
         "Works alongside you inside a task. Proposes and executes under supervision.",
         "The human reviews each step and stays in the loop throughout.",
         ["Claude Code", "Cursor"], False),
        ("LEVEL 3", "Agentic AI", Q_HIGH, TINT3,
         "Owns a process end to end. Chooses its own tool calls and runs unattended.",
         "The human sets the outcome and the guardrails, then reads the result.",
         ["Relevance AI", "Wonderful"], False),
        ("LEVEL 4", "Autonomous and self-improving", Q_OUT, TINTN,
         "Sets its own sub-goals, learns from its own runs, improves without being re-prompted.",
         "The human sets intent. The system manages its own performance.",
         ["The future"], True),
    ]
    top, rh, rgap = 214, 118, 14
    H = top + len(levels) * (rh + rgap) + 196
    s = [svg_open(W, H, "Four levels of agentic autonomy",
                  "Level 1 AI assistant, Level 2 co-pilot, Level 3 agentic AI, Level 4 "
                  "autonomous and self-improving - each with what it does, who drives, and "
                  "example products. Relevance AI spans levels 2 to 4.")]
    s.append(header(W, f"{KICK} - figure 2", "Four levels of autonomy, not one word",
                    "\"AI platform\" covers all four of these. What changes between levels is "
                    "not model quality - it is who is holding the steering wheel."))
    for i, (lvl, name, accent, fill, what, who, ex, future) in enumerate(levels):
        y = top + i * (rh + rgap)
        s.append(rect(56, y, W - 112, rh, fill=fill, rx=12))
        if future:
            s.append(f'<rect x="56" y="{y}" width="{W-112}" height="{rh}" rx="12" fill="none" '
                     f'stroke="{Q_OUT}" stroke-width="1.5" stroke-dasharray="7 5"/>')
        s.append(rect(56, y, 4, rh, fill=accent, rx=2))
        s.append(text(80, y + 38, lvl, 11.5, 700, accent, ls="1.4"))
        if future:
            p, _w = pill(80 + tw(lvl, 11.5, 700) + 16, y + 24, "NOT YET", 9.5, Q_OUT, PANEL, h=20)
            s.append(p)
        s.append(para(80, y + 66, name, 19, 700, INK, max_w=252, lh=1.18))
        s.append(text(340, y + 34, "WHAT IT DOES", 9.5, 700, MUTED, ls="1.2"))
        s.append(para(340, y + 54, what, 13.5, 500, INK, max_w=336, lh=1.44))
        s.append(text(704, y + 34, "WHO IS DRIVING", 9.5, 700, MUTED, ls="1.2"))
        s.append(para(704, y + 54, who, 13.5, 400, INK2, max_w=300, lh=1.44))
        s.append(text(1030, y + 34, "EXAMPLE", 9.5, 700, MUTED, ls="1.2"))
        for k, e in enumerate(ex):
            p, _w = pill(1030, y + 44 + k * 28, e, 11.5, INK, PANEL)
            s.append(p)
    y = top + len(levels) * (rh + rgap) + 24
    s.append(rect(56, y, W - 112, 56, fill=TINT3, rx=10))
    s.append(rect(56, y, 4, 56, fill=Q_HIGH, rx=2))
    s.append(text(76, y + 24, "Relevance AI spans Level 2 to Level 4.", 15, 700, INK))
    s.append(text(76, y + 44, "Level 3 is where a process stops needing a human at every step.",
                  13.5, 400, INK2))
    y += 72
    s.append(callout(56, y, W - 112,
                     "Most organisations run a portfolio: Level 1 and 2 from OpenAI or "
                     "Anthropic, Level 3 and 4 on an agentic platform. Same reason engineering "
                     "teams run both Claude Code and Cursor."))
    s.append(svg_close())
    write("02-four-levels-of-autonomy.svg", "\n".join(s))


# ══════════════════════════════════════════════════════ 3. context first
def d3():
    W, H = 1200, 800
    systems = [
        ("SOURCE", "Email mailbox", "Microsoft Outlook",
         "Where invoices arrive. Polled automatically; attachments enabled.",
         "Pre-built connector", "OAuth", Q_HIGH),
        ("READING", "Document OCR", "Mistral AI",
         "Reads the PDF so fields come from the source document, not a guess.",
         "Pre-built connector", "API key", Q_HIGH),
        ("SYSTEM OF RECORD", "Invoice application", "Homegrown",
         "Where the invoice entry is lodged. No connector exists - none is needed.",
         "One-step API tool", "REST POST", Q_MID),
        ("VISIBILITY", "Notifications", "Slack",
         "Every run reports out, success or failure, to a channel humans watch.",
         "Pre-built connector", "OAuth", Q_HIGH),
    ]
    s = [svg_open(W, H, "Connect the systems before you build the agent",
                  "The four systems this use case needs - Outlook as source, Mistral for OCR, a "
                  "homegrown invoice application as system of record, and Slack for visibility - "
                  "with the connector type each uses and who owns each step.")]
    s.append(header(W, f"{KICK} - figure 3", "Context first. Agents second.",
                    "An agent with no reach is a chatbot. Before building anything, name the "
                    "systems the use case touches and connect them."))
    cw, gap = 254, 24
    top, ch = 230, 312
    for i, (band_, title, vendor, why, how, auth, accent) in enumerate(systems):
        x = 56 + i * (cw + gap)
        s.append(rect(x, top, cw, ch, fill=PANEL, stroke=GRID, rx=12))
        s.append(rect(x, top, cw, 4, fill=accent, rx=2))
        s.append(text(x + 20, top + 36, band_, 10, 700, accent, ls="1.3"))
        s.append(para(x + 20, top + 64, title, 18, 700, INK, max_w=cw - 40, lh=1.2))
        s.append(text(x + 20, top + 90, vendor, 13, 500, MUTED))
        s.append(line(x + 20, top + 108, x + cw - 20, top + 108, GRID, 1))
        s.append(para(x + 20, top + 132, why, 13, 400, INK2, max_w=cw - 40, lh=1.45))
        s.append(text(x + 20, top + ch - 76, "HOW IT CONNECTS", 9.5, 700, MUTED, ls="1.2"))
        p1, w1 = pill(x + 20, top + ch - 64, how, 11, INK,
                      TINT3 if how.startswith("Pre") else TINT2)
        s.append(p1)
        p2, _ = pill(x + 20, top + ch - 32, auth, 11, INK2, TINTN)
        s.append(p2)
        if i < len(systems) - 1:
            ax = x + cw + 3
            s.append(arrow(ax, top + ch / 2, ax + gap - 6, top + ch / 2, RULE, 2))

    y = top + ch + 46
    s.append(text(56, y, "WHO DOES WHAT", 11.5, 700, MUTED, ls="1.4"))
    s.append(line(56, y + 14, W - 56, y + 14, GRID, 1))
    halves = [("IT", "Authorise the connection. Once.",
               "Approve the OAuth grant, hold the API key, confirm the endpoint is reachable. "
               "IT is the facilitator here, not the builder.", Q_HIGH, TINT3),
              ("The subject matter expert", "Everything after that.",
               "Writes the SOP, builds the agent, tests it, iterates it. The person who "
               "understands invoices is the person who should own the invoice agent.",
               ACCENT, TINT1)]
    hw = (W - 112 - 24) / 2
    for i, (who, claim, detail, accent, fill) in enumerate(halves):
        x = 56 + i * (hw + 24)
        s.append(rect(x, y + 34, hw, 118, fill=fill, rx=12))
        s.append(rect(x, y + 34, 4, 118, fill=accent, rx=2))
        s.append(text(x + 20, y + 64, who.upper(), 10.5, 700, accent, ls="1.3"))
        s.append(text(x + 20, y + 90, claim, 17, 700, INK))
        s.append(para(x + 20, y + 112, detail, 13, 400, INK2, max_w=hw - 40, lh=1.45))
    s.append(svg_close())
    write("03-context-before-agents.svg", "\n".join(s))


# ══════════════════════════════════════════════════════ 4. Richard's anatomy
def d4():
    W, H = 1200, 1010
    s = [svg_open(W, H, "What Richard the Invoice Manager is made of",
                  "The agent's trigger, its configuration, the three parts of its system prompt "
                  "- guardrails, classification rules and a seven-step workflow - and the four "
                  "tools it can call.")]
    s.append(header(W, f"{KICK} - figure 4", "What \"Richard the Invoice Manager\" is made of",
                    "Read from the live agent. A trigger that wakes it, an instruction set that "
                    "constrains it, and four tools that let it touch the outside world."))

    # trigger
    ty = 214
    s.append(rect(56, ty, W - 112, 74, fill=TINT3, rx=12))
    s.append(rect(56, ty, 4, 74, fill=Q_HIGH, rx=2))
    s.append(text(78, ty + 28, "TRIGGER", 10.5, 700, Q_HIGH, ls="1.3"))
    s.append(text(78, ty + 52, "Outlook mailbox, polled automatically - attachments enabled",
                  16.5, 700, INK))
    p, w = pill(760, ty + 24, "Runs unattended", 11, INK, PANEL)
    s.append(p)
    p2, _ = pill(760 + w + 8, ty + 24, "No human in the loop to start it", 11, INK2, PANEL)
    s.append(p2)
    s.append(arrow(W / 2, ty + 80, W / 2, ty + 104, RULE, 2))

    # the agent
    ay, ah = ty + 112, 452
    s.append(rect(56, ay, W - 112, ah, fill=PANEL, stroke=RULE, rx=14, sw=1.5))
    s.append(text(80, ay + 36, "THE AGENT", 10.5, 700, ACCENT, ls="1.3"))
    s.append(text(80, ay + 62, "Richard the Invoice Manager", 21, 700, INK))
    s.append(para(80, ay + 86, "Monitors the invoice mailbox, identifies invoice emails, extracts "
                               "invoice data, submits complete invoices to the homegrown invoice "
                               "application, and reports results for human visibility.",
                  13.5, 400, INK2, max_w=700, lh=1.45))

    cfg = ["Model: cost-optimized", "Temperature 0", "Autonomy limit 50",
           "Approval mode: ask", "Memory off", "Extended thinking off"]
    s.append(text(80, ay + 156, "CONFIGURATION", 9.5, 700, MUTED, ls="1.2"))
    pr, ph = pill_row(80, ay + 168, cfg, 11, INK2, TINTN, max_x=W - 80)
    s.append(pr)

    # three parts of the instruction set
    iy = ay + 168 + ph + 22
    parts = [
        ("GUARD RAILS", "Facts only, or stop", [
            "Facts from the email, attachment or",
            "tool results only",
            "Never invent invoice details",
            "Missing or ambiguous, stop and ask",
            "No success claim without API proof",
        ], CRIT),
        ("CLASSIFICATION RULES", "What counts as an invoice", [
            "PDF: Sold-To, Bill-To, Order Details,",
            "Billing Summary, Invoice Date,",
            "Invoice Number, Due Date, Price",
            "Body only: Order#, Order Summary,",
            "Total Due, Due Date, Bill Number",
        ], ACCENT),
        ("WORKFLOW", "Seven ordered steps", [
            "Classify, read the PDF, extract,",
            "validate, escalate or submit,",
            "notify, record",
            "OCR is mandatory even when the",
            "email already contains its text",
        ], Q_HIGH),
    ]
    pw = (W - 112 - 48 - 40) / 3
    for i, (kicker, claim, lines, accent) in enumerate(parts):
        x = 80 + i * (pw + 24)
        s.append(rect(x, iy, pw, 176, fill=TINT1, rx=10))
        s.append(rect(x, iy, 3, 176, fill=accent, rx=2))
        s.append(text(x + 16, iy + 26, kicker, 9.5, 700, accent, ls="1.2"))
        s.append(text(x + 16, iy + 48, claim, 14.5, 700, INK))
        for k, ln in enumerate(lines):
            s.append(text(x + 16, iy + 76 + k * 22, ln, 11.5, 400, INK2))
    s.append(text(80, ay + ah - 22, "System prompt: 49 lines, 3,637 characters",
                  11.5, 500, MUTED))

    s.append(arrow(W / 2, ay + ah + 6, W / 2, ay + ah + 30, RULE, 2))

    # tools
    tly = ay + ah + 40
    s.append(text(56, tly, "FOUR TOOLS", 11.5, 700, MUTED, ls="1.4"))
    s.append(line(56, tly + 14, W - 56, tly + 14, GRID, 1))
    tools = [
        ("Find email in the mailbox", "Microsoft Outlook", "OAuth", "1 step", "Built by Invent"),
        ("Read the PDF with OCR", "Mistral AI", "API key", "2 steps", "Built in the builder"),
        ("Create the invoice record", "Homegrown API", "REST POST", "1 step",
         "Built in the builder"),
        ("Post the notification", "Slack", "OAuth", "2 steps", "Reused from another use case"),
    ]
    tw_, tgap = 254, 24
    for i, (title, vendor, auth, steps, origin) in enumerate(tools):
        x = 56 + i * (tw_ + tgap)
        y = tly + 34
        s.append(rect(x, y, tw_, 128, fill=PANEL, stroke=GRID, rx=10))
        s.append(text(x + 16, y + 26, f"0{i+1}", 10.5, 700, ACCENT, ls="1"))
        s.append(para(x + 16, y + 50, title, 15, 700, INK, max_w=tw_ - 32, lh=1.22))
        s.append(text(x + 16, y + 88, vendor, 12.5, 500, INK2))
        p1, w1 = pill(x + 16, y + 98, auth, 10, INK2, TINTN, h=20)
        s.append(p1)
        p2, _ = pill(x + 16 + w1 + 6, y + 98, steps, 10, INK2, TINTN, h=20)
        s.append(p2)
    s.append(svg_close())
    write("04-richard-anatomy.svg", "\n".join(s))


# ══════════════════════════════════════════════════════ 5. decision flow
def d5():
    W, H = 1200, 1246
    s = [svg_open(W, H, "Richard's decision flow, from the SOP",
                  "A flowchart: an email arrives, is classified as an invoice or not, the PDF is "
                  "read with OCR, six fields are extracted and validated, and the invoice is "
                  "either escalated for human review or posted to the API and reported to Slack.")]
    s.append(header(W, f"{KICK} - figure 5", "The SOP, as the agent actually runs it",
                    "Two of these branches stop the process. That is the point - a good agent "
                    "has more ways to stop than it has ways to act."))

    CX = 430          # main column centre
    bw = 396          # main box width
    SX = 900          # side column centre
    sw_ = 300

    def box(cx, y, w, h, title, sub=None, fill=PANEL, stroke=GRID, accent=None, tcol=INK):
        o = [rect(cx - w / 2, y, w, h, fill=fill, stroke=stroke, rx=10)]
        if accent:
            o.append(rect(cx - w / 2, y, 4, h, fill=accent, rx=2))
        o.append(text(cx, y + (30 if sub else h / 2 + 6), title, 15, 700, tcol, anchor="middle"))
        if sub:
            for k, ln in enumerate(wrap(sub, 12.5, w - 44)):
                o.append(text(cx, y + 50 + k * 18, ln, 12.5, 400, INK2, anchor="middle"))
        return "\n".join(o)

    def diamond(cx, cy, w, h, label):
        o = [f'<path d="M {cx} {cy-h/2} L {cx+w/2} {cy} L {cx} {cy+h/2} L {cx-w/2} {cy} Z" '
             f'fill="{TINT3}" stroke="{Q_HIGH}" stroke-width="1.5"/>']
        lines = wrap(label, 13.5, w - 90, 700)
        for k, ln in enumerate(lines):
            o.append(text(cx, cy - (len(lines) - 1) * 9 + k * 18 + 5, ln, 13.5, 700, INK,
                          anchor="middle"))
        return "\n".join(o)

    def vlink(cx, y1, y2, label=None):
        o = [arrow(cx, y1, cx, y2, RULE, 2)]
        if label:
            o.append(text(cx + 10, (y1 + y2) / 2 + 4, label, 11.5, 700, INK2))
        return "\n".join(o)

    def hlink(x1, y, x2, label):
        o = [arrow(x1, y, x2, y, RULE, 2),
             text((x1 + x2) / 2, y - 10, label, 11.5, 700, INK2, anchor="middle")]
        return "\n".join(o)

    y = 214
    s.append(box(CX, y, bw, 62, "Email arrives in the mailbox", accent=ACCENT, fill=TINT1))
    s.append(vlink(CX, y + 66, y + 92))

    # decision 1
    y = y + 92
    s.append(diamond(CX, y + 46, 340, 92, "Invoice indicators present?"))
    s.append(hlink(CX + 172, y + 46, SX - sw_ / 2 - 4, "no"))
    s.append(box(SX, y + 12, sw_, 68, "Stop. No invoice detected.",
                 "Say so and take no external action.", fill=TINTN, accent=Q_OUT))
    s.append(vlink(CX, y + 96, y + 122, "yes"))

    # decision 2
    y = y + 122
    s.append(diamond(CX, y + 46, 340, 92, "PDF attachment?"))
    s.append(hlink(CX + 172, y + 46, SX - sw_ / 2 - 4, "no"))
    s.append(box(SX, y + 12, sw_, 68, "Extract from the email body",
                 "Supplier, number, due date, description, amount.",
                 fill=TINT1, accent=ACCENT))
    s.append(vlink(CX, y + 96, y + 122, "yes"))

    # OCR
    y = y + 122
    s.append(box(CX, y, bw, 76, "Read the PDF with Mistral OCR",
                 "Mandatory - even if the email already contains OCR text.",
                 fill=TINT1, accent=ACCENT))
    s.append(f'<line x1="{SX}" y1="{y-34}" x2="{SX}" y2="{y+112}" stroke="{RULE}" '
             f'stroke-width="2" stroke-linecap="round"/>')
    s.append(vlink(CX, y + 80, y + 104))

    # extract + validate
    y = y + 104
    s.append(box(CX, y, bw, 76, "Extract, then validate six fields",
                 "invoiceNumber, invoiceDate, description, merchant, owner, amount",
                 fill=PANEL, accent=ACCENT))
    s.append(f'<path d="M {SX} {y+8} L {SX} {y+38} L {CX+bw/2+4} {y+38}" fill="none" '
             f'stroke="{RULE}" stroke-width="2" stroke-linecap="round" '
             f'marker-end="url(#ah)"/>')
    s.append(vlink(CX, y + 80, y + 106))

    # decision 3
    y = y + 106
    s.append(diamond(CX, y + 50, 380, 100, "All six present and valid?"))
    s.append(hlink(CX + 192, y + 50, SX - sw_ / 2 - 4, "no"))
    s.append(box(SX, y + 8, sw_, 84, "Escalate for human review",
                 "Name what is missing and why it stopped. Do not call the API.",
                 fill=TINTN, accent=CRIT))
    s.append(vlink(CX, y + 104, y + 130, "yes"))

    # post
    y = y + 130
    s.append(box(CX, y, bw, 62, "POST to the invoice API", accent=Q_HIGH, fill=TINT3))
    s.append(vlink(CX, y + 66, y + 92))

    # decision 4
    y = y + 92
    s.append(diamond(CX, y + 46, 340, 92, "API confirms success?"))
    s.append(hlink(CX + 172, y + 46, SX - sw_ / 2 - 4, "no"))
    s.append(box(SX, y + 12, sw_, 68, "Slack the error",
                 "Never claim success without confirmation.", fill=TINTN, accent=CRIT))
    s.append(vlink(CX, y + 96, y + 122, "yes"))

    # done
    y = y + 122
    s.append(box(CX, y, bw, 76, "Slack the invoice ID, then record the run",
                 "What was extracted, whether it submitted, what Slack returned.",
                 fill=TINT3, accent=Q_HIGH))
    s.append(svg_close())
    write("05-richard-decision-flow.svg", "\n".join(s))


# ══════════════════════════════════════════════════════ 6. end-to-end run
def d6():
    W = 1200
    steps = [
        ("00:00", "Trigger", "Outlook delivers \"Fwd: Your Superloop Bill\"",
         ["Attachment: Invoice.pdf, 3 pages",
          "No human involved in starting the run"], ACCENT),
        ("00:00", "Classify", "Invoice confirmed from the PDF",
         ["Indicators found: Tax Invoice, Invoice Number, Date of Issue,",
          "This Bill, This Bill Due, This Bill Summary"], ACCENT),
        ("00:05", "Read", "Mistral OCR parses pages 1-3",
         ["Fields come from the source document,",
          "not from the summary in the email body"], ACCENT),
        ("00:12", "Extract", "Six required fields, plus context",
         ["merchant: Superloop Limited (ABN 96 169 263 094)",
          "invoiceNumber: E87296308",
          "invoiceDate: 2026-08-08",
          "dueDate: 2026-08-24",
          "amount: 110.35 AUD",
          "description: Broadband $109.00; Card Processing Fee $1.35",
          "owner: Jefferson Haw"], ACCENT),
        ("00:14", "Validate", "6 of 6 present and valid",
         ["Date coercible. Amount numeric and at least zero.",
          "No missing or ambiguous values, so no escalation."], Q_HIGH),
        ("00:16", "Submit", "POST returns 201 Created",
         ["Invoice id returned: cmswsg21i0000uvxzzf8d0h0h",
          "The API echoed the record back with timestamps"], Q_HIGH),
        ("00:33", "Report", "Slack notification posted",
         ["The created invoice, the extracted fields and the returned id"], Q_HIGH),
    ]

    def row_h(detail):
        """Fit the detail lines, with a floor so short rows still read as rows."""
        return max(90, 78 + (len(detail) - 1) * 17)

    top = 244
    pitch = 12
    heights = [row_h(d) for _t, _n, _w, d, _a in steps]
    H = top + sum(heights) + pitch * (len(steps) - 1) + 160
    s = [svg_open(W, H, "One successful end-to-end run",
                  "A seven-step trace of a real run: Outlook trigger, classification, Mistral "
                  "OCR, field extraction, validation, a 201 Created from the invoice API with "
                  "the returned invoice id, and a Slack notification - 33 seconds end to end.")]
    s.append(header(W, f"{KICK} - figure 6", "One run, start to finish, no human touch",
                    "Pulled from the agent's own task history. Elapsed times are relative to "
                    "the first message; the whole run took 33 seconds."))
    s.append(text(56, top - 20, "ELAPSED", 9.5, 700, MUTED, ls="1.2"))
    s.append(text(150, top - 20, "STEP", 9.5, 700, MUTED, ls="1.2"))
    s.append(text(330, top - 20, "WHAT HAPPENED", 9.5, 700, MUTED, ls="1.2"))
    s.append(line(56, top - 8, W - 56, top - 8, RULE, 1.5))

    y = top
    for i, (t, name, what, detail, accent) in enumerate(steps):
        h = heights[i]
        s.append(rect(56, y, W - 112, h, fill=TINT1 if i % 2 == 0 else PANEL, rx=10))
        s.append(rect(56, y, 3, h, fill=accent, rx=2))
        s.append(text(76, y + 34, t, 13, 700, MUTED))
        s.append(f'<circle cx="132" cy="{y+29:.1f}" r="15" fill="{accent}"/>')
        s.append(text(132, y + 34, str(i + 1), 13, 700, "#ffffff", anchor="middle"))
        s.append(text(158, y + 34, name, 15.5, 700, INK))
        s.append(text(330, y + 30, what, 15, 600, INK))
        for k, ln in enumerate(detail):
            s.append(text(330, y + 52 + k * 17, ln, 11.5, 400, INK2))
        if i < len(steps) - 1:
            s.append(f'<line x1="132" y1="{y+46:.1f}" x2="{y and 132 or 132}" '
                     f'y2="{y+h+pitch-2:.1f}" stroke="{GRID}" stroke-width="2" '
                     f'stroke-linecap="round"/>')
        y += h + pitch

    y += 10
    ico, col = status_icon(80, y + 26, True, 13)
    s.append(rect(56, y, W - 112, 56, fill=TINT3, rx=10))
    s.append(rect(56, y, 4, 56, fill=Q_HIGH, rx=2))
    s.append(ico)
    s.append(text(104, y + 25, "Invoice recorded and reported in 33 seconds.", 15, 700, INK))
    s.append(text(104, y + 44, "Four systems touched. Zero human steps. One Slack message to "
                               "prove it happened.", 13.5, 400, INK2))
    s.append(svg_close())
    write("06-end-to-end-run.svg", "\n".join(s))


# ══════════════════════════════════════════════════════ 7. iteration log
def d7():
    W = 1200
    runs = [
        ("RUN 1", "OCR came back empty", False,
         "The OCR step returned nothing, and the invoice API tool was not attached yet.",
         "Richard refused to submit, extracted what it could from the email body, and asked "
         "for a human.",
         "The guardrail worked before the happy path did. That is the right order."),
        ("RUN 2", "POST returned 404", False,
         "OCR read the PDF correctly. The POST went to /api/invoice - the endpoint is "
         "/api/invoices.",
         "Richard reported the failure to Slack with the payload, and did not claim the "
         "invoice was recorded.",
         "Do not make an agent remember a URL. Pin the endpoint inside the tool."),
        ("RUN 3", "201 Created", True,
         "OCR read pages 1-3, six fields validated, POST accepted, invoice id returned.",
         "Slack posted the created invoice and its id.",
         "Nothing changed about the instructions. One wrong character was the whole gap."),
        ("RUN 4", "Correctly ignored", True,
         "A Vanta \"overdue security tasks\" email arrived in the same mailbox.",
         "Classified as not an invoice. No OCR, no API call, no Slack noise.",
         "Test the negative case. An agent that never says no will submit rubbish."),
    ]
    top, rh, rgap = 240, 152, 14
    H = top + len(runs) * (rh + rgap) + 130
    s = [svg_open(W, H, "Four runs of iteration on one agent",
                  "Run one: OCR empty, agent escalated. Run two: a 404 from a mistyped "
                  "endpoint, agent reported the failure. Run three: 201 Created. Run four: a "
                  "non-invoice email correctly ignored.")]
    s.append(header(W, f"{KICK} - figure 7", "It took four runs, and two of them failed",
                    "The failures are the useful part. Each one shows a guardrail holding "
                    "while something underneath was still wrong."))
    s.append(text(56, top - 20, "RUN", 9.5, 700, MUTED, ls="1.2"))
    s.append(text(420, top - 20, "WHAT WENT WRONG, OR RIGHT", 9.5, 700, MUTED, ls="1.2"))
    s.append(text(770, top - 20, "WHAT RICHARD DID", 9.5, 700, MUTED, ls="1.2"))
    s.append(line(56, top - 8, W - 56, top - 8, RULE, 1.5))
    for i, (num, verdict, ok, what, did, lesson) in enumerate(runs):
        y = top + i * (rh + rgap)
        s.append(rect(56, y, W - 112, rh, fill=PANEL, stroke=GRID, rx=12))
        s.append(rect(56, y, 4, rh, fill=(GOOD if ok else CRIT), rx=2))
        s.append(text(80, y + 32, num, 10.5, 700, MUTED, ls="1.3"))
        ico, col = status_icon(92, y + 60, ok)
        s.append(ico)
        s.append(para(114, y + 65, verdict, 16.5, 700, INK, max_w=250, lh=1.2))
        s.append(para(420, y + 32, what, 13, 400, INK2, max_w=326, lh=1.45))
        s.append(para(770, y + 32, did, 13, 400, INK2, max_w=352, lh=1.45))
        s.append(line(80, y + rh - 44, W - 80, y + rh - 44, GRID, 1))
        s.append(text(80, y + rh - 20, "LESSON", 9.5, 700, ACCENT, ls="1.2"))
        s.append(text(150, y + rh - 20, lesson, 13.5, 500, INK))
    y = top + len(runs) * (rh + rgap) + 20
    s.append(callout(56, y, W - 112,
                     "Building the agent took one SOP. Getting it right took four runs and one "
                     "character. Budget for the second part.", h=56))
    s.append(svg_close())
    write("07-iteration-log.svg", "\n".join(s))


if __name__ == "__main__":
    print("Generating Part Two SVG diagrams:")
    for fn in (d1, d2, d3, d4, d5, d6, d7):
        fn()
    print("Done.")
