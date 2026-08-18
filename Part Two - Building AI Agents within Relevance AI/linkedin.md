<!--
LINKEDIN VERSION of Part Two. Same argument as README.md, reshaped for the
LinkedIn article editor.

HOW TO USE THIS FILE
1. LinkedIn's editor does not read Markdown. Paste the body as plain text, then
   apply Heading 2 to the ## lines and Heading 3 to the ### lines using the
   toolbar, and bold the lead-ins manually (they are marked **like this**).
2. Upload the PNGs from ./assets/ at each [IMAGE n] marker. Paste the alt text
   given beside the marker into LinkedIn's alt-text field.
3. Delete every [IMAGE n] marker line and this comment block before publishing.
4. Suggested title, subtitle and hashtags are at the bottom.

WHAT CHANGES FROM README.md
- Opens on the platform-selection problem, not on series navigation.
- No relative links; the GitHub URL and the SOP link are spelled out.
- Drops "What's in this folder" and the redaction footnote.
- Closes with a question that invites a specific answer.
-->

# Nobody tells you the hardest part of agentic AI is choosing what to build it on

You picked a use case. It has volume, it has a documented process, and it moves a number someone already reports. Good — that was the hard part, and I wrote about how to get there in Part One.

Then comes the question I get asked before anyone asks me about prompts: **what do we build it on?**

That question is harder than it should be, because the market describes wildly different products with the same three words. So here is how I break it down, and then a real agent I built — including the two runs that failed.

---

## Three shapes, not one market

[IMAGE 1 — 01-ai-platform-landscape.png]
Alt text: Three shapes of AI in the market — point solutions that solve one task for one industry, embedded AI inside tools you already own, and horizontal platforms that support any use case across business units — each with examples, where it wins and where it runs out.

**Point solutions** solve one specific problem very deeply, usually for one industry — Heidi Health doing clinical documentation for healthcare, for instance. If your use case is exactly the one it was built for, nothing horizontal will match its depth and nothing will get you to value faster. Where it runs out is the second use case. And the third. Each one is another vendor, another contract, another login.

**Embedded AI** ships inside products you already own: Notion agents, the copilot in your CRM, suggest-reply in your helpdesk. No procurement, no onboarding, and the context is already in the product — a genuine advantage people under-rate. Where it runs out is the edge of that product. Embedded AI can only see its own data, and most genuinely valuable work crosses systems.

**Horizontal platforms** are something you build on rather than switch on: Relevance AI, Wonderful, Anthropic, OpenAI. One platform, many use cases, many departments, and work spanning four systems is the normal case. Where it runs out is depth on a single vertical job — and the fact that it asks you to build something.

Most organisations end up with all three. The useful question is not which one wins. It is **which layer owns which use case**.

---

## And four levels of autonomy inside the horizontal layer

[IMAGE 2 — 02-four-levels-of-autonomy.png]
Alt text: Four levels of agentic autonomy — Level 1 AI assistant, Level 2 co-pilot, Level 3 agentic AI, Level 4 autonomous and self-improving — with what each does, who is driving, and example products. Relevance AI spans levels 2 to 4.

What changes between these is not model quality. It is who is holding the steering wheel.

**Level 1 — AI assistant.** Answers when asked. Every step is a prompt. ChatGPT. The human drives, and nothing happens between questions.

**Level 2 — Co-pilot.** Works alongside you inside a task, proposing and executing under supervision. Claude Code, Cursor. The human reviews each step.

**Level 3 — Agentic AI.** Owns a process end to end, chooses its own tool calls, runs unattended. Relevance AI, Wonderful. The human sets the outcome and the guardrails, then reads the result.

**Level 4 — Autonomous, self-learning and self-improving.** Sets its own sub-goals, learns from its own runs, improves without being re-prompted. This is the future, and anyone claiming to ship it today is selling Level 3 with better marketing.

Relevance AI spans Level 2 to Level 4.

Here is the part that trips up platform decisions: **depending on your AI maturity, you will end up running more than one platform, and that is fine.** It is already common practice — OpenAI or Anthropic for Level 1 and 2, something like Relevance AI for Level 3 and 4. Same reason engineering teams happily run both Claude Code and Cursor. Nobody calls that a failure to decide. It is a portfolio matched to the job.

---

## Why "platform-centric" changes who builds

The part of Relevance AI's approach that matters most in practice is not a model choice. It is **who is allowed to build**.

The platform gives subject matter experts the tools to build agents themselves. IT's role shifts to facilitating — onboarding the systems the organisation already uses, through pre-built connectors — and then getting out of the way. Different business units build their own agents and workforces on shared plumbing, and those agents start acting like part of the company's operating system rather than a side project.

This matters because the bottleneck in agentic AI is almost never the model. It is the distance between the person who understands the process and the person allowed to automate it. Every hop across that gap loses detail.

---

## Context first. Agents second.

[IMAGE 3 — 03-context-before-agents.png]
Alt text: The four systems an invoice use case needs — Outlook as source, Mistral AI for OCR, a homegrown invoice application as system of record, and Slack for visibility — with the connector type each uses and the split of work between IT and the subject matter expert.

Before you build anything, the platform needs the **context** the use case depends on: **system integrations**, and the **knowledge you already maintain**. So the first real step is connecting your systems of record.

My example is deliberately unglamorous: automate the invoices an organisation receives from multiple suppliers. Classify whether an inbound email is invoice-related; if it is, extract the data from the email or its PDF attachment; then lodge an entry in the invoice management system — which here is homegrown.

Four systems:

1. **Where the invoice comes from** — the email platform. Microsoft Outlook, polled automatically, attachments enabled.
2. **A model that can read a PDF** — Mistral AI, for OCR.
3. **Where the entry is lodged** — the homegrown invoice application, over its REST API.
4. **Notification of what happened** — Slack.

All four are supported, which is the point: onboarding took minutes, not a project. Three are pre-built connectors. The homegrown app has no connector and does not need one — a single-step API tool that POSTs a JSON body is enough.

**IT's job is to authorise the connection, once.** Approve the OAuth grant, hold the API key, confirm the endpoint is reachable. **Everything after that belongs to the subject matter expert.** The person who understands invoices should own the invoice agent.

---

## The build input is an SOP, not a prompt

With context in place, building the agent uses Relevance AI's Invent capability — and the only thing you supply is a **Standard Operating Procedure**. The same document you would hand a new starter.

Here is the one I used: https://docs.google.com/document/d/1fWO_nNq-v7AqLl9a70mQAQOpShTKPQpEifhVUFgnUxk/edit

This is where Part One earns its keep. "A documented process" was one of my five criteria, and this is the concrete reason: **the SOP is the build input.** If it does not exist, you are not blocked on the platform — you are blocked on knowing what your own process is.

A good SOP for this names five things: the role and its boundary, the classification rule in specifics, the ordered steps and which are mandatory, the exact output fields and what makes each valid, and the escalation rule. Miss the last one and you get an agent that guesses instead of asking.

---

## What it produced: "Richard the Invoice Manager"

[IMAGE 4 — 04-richard-anatomy.png]
Alt text: What Richard the Invoice Manager is made of — an Outlook trigger, the agent's configuration, three parts of its instruction set (guardrails, classification rules and a seven-step workflow), and the four tools it can call.

Everything here is read from the live agent, not from my notes.

**Configuration.** A cost-optimised model at temperature 0 — this is extraction and validation, not writing, so determinism is the point. Memory off and extended thinking off, both correct: every run is independent, and nothing benefits from the agent remembering the last invoice.

**Trigger.** The Outlook mailbox, polled automatically, attachments enabled. No human starts a run.

**Guardrails** come first in the instruction set, and they are why I trust it at all:

- Use only facts from the email, its attachment, or tool results.
- Never invent invoice details.
- If required information is missing or ambiguous, stop and request human review — stating exactly what is missing and why.
- Never claim success unless the API response confirms it.

**Classification rules** are refreshingly unsubtle. A PDF counts as an invoice when it contains Sold-To, Bill-To, Order Details, Billing Summary, Invoice Date, Invoice Number, Due Date or Price. An email with no attachment counts when the body contains Order#, Order Summary, Total Due, Due Date or Bill Number. Anything else is ignored.

Notice what that is *not*: "use your judgement about whether this looks like an invoice." Vague classification is where agents get expensive.

**The workflow** is seven ordered steps — classify, read the PDF, extract, validate, escalate or submit, notify, record. One line does more work than the rest combined: **the OCR call is mandatory, even when the email already contains OCR text or a summary of extracted fields.** That stops the agent trusting a convenient summary over the source document.

**Four tools**, each doing one job: find the email (Outlook, OAuth), read the PDF (Mistral, API key), create the invoice record (one-step POST), post the notification (Slack, OAuth).

---

## What it actually does

[IMAGE 5 — 05-richard-decision-flow.png]
Alt text: Richard's decision flow — an email arrives, is classified as an invoice or not, the PDF is read with OCR, six fields are extracted and validated, and the invoice is either escalated for human review or posted to the API and reported to Slack.

Count the exits in that diagram. There are five, and **two of them stop the process without touching anything**: "not an invoice, take no action", and "fields missing, escalate and do not call the API".

That ratio is the whole design. **A good agent has more ways to stop than it has ways to act.** If yours only has a happy path, you have not built an agent — you have built a pipeline that will eventually push something wrong into a system of record and be confident about it.

The validation gate is where extraction becomes trustworthy. Six fields must be present and valid before submission: invoiceNumber, invoiceDate, description, merchant, owner, amount. Date must be coercible. Amount must be numeric and at least zero. And a nice specific rule: if two or more fields are unavailable, pause for human review rather than substituting the due date for the invoice date. Someone thought about the failure mode where a plausible guess quietly becomes a wrong record.

---

## Then you iterate. It took four runs, and two failed.

[IMAGE 6 — 07-iteration-log.png]
Alt text: Four runs of iteration — run one, OCR returned nothing and the agent escalated; run two, a 404 from a mistyped endpoint and the agent reported the failure; run three, 201 Created; run four, a non-invoice email correctly ignored.

**Run 1 — OCR came back empty.** The OCR step returned nothing, and the invoice API tool was not attached yet. Richard extracted what it could from the email body, said plainly that OCR had failed, refused to submit, and asked for a human — while showing the exact payload it *would* have sent. The guardrail worked before the happy path did. That is the right order for things to start working in.

**Run 2 — a 404.** OCR read the PDF correctly. Validation passed. Then the POST went to `/api/invoice` when the endpoint is `/api/invoices`. Richard reported the failure to Slack with the payload, listed likely causes, and explicitly said the invoice had **not** been recorded.

Entirely my fault — and the design lesson is worth more than the fix. **The endpoint URL was written in the system prompt.** The agent was being asked to remember a string. Pin it inside the tool, where it cannot be retyped.

**Run 3 — 201 Created.** Same instructions, correct path. Invoice created, id returned, Slack posted. Nothing about the agent's reasoning changed between runs 2 and 3. One character was the whole gap.

**Run 4 — the negative case.** A Vanta "overdue security tasks" email landed in the same mailbox. Richard classified it as not an invoice, ran no OCR, called no API, posted no Slack noise. This matters as much as run 3. An agent that never says no will eventually submit rubbish confidently, and you will not hear about it from the agent.

Test the negative case. Ideally, test it first.

---

## The run that worked

[IMAGE 7 — 06-end-to-end-run.png]
Alt text: One successful end-to-end run in seven steps — Outlook trigger, classification, Mistral OCR, field extraction, validation, a 201 Created from the invoice API with the returned invoice id, and a Slack notification, 33 seconds in total.

A forwarded Superloop bill arrives with a three-page PDF attached. Richard classifies it as an invoice on the strength of the document containing *Tax Invoice*, *Invoice Number*, *Date of Issue*, *This Bill*, *This Bill Due* and *This Bill Summary*. Mistral OCR parses all three pages, so the fields come from the source document rather than from the email body.

Extraction: merchant *Superloop Limited*, invoiceNumber *E87296308*, invoiceDate *2026-08-08*, dueDate *2026-08-24*, amount *110.35 AUD*, description built from the actual line items — *Broadband $109.00; Card Processing Fee $1.35* — owner *Jefferson Haw*.

Validation: six of six present and valid, so no escalation. The POST returns **201 Created** with an invoice id, and the API echoes the record back. Richard posts the created invoice and the returned id to Slack.

**33 seconds. Four systems touched. Zero human steps. One Slack message so a human can check.**

Two details matter more than the speed. The description came from the *line items* on the PDF, not the total in the email — that is the mandatory-OCR instruction paying for itself. And the invoice id in the Slack message is what makes the run auditable. "The agent said it worked" is not evidence. "Here is the id the system of record returned" is.

---

## What I would do differently

None of these are about the model.

**Pin the endpoint in the tool, not the prompt.** Any value the agent has to retype is a value it can get wrong. Configuration belongs in configuration.

**Purpose-build the notification tool.** Mine was reused from a documentation-triage use case and still describes itself that way. Reuse across use cases is a real benefit of a platform approach — but a tool whose schema describes a different job will nudge the agent into filling fields with the wrong thing. Reuse the pattern, not the mismatched tool.

**Make notifications confirmable.** That tool's declared output referenced a step that does not exist in it, so successful sends returned an empty object. Messages arrived; the agent got nothing back it could assert on. That sits awkwardly beside a guardrail saying never claim success without confirmation.

**Do not trust a dev tunnel.** The homegrown API sat behind a temporary tunnel. Fine for a demo, a liability for anything else.

---

## What to do this week

1. **Name your layer.** Point solution, embedded feature, or horizontal platform — and write the reason in one sentence.
2. **Name your level.** Is the thing you want actually Level 3, or a Level 2 co-pilot with ambitions? Both are fine; confusing them is not.
3. **List the systems** the use case touches: source, reasoning, system of record, notification.
4. **Get IT to authorise the connections.** One grant per system. That is their whole part.
5. **Write the SOP.** Role and boundary, classification rule, ordered steps, output fields, escalation rule.
6. **Build from the SOP, then break it on purpose.** Feed it a document with a missing field. Feed it something that is not an invoice at all. You are testing guardrails, not the happy path.
7. **Only then run the happy path** — and check the destination system, not the agent's summary of itself.

The full write-up, all seven diagrams, and the agent's system prompt with the redacted values marked, are on GitHub:

**github.com/hawjefferson/RelevanceAI-AgenticAI-Series**

Part Three is about what comes after "it worked once": test sets, checks, and knowing when an agent is reliable enough to stop watching.

If you have built an agent that reached production — what did your first failed run teach you that the happy path never would have?

---
---

## Publishing notes (delete before posting)

**Suggested title**
> Nobody tells you the hardest part of agentic AI is choosing what to build it on

**Alternative titles**
> - Point, embedded, or horizontal: how to choose an agentic AI platform
> - I built an invoice agent from one SOP. Two of the four runs failed.
> - The four levels of AI autonomy, and why you will end up with more than one platform

**Suggested subtitle / hook line**
> How to read the AI platform market, the four levels of autonomy, and a real agent built from a single SOP — including the two runs that failed and what they taught me.

**Hashtags** (LinkedIn favours 3–5)
> #AgenticAI #AIAgents #RelevanceAI #AIImplementation #Automation

**Cover image:** `02-four-levels-of-autonomy.png` — the four levels are the idea most people have not seen laid out.

**Length:** ~2,700 words. If you want a feed post instead, the "It took four runs, and two failed" section stands alone at ~450 words with figure 7 as the image — it is the most shareable part.

**Note on figure order:** the iteration log is figure 7 in the repo but appears *before* the successful run here, because the failures are the hook. The [IMAGE n] numbering above follows this article's order, not the filenames — check you upload the file named in each marker.
