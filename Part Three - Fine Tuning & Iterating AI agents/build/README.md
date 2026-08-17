# build/

Exported Relevance AI artifacts for this part, so a reader can import and run exactly what the article describes.

**What goes here**

| Kind | Filename pattern | Notes |
|---|---|---|
| Tool | `tool-<slug>.json` | One file per tool |
| Agent | `agent-<slug>.json` | Include the system prompt as exported |
| Workforce | `workforce-<slug>.json` | Reference the agents it orchestrates |
| Knowledge / sample data | `data-<slug>.csv` | Synthetic or anonymised only |

**Rules**

- **No secrets.** Strip API keys, tokens, OAuth account IDs and webhook URLs before exporting. Replace with `<YOUR_API_KEY>` and note it in the article's prerequisites.
- **No real customer data.** Sample data must be synthetic or fully anonymised.
- **No project-specific IDs** left in place where a reader would have to change them silently — call them out in the article instead.
- Note in the part's `README.md` which Relevance AI region/project the export came from if it matters for import.
