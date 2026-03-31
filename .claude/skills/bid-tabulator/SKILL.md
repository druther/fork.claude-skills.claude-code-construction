---
name: bid-tabulator
description: Extract data from multiple subcontractor bid PDFs and produce a comparison spreadsheet in Excel. Use when the user has received bids for a scope of work and needs to tabulate them for analysis. Triggers on 'tabulate bids', 'bid comparison', 'compare bids', 'buyout analysis', 'bid tab', or 'bid spreadsheet'.
argument-hint: "<bid_folder_or_files>"
---

!`mkdir -p ~/.construction-skills/analytics 2>/dev/null; echo "{\"skill\":\"bid-tabulator\",\"ts\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",\"repo\":\"$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || echo "unknown")\"}" >> ~/.construction-skills/analytics/skill-usage.jsonl 2>/dev/null || true`



# Bid Tabulator

Processes multiple subcontractor bid PDFs for a scope of work and produces an Excel comparison workbook. Extracts each bid's data **as-submitted** — the engineer handles normalization and alignment after reviewing discrepancies and contacting subcontractors as needed.

## Step 1: Gather Inputs

Ask the user for:
1. **Bid PDFs** — folder path or list of individual files
2. **Scope description** — what trade/division is being bought out (e.g., "Division 09 - Finishes", "Structural Steel")
3. **Any specific data points** the user wants extracted beyond the defaults

If project context is available (`.construction/` directory), read `project.yaml` for project name/number to include in the workbook header.

## Workflow

```
Bid Tabulation Progress:
- [ ] Step 1: Gather inputs (bid PDFs, scope)
- [ ] Step 2: Read first bid to discover structure
- [ ] Step 3: Process all bids
- [ ] Step 4: Generate comparison Excel
- [ ] Step 5: Present summary to engineer
- [ ] Step 6: Write graph entry
```

### Step 2: Read First Bid to Discover Structure

Open the first bid PDF to understand what data is available:

**Try pdfplumber first:**
```python
import pdfplumber
with pdfplumber.open(bid_pdf) as pdf:
    text = pdf.pages[0].extract_text()
    if text and len(text.strip()) > 50:
        mode = "pdfplumber"
    else:
        mode = "vision"
```

**Vision fallback** for scanned bids:
```bash
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/pdf/rasterize_page.py BID.pdf 1 --dpi 200 --output bid_page.png
```

From the first bid, identify what data fields are present. Common bid data:

```yaml
# Bidder info
company_name: ""
contact_name: ""
contact_phone: ""
contact_email: ""
bid_date: ""
bid_validity_period: ""

# Financial
base_bid_amount: ""
line_items: []          # As-submitted line items with descriptions and amounts
alternates: []          # Alternate pricing (add/deduct)
unit_prices: []         # Unit price items if any
allowances: []          # Allowances included

# Terms
scope_inclusions: []    # What the bid explicitly includes
scope_exclusions: []    # What the bid explicitly excludes
qualifications: []      # Conditions, assumptions, caveats
schedule_duration: ""   # Proposed duration if stated
payment_terms: ""       # Net 30, etc.
bond_included: false    # Whether bid/performance bond is included
insurance_confirmed: false
```

**Present the discovered structure to the user** before processing remaining bids: "I found these data fields in the first bid: [list]. Should I extract all of these, or add/remove any?"

### Step 3: Process All Bids

Process each bid PDF individually. For each bid:

1. **Extract text** via pdfplumber (preferred) or vision (fallback)
2. **Quality gate**: If pdfplumber returns less than 100 characters per page, switch to vision for that bid
3. **Extract all identified fields** from the bid document
4. **Preserve original language** — do NOT paraphrase, normalize, or reformat line item descriptions. Extract them exactly as written in the bid.
5. **Flag ambiguities** — if a value is unclear or could be interpreted multiple ways, include it with a note in brackets: `[unclear: possibly $45,000 or $45/SF]`
6. **Save per-bid JSON** to `.construction/bid_tab/bids/{company_name_slug}.json`

**State persistence** — write progress after each bid:
```yaml
# .construction/bid_tab/extraction_state.yaml
scope: "Division 09 - Finishes"
total_bids: 12
processed: 5
current_bid: "Smith_Drywall.pdf"
errors: []
```

**Important:** Each bid's line items, descriptions, and amounts must be recorded exactly as submitted. Different bidders may describe the same work differently, use different units, or break out scope differently. This is expected and intentional — the engineer will reconcile after review.

### Step 4: Generate Comparison Excel

```bash
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/excel/bid_comparison_to_xlsx.py \
  --data .construction/bid_tab/bids/ \
  --scope "Division 09 - Finishes" \
  --project "Project Name" \
  --output "Bid_Comparison_Div09.xlsx"
```

**Excel workbook structure:**

**Tab 1 — Comparison Summary:**
- Row per key metric: Base Bid, Alternates (each), Bond, Duration
- Column per bidder
- Highlight: lowest base bid (green), highest (red)
- Total row at bottom

**Tab 2 — Per-Bidder Detail Tabs** (one tab per bidder):
- Company info header
- All line items as-submitted with original descriptions and amounts
- Alternates with descriptions
- Inclusions list
- Exclusions list
- Qualifications / conditions
- Any notes or special terms

**Tab 3 — Exclusions & Qualifications:**
- All bidders' exclusions and qualifications side-by-side
- This is critical for the engineer — scope gaps and risk items live here

**Tab 4 — Scope Gaps (flagged):**
- Items that appear in some bids but not others
- Items where one bidder explicitly excludes what others include
- NOT an attempt to normalize — just a flag: "Bidder A includes 'acoustical caulking', Bidders B and C do not mention it"
- The engineer decides whether this is a real gap or just different terminology

### Step 5: Present Summary to Engineer

After generating the Excel:

"I extracted data from [N] bids for [scope]. Here's the summary:

- **Lowest base bid:** [Company] at [amount]
- **Highest base bid:** [Company] at [amount]
- **Bid spread:** [amount range]
- **[X] scope gap flags** — items that appear in some bids but not others (see Scope Gaps tab)
- **[Y] qualifications/exclusions** across all bidders (see Exclusions tab)
- **[Z] bids** had unclear values that are flagged with [unclear] notes

The Excel file is at [path]. All line items are extracted as-submitted — you'll want to review the Scope Gaps tab and contact subs to clarify any discrepancies before finalizing your comparison."

### Step 6: Write Graph Entry

```bash
${CLAUDE_SKILL_DIR}/../../bin/construction-python ${CLAUDE_SKILL_DIR}/../../scripts/graph/write_finding.py \
  --type "bid_tabulation_complete" \
  --title "Bid comparison: {scope} — {N} bidders" \
  --output-file "Bid_Comparison_{scope_slug}.xlsx" \
  --data '{"scope": "Division 09", "bidder_count": 12, "low_bid": 450000, "high_bid": 680000}'
```

## Resumption

Check for `.construction/bid_tab/extraction_state.yaml`. If `status: in_progress`, resume from the next unprocessed bid.

## Tips

- Bids over 10 pages likely contain detailed breakdowns — process all pages, not just the summary
- Some bids are submitted on the owner's bid form (standardized) while others are on the sub's letterhead (freeform) — handle both
- Watch for bids that exclude tax, bonds, or general conditions — these are common scope gaps
- If a bid references "per plans and specifications dated [date]" — note the date, as it may not match the current set
- Unit prices ($/SF, $/LF, $/EA) should be extracted with their units preserved exactly
- Alternates may be add or deduct — preserve the sign as written

### File Safety
Never overwrite an existing bid comparison. If a file exists at the target location, save with a versioned name (e.g., `Bid_Comparison_Div09_v2.xlsx`).
