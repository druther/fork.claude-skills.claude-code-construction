---
name: project-onboarding
description: Index and classify a construction project's files on first contact. Use when opening a new project folder, when asked to explore or inventory project documents, or when no sheet index exists yet. Triggers on phrases like "new project", "what is in this project", "index the drawings", or "set up the project".
disable-model-invocation: true
---

> **Behavioral context skill** — not invocable as a slash command. This skill's core patterns (AgentCM fast path, file classification, project orientation) are integrated into the parent CLAUDE.md and applied automatically via `/init` or when users ask "what's in this project?".

!`mkdir -p ~/.construction-skills/analytics 2>/dev/null; echo "{\"skill\":\"project-onboarding\",\"ts\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",\"repo\":\"$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || echo "unknown")\"}" >> ~/.construction-skills/analytics/skill-usage.jsonl 2>/dev/null || true`



# Project Onboarding

Meta-skill that runs on first contact with a construction project. Produces a project context file, file inventory, and triggers downstream indexing.

## Current Project Files
!`ls *.pdf drawings/ specs/ plans/ Drawings/ Specifications/ 2>/dev/null | head -30 || echo "No standard directories found"`

## Workflow

```
Onboarding Progress:
- [ ] Step 1: Detect data mode
- [ ] Step 2: Read or build project context
- [ ] Step 3: Inventory all files
- [ ] Step 4: Classify documents
- [ ] Step 5: Build sheet index (trigger sheet-index-builder)
- [ ] Step 6: Report summary to user
- [ ] Step 7: Write graph entry
```

### Step 1: Detect Data Mode

### Data Mode Detection — Graph-Guided Cascade

Check for `.construction/` directory in the project root. This determines your data mode:

#### AgentCM Present (graph-guided)

When `.construction/` exists, follow this cascade to build context BEFORE reading documents:

1. **Read project orientation**: `.construction/CLAUDE.md` — project name, structure, API endpoints, navigation guide
2. **Read graph summary**: `.construction/graph/graph_summary.yaml` — sheet count, view count, room count, element count, callout edge count, unresolved callouts, validation issues
3. **Query the navigation graph**: `.construction/graph/navigation_graph.json` — the primary data source. Contains the full enriched semantic network: sheets, views, rooms, elements, callout edges, note blocks, schedule tables, and grid system. All with normalized coordinates and centroids.
4. **For supplementary detail**: Read `.construction/extractions/{sheet_number}/` files when you need data not in the graph:
   - `ocr_output.json` — raw OCR text blocks with bounding boxes (large file — read only when you need specific text lookups)
   - `groups.json` — raw detected annotation groups (the unprocessed data that feeds the graph)
5. **Use this context to guide reading**: "I know room 103 is at centroid [0.35, 0.42] on sheet A-1.1 — let me rasterize and look at that specific area" or "There are 3 unresolved callouts pointing to sheet C161 — let me check if that sheet exists"

**Key data properties:**
- All coordinates are normalized 0-1. Use `--normalized` flag with `crop_region.py` to pass coordinates directly, or multiply by image pixel dimensions for other tools.
- Centroids are `[cx, cy]` tuples
- Bounding regions: `{x, y, width, height}` normalized

#### No AgentCM (unguided fallback)

Use Claude Code vision on rasterized PDFs, `pdfplumber` for text/table extraction, and `pymupdf` for PDF manipulation:

**Rasterize for vision:**
```bash
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/pdf/rasterize_page.py {pdf_path} {page} --dpi 200 --output page.png
```

**Crop specific regions:**
```bash
# With normalized 0-1 coordinates (from graph centroids/bounding regions):
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/pdf/crop_region.py page.png --box x1,y1,x2,y2 --normalized --output detail.png
# With pixel coordinates:
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/pdf/crop_region.py page.png --box x1,y1,x2,y2 --output detail.png
# Anchor-based (e.g., title block):
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/pdf/crop_region.py page.png --anchor bottom-right --width 2400 --height 1200 --output titleblock.png
```

**Extract text with pdfplumber** (works well on searchable PDFs — most architect-issued documents):
```python
import pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    text = pdf.pages[page_num].extract_text()
    tables = pdf.pages[page_num].extract_tables()
```

Without structured data, you must discover everything through these tools: scan for room tags, callout symbols, schedule tables, and cross-references manually. This works but is slower and less precise than graph-guided reading.


### AgentCM Fast Path

**If `.construction/` exists**: The platform has already extracted and indexed the project. Read these files for instant orientation:

1. `.construction/CLAUDE.md` — full project navigation guide
2. `.construction/project.yaml` — project name, number, location, calibration status
3. `.construction/index/sheet_index.yaml` — all sheets with number, title, discipline, scale, revision
4. `.construction/graph/graph_summary.yaml` — counts of sheets, views, rooms, elements, callout edges, validation issues

**Present the summary immediately** — no need to rasterize, scan, or classify. The platform has done all the heavy lifting. Then offer to:
- Read specific sheets (ask about any sheet by number)
- Extract schedules (`schedule-extractor`)
- Research building codes (`code-researcher`)
- Split specs or drawings (`spec-splitter`, `sheet-splitter`)

**Also inventory non-drawing files** that AgentCM doesn't process: specifications, submittals, RFIs, correspondence, photos. These still need classification via Step 3-4 below.

### Step 2: Read or Build Project Context (No AgentCM)

Look for a title block on the first drawing sheet you find (any PDF in a `drawings/` or `plans/` folder). Extract:
- Project name
- Project number
- Location (city, state — needed for code compliance)
- Architect / Engineer names
- Date / phase (e.g., "100% CD", "Bid Set", "Addendum 2")

Rasterize the title block region for vision:
```bash
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/pdf/rasterize_page.py {pdf_path} 1 --dpi 200 --output cover.png
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/pdf/crop_region.py cover.png --anchor bottom-right --width 1200 --height 600 --output tb_crop.png
```

Write to `.construction/project_context.yaml`.

### Step 3: Inventory All Files

Scan the project directory recursively. Catalog every file with:
- File path
- File type (PDF, DWG, DOCX, XLS, etc.)
- File size
- Parent folder name (used for classification)

### Step 4: Classify Documents

Classify each file into categories:
- **Drawings**: PDFs with sheet numbers in filenames or containing title blocks
- **Specifications**: PDFs/DOCX in `Specs/` folders or with CSI section numbers in filenames
- **Schedules**: Excel/CSV files with schedule data
- **Submittals**: PDFs in submittal folders
- **RFIs**: Documents in RFI folders
- **Other**: Correspondence, photos, reports, etc.

### Step 5: Build Sheet Index

If no AgentCM sheet index exists, trigger the `sheet-index-builder` skill to create `.construction/index/sheet_index.yaml`.

### Step 6: Report Summary

Present to user:
- Project name, number, location
- Data mode (AgentCM or vision fallback)
- Drawing count by discipline
- Spec sections identified
- Other document categories and counts
- Navigation graph summary (if AgentCM: sheet/view/room/element counts, unresolved callouts)
- Any issues found (missing sheets, unreadable files, orphaned rooms)
- Suggested next actions based on what's available

### Step 7: Write Graph Entry

```bash
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/graph/write_finding.py \
  --type "project_onboarded" \
  --title "Project onboarding completed" \
  --data '{"drawings": N, "specs": N, "disciplines": ["A","S","M","E","P"], "agentcm": true|false}'
```
