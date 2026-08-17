# build/

## `use-case-scoring-sheet.xlsx`

The scoring sheet from [the article](../README.md). Score candidate use cases against the five
gates and the value/effort inputs, and it places each one in a quadrant and ranks them.

**Four tabs:**

| Tab | What it is |
|---|---|
| **Read me** | How to use the sheet, plus the weights and thresholds as editable cells. Every formula on the other tabs reads these, so changing one re-ranks the whole list. |
| **Score use cases** | The blank template. Type in the white cells; grey cells are formulas. Row 5 is a filled example — overwrite it. |
| **Worked example** | Ten scored use cases: four build-first, three to sequence later, two capacity fillers, one to decline. |
| **Scoring guide** | Concrete 1-to-5 anchors for every input, and what a Y and an N look like for each of the five gates. |

**How the model works**

- The **five gates** (columns D–H) are answered Y or N. Five Y's means eligible to build; fewer
  means there is a specific gap to close first, and the sheet names how many.
- **Value inputs** are scored 1–5 and weighted: hours or cost released ×3, volume ×2, strategic
  pull ×2, quality or risk upside ×1.
- **Effort inputs** are scored 1–5 and weighted: process documentation maturity ×3, system
  access and integration count ×3, knowledge and data readiness ×2, owner availability ×1.
- Effort inputs are scored so **5 always means hardest**. The sheet flips the weighted total
  into an *ease* index, so a high ease index means easy to deliver.
- Both totals normalise to a 0–100 index, and one rule decides placement:
  **value ≥ threshold AND ease ≥ threshold → build first.**
- The **priority index** blends the two (65% value, 35% ease by default) so a trivial-but-easy
  task cannot outrank a valuable one. Both blend weights are editable.

**Assumptions.** The weights, thresholds and blend are a documented starting point taken from
the article, not an empirical benchmark. They encode one opinion: that documentation maturity
and system access drive delivery effort more than anything else, and that released hours or
cost drive value more than anything else. Replace them with what your own delivery history
supports. The ten example rows are illustrative and are not customer data.

---

## Conventions for anything else added here

Exported Relevance AI artifacts so a reader can import and run what an article describes.

| Kind | Filename pattern |
|---|---|
| Tool | `tool-<slug>.json` |
| Agent | `agent-<slug>.json` |
| Workforce | `workforce-<slug>.json` |
| Knowledge / sample data | `data-<slug>.csv` |

- **No secrets.** Strip API keys, tokens, OAuth account IDs and webhook URLs before exporting.
  Use `<YOUR_API_KEY>` placeholders and list what the reader must supply in the article's
  prerequisites.
- **No real customer data.** Synthetic or fully anonymised only.
- Call out any project-specific IDs a reader would otherwise have to change silently.
