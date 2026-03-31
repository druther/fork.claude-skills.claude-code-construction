# Construction Skills for Claude Code

Open source skills that make Claude Code a competent Project Engineer for construction management.

**Works standalone** — these skills use Claude Code's built-in vision and PDF tools to read any construction document. No additional platform required.

**AgentCM integration** (optional) — if you use [AgentCM](https://github.com/dleerdefi/AgentCM), skills read from pre-indexed structured data for faster, more accurate results.

> **New here?** See the [Quickstart Guide](docs/QUICKSTART.md) to try your first skill in 5 minutes.

## Quick Start

```bash
# Clone into your project's .claude/skills/ directory
git clone https://github.com/dleerdefi/claude-code-construction .claude/skills/construction

# Or install globally
git clone https://github.com/dleerdefi/claude-code-construction ~/.claude/skills/construction
```

Then run setup:

```bash
cd .claude/skills/construction  # or ~/.claude/skills/construction
./setup                         # Installs Python deps, registers skills
```

Then add to your project's `CLAUDE.md`:

```markdown
@.claude/skills/construction/CLAUDE.md
```

## How It Works

These skills follow Anthropic's [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) architecture with **progressive disclosure**: Claude loads only what each task requires.

### Two Operating Modes

**With AgentCM** (structured data): Skills read from the `.construction/` directory — pre-indexed sheets, parsed specs, OCR annotations, resolved cross-references. Fast and token-efficient.

**Without AgentCM** (vision fallback): Skills use Claude Code's vision capabilities on rasterized PDFs plus `pdfplumber` for text extraction. Slower but fully functional. The `sheet-index-builder` skill creates a local index to accelerate subsequent operations.

### Graph Context Retention

Every skill outputs structured findings to `.construction/agent_findings/` so that:
- Future queries can traverse prior work product
- Marked-up drawings, RFIs, takeoffs, and extractions persist across sessions
- The knowledge graph grows as Claude contributes findings and completes tasks

## Skills

| Skill | Description |
|---|---|
| `project-onboarding` | Index a project, classify files, establish context |
| `sheet-index-builder` | Build navigable drawing sheet index via vision + title blocks |
| `sheet-splitter` | Split bound drawing set into individual sheet PDFs |
| `spec-splitter` | Split bound project manual into individual spec section PDFs |
| `spec-parser` | Parse spec sections, extract submittal/product requirements |
| `schedule-extractor` | Extract structured schedule data from drawings or specs |
| `submittal-log-generator` | Extract submittal requirements from specs (DRAFT — engineer review required) |
| `bid-tabulator` | Tabulate multiple subcontractor bids into comparison spreadsheet |
| `code-researcher` | Deep research on building codes, standards, and jurisdiction requirements |
| `subcontract-writer` | Generate scope-specific subcontract from firm's template |

## Repository Structure

```
construction-skills/
├── CLAUDE.md                              # Development orchestrator
├── README.md
├── requirements.txt
├── setup                                  # Installation script
├── conductor.json                         # Lifecycle hooks
├── .claude/
│   └── skills/
│       ├── CLAUDE.md                      # Runtime orchestrator (import this)
│       ├── project-onboarding/SKILL.md
│       ├── sheet-index-builder/SKILL.md
│       ├── sheet-splitter/SKILL.md
│       ├── spec-splitter/SKILL.md
│       ├── spec-parser/SKILL.md
│       ├── schedule-extractor/SKILL.md
│       ├── submittal-log-generator/SKILL.md
│       ├── bid-tabulator/SKILL.md
│       ├── code-researcher/SKILL.md
│       └── subcontract-writer/SKILL.md
├── reference/
│   ├── csi_masterformat.yaml
│   ├── drawing_conventions.md
│   ├── common_abbreviations.yaml
│   ├── scale_factors.yaml
│   ├── ada_requirements.yaml
│   └── ibc_egress_tables.yaml
├── scripts/
│   ├── pdf/
│   ├── vision/
│   ├── excel/
│   ├── bulk/
│   └── graph/
├── evals/
│   ├── EVAL_SPEC.md
│   ├── test_docs/
│   ├── cases/
│   ├── runners/
│   └── results/
└── templates/
    ├── graph_entry.yaml
    ├── project_context.yaml
    ├── sheet_index.yaml
    ├── rfi_template.md
    ├── submittal_register.yaml
    └── takeoff_template.yaml
```

## Long-Running Skills

**`submittal-log-generator`** is designed as a background process that can run for extended periods. It parses every specification section to extract submittal requirements, using pdfplumber for text extraction with vision fallback for scanned documents. A state file at `.construction/submittal_extraction_state.yaml` enables resumption after interruption.

## Local Analytics

Every skill invocation is logged locally to `~/.construction-skills/analytics/skill-usage.jsonl`. No data is sent externally. View your usage:

```bash
bin/construction-analytics              # Full summary
bin/construction-analytics --top        # Top 10 skills
bin/construction-analytics --recent 7   # Last 7 days
```

## PDF Annotations

Skills produce real PDF annotation objects (via PyMuPDF) that are viewable in Bluebeam, Adobe, and any standard PDF reader. The annotation script writes circles, rectangles, clouds, text labels, stamps, and polygons as non-destructive annotation layer objects — not raster overlays.

## Evaluations

The `evals/` directory contains a test framework for validating skills against real construction documents. See `evals/EVAL_SPEC.md` for the full specification.

## Requirements

**Python 3.10+** (core) — installed into an isolated venv at `~/.construction-skills/venv/`:
- `pdfplumber` — PDF text/table extraction
- `pymupdf` (fitz) — PDF annotation read/write, rasterization
- `openpyxl` — Excel output
- `Pillow` — Image processing and cropping
- `PyYAML` — YAML read/write

The `./setup` script automatically creates the venv and installs dependencies. All skill scripts invoke Python through `bin/construction-python`, which transparently uses the venv interpreter — no manual activation needed.

## License

MIT
