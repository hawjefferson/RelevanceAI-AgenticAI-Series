# build/

## `richard-system-prompt.md`

The instruction set Relevance AI's **Invent** capability produced from the SOP, exactly as it
stands in the live agent — 49 lines covering guardrails, classification rules and a seven-step
workflow. Swap the domain nouns and it is a working starting point for any
classify → extract → validate → submit → notify agent.

Four values are replaced with placeholders: the API host, the escalation address, the Slack
channel, and the tool action IDs (which are project-specific). The file explains what to wire
each one to, and which lines to change first if you adapt it.

## What is not here, and why

The agent and tool JSON exports are **not** published. They carry OAuth account identifiers, a
Slack channel and workspace ID, a Mistral API key reference and a private API host — and
stripping those from a raw export reliably leaves something that no longer imports cleanly. The
system prompt above plus the tool descriptions in [the article](../README.md) are enough to
rebuild the agent, and they are honest about what they are.

Four tools, if you are rebuilding it:

- **Find email in the mailbox** — Outlook connector, OAuth, one step.
- **Read the PDF with OCR** — Mistral, API key, two steps: resolve the document URL, then OCR it.
- **Create the invoice record** — one step, POST a JSON body to your invoice API. Pin the URL in
  the tool, not in the prompt.
- **Post the notification** — Slack connector, OAuth, two steps: compose the message, then send.

---

## Conventions for anything added here

Exported Relevance AI artifacts so a reader can import and run what an article describes.

| Kind | Filename pattern |
|---|---|
| Tool | `tool-<slug>.json` |
| Agent | `agent-<slug>.json` |
| Workforce | `workforce-<slug>.json` |
| Knowledge / sample data | `data-<slug>.csv` |

- **No secrets.** Strip API keys, tokens, OAuth account IDs, channel IDs and webhook URLs before
  exporting. Use `<PLACEHOLDER>` names and list what the reader must supply in the article's
  prerequisites.
- **No real customer data.** Synthetic or fully anonymised only.
- Call out any project-specific IDs a reader would otherwise have to change silently.
