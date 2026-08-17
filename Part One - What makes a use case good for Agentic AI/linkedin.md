<!--
LINKEDIN VERSION of Part One. Same argument as README.md, reshaped for the
LinkedIn article editor.

HOW TO USE THIS FILE
1. LinkedIn's editor does not read Markdown. Paste the body as plain text, then
   apply Heading 2 to the ## lines and Heading 3 to the ### lines using the
   toolbar, and bold the lead-ins manually (they are marked **like this**).
2. Upload the PNGs from ./assets/ at each [IMAGE n] marker. The alt text for each
   is given beside the marker - paste it into LinkedIn's alt-text field.
   PNGs are 1200px wide, which is what LinkedIn wants.
3. Delete every [IMAGE n] marker line and this comment block before publishing.
4. Suggested title, subtitle and hashtags are at the bottom.
-->

# Most agentic AI projects don't fail in the build. They fail in the pick.

I have watched teams ship a technically excellent agent that nobody wanted.

The pattern is consistent enough to be boring. Someone picks a use case that sounds impressive. Six or eight weeks disappear into building it. The demo works. And then it dies quietly — because the process it automated only ran eleven times a quarter, or because the person who was supposed to accept its output had never agreed to, or because nobody could say what number moved.

Nothing went wrong in the build. Everything went wrong before it.

Selecting the right use case is the highest-leverage twenty minutes in an agentic AI program. It is also the part most teams treat as already settled, because a slide from the sales cycle said so.

Here is how I'd run it instead.

---

## Selection doesn't happen in presales

[IMAGE 1 — 01-where-selection-happens.png]
Alt text: Where use case selection actually happens — a five-stage timeline from presales through kickoff, ideation and pressure-testing to build. Ideation and pressure-testing are highlighted as the stages where the decision is actually made.

Presales produces a **direction**. That's genuinely useful — someone has already found the pain, and you're not starting from a blank page. But a direction is not a plan, and the slide that won the deal was written to win the deal.

So implementation planning should start by taking the presales use cases as input and **pressure-testing them** — on feasibility and on value, separately. Some survive intact. Some turn out to be three use cases wearing one name. Some quietly fail a criterion nobody checked during the sales cycle.

That pressure-test has to happen with the **champion and the executive buyer**, after kickoff. Two reasons.

**The champion knows where the bodies are buried.** They know the "documented" process has three undocumented exceptions, that the system of record isn't the system people actually use, and that the team who owns it is mid-reorg. None of that was in the deal.

**The executive buyer owns the sponsorship.** If they haven't personally re-confirmed the priority order, they haven't committed to defending it in eight weeks when someone asks why the team is spending time on this. Sponsorship that was never re-confirmed is sponsorship you don't have.

Ideation and pressure-testing are the two stages that get cut when a program runs late. Cutting them is precisely how a presales slide becomes a six-month build nobody sponsors.

### And no, the answer isn't "transform everything"

There's a version of this conversation where the answer is "all of it" — rebuild how the company works, agents everywhere. It's an exciting conversation, and it's the most reliable way to kill an agentic AI program.

Org-wide transformation fails for reasons that have nothing to do with the technology. It needs every team's attention at once, when each team has its own quarter to survive. It has no early proof point, so it burns political capital before it produces evidence. It touches enough systems that one access request can stall everything. And it makes the program's first visible milestone a reorganisation, which is the least popular thing you can ask an organisation to look at.

Narrow, high-value, low-effort work does the opposite. It produces a result while people are still paying attention. That result buys the right to go wider.

---

## Value vs effort: aim for the top-right

[IMAGE 2 — 02-value-effort-quadrant.png]
Alt text: The value versus effort quadrant. Business value rises up the vertical axis, ease of delivery rises to the right, so the top-right quadrant is high value and low effort. Eight example use cases are plotted and keyed below.

Read the horizontal axis carefully, because it's drawn deliberately: it runs from **harder** on the left to **easier** on the right. That puts high value and low effort together in the top-right corner. If you've seen this grid with effort ascending rightward, the target moves to the top-left — same idea, mirrored. I draw it this way so "aim top-right" means one thing every time.

**Top-right — build first.** High value, low effort. One or two of these. This is the whole game.

**Top-left — sequence later.** High value, high effort. Real work, worth doing, and it will outrun your sponsorship if you start there. Put a date on revisiting it.

**Bottom-right — fill capacity.** Low value, low effort. Fine once the team has slack, never the flagship. This quadrant is dangerous because it *feels* productive: things ship, demos happen, and six weeks later there's no business number to point at.

**Bottom-left — decline.** Low value, high effort. Say no out loud, early, and in front of the executive buyer. A quiet no becomes a resurrection three months later.

The reason to be this disciplined isn't tidiness. It's that **executive attention has a half-life.** From kickoff you have a window in which the exec buyer is personally invested and will clear obstacles for you. Spend that window on something that produces a result inside it, and you get a second window longer than the first. Spend it on a transformation and you'll be explaining a Gantt chart to someone who has stopped attending.

---

## Five criteria for a high-probability use case

[IMAGE 3 — 03-five-criteria.png]
Alt text: The five criteria for a high-probability agentic use case — high volume, a documented process, owners already in place, system and knowledge context, and measurable business impact — with the question to ask and the failure mode for each.

These are gates, not a weighted average. A use case that clears four of five isn't 80% ready. It has one specific, nameable hole — and naming it is far more useful than averaging it away.

### 1. High volume

**Ask:** how many times a week does this happen, and who counts it?

The arithmetic is unforgiving. An agent that saves twenty minutes on a task running forty times a year saves about thirteen hours annually. That's a demo. The same agent on a task running forty times a **day** is a different conversation.

The failure mode is low volume dressed up as high stakes. "It only happens a few times a year, but when it does it's critical" is often a real problem — it's just rarely an agentic one.

### 2. A documented process

**Ask:** can you show me the SOP, the checklist, or a screen recording?

This is the gate that fails most often and the one people most want to wave through. If the process only exists in someone's head, you're not automating a process — you're inventing one, on a deadline, while also building an agent. That's organisational design disguised as engineering.

When two leaders describe the same process differently in the same meeting, stop. The next step is a week-long workshop to write it down, not a quarter-long build.

### 3. Owners already in place — business and technical

**Ask:** who owns this in the business, and who owns the systems it touches?

Two named people, both with time. The business owner accepts the output and is accountable for the metric. The technical owner opens the doors: access, credentials, the security review.

The failure mode is an enthusiastic executive and nobody accountable underneath. Executive interest is necessary and not sufficient. Without a business owner the output has no home; without a technical owner, access requests sit in a queue for five weeks and the momentum you were protecting is gone.

### 4. System and knowledge context

**Ask:** what must the agent read in order to be right, and can we actually reach it?

Name the systems, documents, definitions and edge-case rules the agent needs, and confirm they exist somewhere retrievable — not in someone's head, not in a deck from 2023, not in a system nobody has credentials for.

An agent with no grounding doesn't fail loudly. It guesses, fluently and confidently, and people believe it. That's worse than no agent, because it damages trust in the whole program rather than in one workflow.

### 5. Measurable business impact

**Ask:** what number moves, by how much, and who already reports it?

"Already reports it" is the load-bearing part. If proving the benefit requires inventing a metric, establishing a baseline and getting someone to own a dashboard, the measurement project is bigger than the agent project — and at renewal the conversation becomes an argument about vibes.

What good looks like: an existing metric on an existing report, ideally one the exec buyer already looks at. Speed to first touch. First-response time. Days to close. Cost per invoice processed.

**Five for five is the bar.** Four out of five isn't a green light; it's a named piece of work to do before the build starts. Usually days, not months — and doing it first is what separates programs that compound from programs that stall.

---

## Score it, don't argue it

[IMAGE 4 — 04-scoring-to-quadrant.png]
Alt text: How a scoring sheet turns criteria into a quadrant — weighted value inputs and weighted effort inputs feed one comparison rule, which places each use case into build first, sequence later, fill capacity or decline.

Everything above is judgement, and judgement in a workshop has a problem: the most senior voice wins, and nobody can reconstruct the reasoning two months later.

So put it in a shared sheet. Not because a number is truer than a conversation — because a number is **re-runnable, visible, and arguable in public.**

Score each input 1 to 5. Weight them. Normalise both totals to a 0–100 index.

**Value inputs:** annual hours or cost released (×3), volume (×2), strategic pull from the exec buyer (×2), quality or risk upside (×1).

**Effort inputs:** process documentation maturity (×3), system access and integration count (×3), knowledge and data readiness (×2), owner availability (×1).

Score every effort input so that 5 always means hardest, then flip the total into an **ease** index — so high ease means easy to deliver, which is what puts good candidates in the top-right.

Then one rule: **value index above threshold AND ease index above threshold → build first.** Everything else falls out of the same comparison.

Three things this buys you that a whiteboard doesn't.

**Nobody places their own use case.** The most common workshop failure is the sponsor of an idea deciding which quadrant it goes in. Take that away and most of the politics goes with it.

**Disagreement becomes specific.** "I think that's low effort" is unarguable. "I scored system access a 2, you scored it a 5" resolves in ninety seconds, because one of you knows something the other doesn't. That's the whole value of the exercise.

**The ranking survives re-scoring.** Someone will ask "what if the exec cares more about risk than hours?" Change the weight, watch the ranking move, decide with the new order in front of you. Ten seconds, in the meeting.

---

## The same five criteria, two very different answers

[IMAGE 5 — 05-scorecard-comparison.png]
Alt text: Two scorecards side by side. Inbound lead qualification passes all five criteria and is a build-first candidate. "Make our strategy process AI-powered" passes one of five and should be declined for now.

Both of these came up in the same kickoff, twenty minutes apart.

**"Inbound lead qualification and routing"**, from the sales ops lead. Eighteen hundred leads a month, already reported. Routing rules written down in the sales playbook. Sales ops owns the outcome, RevOps owns the CRM. The CRM, enrichment tool and ICP definition are all reachable. Speed to first touch is already on the executive dashboard. Five for five.

**"Make our strategy process AI-powered"**, from the CEO at the end of the meeting. A handful of cycles a year. No two leaders describe the process the same way. The context lives in people's heads and old decks. No metric anyone currently reports. One for five — and the one it passes is "owners in place", on the strength of the CEO being personally interested.

The second is more exciting. It's also, right now, undeliverable.

And here's the part that matters: the answer isn't "no". It's **"not yet, and here are the four things that have to be true first."** That reframing is the difference between declining a request and handing a CEO a roadmap. One of those makes you a partner.

---

## Teach the customer to run it without you

[IMAGE 6 — 06-ideation-deck-anatomy.png]
Alt text: Anatomy of a modular use case ideation deck — a fixed core, an audience-swappable middle of worked examples by team, and an appendix holding the long tail.

You can run this exercise for a customer once. It's better if they can run it themselves, for the next team, without you. Build the ideation deck as three layers rather than one deck and it survives contact with a real audience.

**The core, always in.** The agent menu — what agents can actually do, in plain language, because most people's mental model is either a chatbot or a robot. How you score and prioritise. Two ROI spotlights with real numbers. Cut any of this and the session drifts into a wish list.

**The middle, swapped for the room.** Worked examples by team: sales, marketing, customer success, operations, finance. Bring **one**. Leaving the sales examples in front of a marketing audience is the fastest way to lose a room — it reads as "we haven't thought about you", and everything after it gets discounted.

**The appendix, on request.** The long tail: rarer team-specific use cases, edge cases people ask about, and things you've seen fail and why. Never presented linearly. It exists so that when someone asks "what about *our* team?", you answer with a slide instead of a promise.

Two habits worth building. **Tailor before you send, not during the call** — ask who's in the room, delete the packs that don't apply, reorder so their team is slide three, move the rest to the appendix. And keep the core free of anything that assumes a signed contract, so the same deck works in presales or in a free-sales motion where you're helping someone see what's possible before they've committed to anything.

---

## Six ways this goes wrong

**The presales handoff.** Treating the deal-stage list as settled. It's an input, written under different incentives.

**The transformation trap.** "Let's redesign how the company works." No early proof, every team's attention at once, first milestone is a reorg.

**The undocumented process.** Building an agent for a process that doesn't exist in writing. You'll do process design under build-phase deadlines, badly.

**The orphan use case.** Executive enthusiasm, no business owner, no technical owner. The output has nowhere to go and access never clears.

**The vanity metric.** "Efficiency gains" with no baseline and no existing report. At renewal you'll have anecdotes where you needed a number.

**Boiling the list.** Twelve use cases in parallel because saying no felt impolite. Twelve half-built agents are worth less than one finished one, and cost more.

---

## What to do this week

1. Write down every candidate use case you've heard, including the ones from presales. Aim for fifteen, not five — you narrow later.
2. Answer the five gates for each. Y or N, no maybes.
3. For anything below five, write down the **specific** gap and who could close it. Most gaps are days of work.
4. Score value and effort for everything that clears all five, and let the ranking fall out.
5. Book ninety minutes with your champion and executive buyer. Score live, get the ranking re-confirmed out loud.
6. Pick **one or two**. Write down what you're declining and why, and send it the same day.

The scoring sheet I use — with the weights, the 1-to-5 anchors for every input, and ten worked examples — is free on GitHub, along with the diagrams above:

**github.com/hawjefferson/RelevanceAI-AgenticAI-Series**

Part Two covers what happens after you've picked: actually building the agent in Relevance AI — tools, system prompt, knowledge, and how to read the trace when it goes wrong.

What's the worst agentic use case you've seen get picked, and which of the five gates did it fail?

---
---

## Publishing notes (delete before posting)

**Suggested title**
> Most agentic AI projects don't fail in the build. They fail in the pick.

**Alternative titles**
> - The five criteria I use before agreeing to build an AI agent
> - Why your best agentic AI use case is probably the boring one
> - How to choose an agentic AI use case that survives contact with an org

**Suggested subtitle / hook line**
> A framework for choosing agentic AI use cases: the value-effort quadrant, five pass/fail criteria, and a scoring sheet you can take into your next ideation session.

**Hashtags** (LinkedIn favours 3–5)
> #AgenticAI #AIAgents #AIImplementation #RelevanceAI #Automation

**Cover image:** use `02-value-effort-quadrant.png` — it carries the single clearest idea.

**Length:** ~2,300 words. Long for a feed post, right for a LinkedIn *article*. If you want a feed post instead, the "Five criteria" section stands alone at ~500 words with figure 3 as the image.
