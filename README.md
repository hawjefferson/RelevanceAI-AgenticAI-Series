# Relevance AI — Agentic AI Series

A practical, hands-on series on designing, building and running **agentic AI workflows** with [Relevance AI](https://relevanceai.com).

Each part is a self-contained article plus the artifacts you need to rebuild what it describes — exported tools, agents and workforces you can import into your own Relevance AI project and run.

---

## Who this is for

- **Operators and domain experts** who own a process and want to know whether an agent should run it.
- **Builders** who are comfortable in Relevance AI (or want to be) and want patterns that hold up in production.
- **Leaders** trying to separate genuine agentic use cases from things a spreadsheet or a single prompt already solves.

No prior agent-building experience is assumed. Later parts get progressively more technical.

---

## Prerequisites

| What | Why |
|---|---|
| A [Relevance AI](https://relevanceai.com) account (free tier is enough to start) | To import and run the exported tools and agents |
| Basic familiarity with LLM prompting | The articles explain agentic concepts, not prompting from zero |
| Credentials for any third-party system a part uses | Some parts connect to email, CRM or a data source — each part lists exactly what it needs |

---

## The series

| # | Part | What it covers | Status |
|---|---|---|---|
| 1 | [What makes a use case good for Agentic AI](./Part%20One%20-%20What%20makes%20a%20use%20case%20good%20for%20Agentic%20AI/) | Choosing the right first use case — and recognising the ones that shouldn't be agentic at all. Includes a [scoring sheet](./Part%20One%20-%20What%20makes%20a%20use%20case%20good%20for%20Agentic%20AI/build/use-case-scoring-sheet.xlsx). | ✅ Written |
| 2 | [Building AI Agents within Relevance AI](./Part%20Two%20-%20Building%20AI%20Agents%20within%20Relevance%20AI/) | Taking a chosen use case and building the agent: tools, prompts, knowledge, running it | 📋 Planned |
| 3 | [Fine Tuning & Iterating AI agents](./Part%20Three%20-%20Fine%20Tuning%20&%20Iterating%20AI%20agents/) | Making a working agent reliable — evaluating, debugging and improving it over time | 📋 Planned |

> **Ideas for later parts** (not committed to — edit freely): multi-agent workforces, triggers and
> unattended runs, observability and cost control in production, integrating agents into existing systems.

---

## How each part is laid out

Every part folder follows the same shape:

```
Part <Number> - <Readable Title>/
├── README.md      ← the article; renders automatically when you open the folder on GitHub
├── linkedin.md    ← the same article reshaped for the LinkedIn article editor
├── assets/        ← figures referenced by the article (PNG for portability, SVG sources)
└── build/         ← exported Relevance AI tools and agents, and any companion assets
```

To follow along with a part: read its `README.md`, then import anything in `build/` into your own Relevance AI project.

---

## Adding a new part

Copy [`_template/`](./_template/), rename it to `Part <Number> - <Readable Title>`, and fill in the skeleton. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full conventions.

---

## License

See [LICENSE](./LICENSE).
