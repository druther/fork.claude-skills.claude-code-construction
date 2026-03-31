---
name: code-researcher
description: >
  Scope-specific code gap analysis for engineers and architects. Given one or
  more project scopes (spec sections, drawing sets, or trade packages), this
  skill extracts what codes and standards the scope already references, researches
  what codes should apply based on the work type and jurisdiction, and surfaces
  only the delta — requirements that should apply but are not addressed in the
  project documents. Outputs a structured gap report with engineer-actionable
  items, confidence levels, and direct references to the plans and specs.

  Use when: an engineer or architect wants to know if they are missing any code
  requirements for a specific scope of work.

  Triggers: "code research", "what codes apply", "am I missing any requirements",
  "code check", "ADA requirements", "egress", "fire code", "what does the code
  say about X", "code gap analysis", "are we covered on X".
argument-hint: "<scope_or_question> e.g. 'Section 09 67 23 resinous flooring' or 'egress from the kitchen complex'"
---

!`mkdir -p ~/.construction-skills/analytics 2>/dev/null; echo "{\"skill\":\"code-researcher\",\"ts\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",\"repo\":\"$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || echo "unknown")\"}" >> ~/.construction-skills/analytics/skill-usage.jsonl 2>/dev/null || true`

# Code Researcher — Scope-Specific Gap Analysis

## What This Skill Does

An engineer managing one or more scopes asks: *"Are there any code requirements
for this scope that I'm missing?"*

This skill answers that question in three passes:

**Pass 1 — What the scope already addresses**
Read the actual project documents — spec sections, drawings, schedules — and
extract every code citation, standard reference, and requirement already
incorporated by the design team.

**Pass 2 — What should apply**
Research all codes and standards that apply to this type of work in this
jurisdiction, regardless of what the project documents say.

**Pass 3 — The gap**
Diff Pass 1 against Pass 2. Present only what's in Pass 2 but absent from
Pass 1, with confidence levels and specific source citations from both the
code and the project documents.

**This is a gap finder, not a code summary.** If the spec already addresses a
requirement correctly, it does not appear in the output. The engineer's time is
spent only on things that may actually be missing.

---

## Framing Rule (Non-Negotiable)

Every finding is framed as:
> *"Code [X] requires [Y]. The project documents [address this at / do not
> appear to address this]. Confidence: [level]. Recommended action: [action]."*

Never frame findings as COMPLIANT / NON-COMPLIANT. The licensed design
professional makes compliance determinations. This skill provides research.

---

## Workflow Overview

```
Phase 1 — Context and Scope Definition
  1a  Gather project context (jurisdiction, occupancy, construction type)
  1b  Define the research scope (which spec sections, which question)
  1c  USER CHECKPOINT — confirm scope before any research begins

Phase 2 — Project Document Extraction (Pass 1)
  2a  Read all project documents in scope
  2b  Extract every code citation, standard reference, requirement
  2c  Build the "already addressed" inventory

Phase 3 — Code Research (Pass 2)
  3a  Research jurisdiction and adopted code editions
  3b  Research applicable requirements for this scope and work type
  3c  USER CHECKPOINT — interim findings, confirm continuation

Phase 4 — Gap Analysis (Pass 3)
  4a  Diff research findings against project document inventory
  4b  Classify each gap by severity and confidence
  4c  USER CHECKPOINT — review gaps before report is written

Phase 5 — Report
  5a  Generate structured gap report
  5b  Write graph entry
```

**Human checkpoints at 1c, 3c, and 4c.** Do not skip them.

---

## Phase 1 — Context and Scope Definition

### 1a — Gather Project Context

Collect minimum required project parameters. Check in this order:

**AgentCM project files (if `.construction/` exists):**
- `.construction/project.yaml` — location, occupancy, construction type
- `.construction/index/sheet_index.yaml` — drawing set composition
- `.construction/graph/navigation_graph.json` — rooms, elements

**Project documents (read directly):**
- Architectural title block — project name, location, jurisdiction
- Spec Section 01 10 00 (Summary of Work) — occupancy, construction type,
  project description
- Spec Section 01 40 00 (Quality Requirements) — codes the design team has
  already identified as applicable
- Spec Section 01 35 13 or 01 35 14 — special project requirements, authority
  having jurisdiction contacts

Minimum required context:

```yaml
project_context:
  project_name: ""
  location:
    address: ""
    city: ""
    county: ""
    state: ""
  occupancy_group: ""         # IBC occupancy group(s), e.g. E, B, A-2, I-2
  construction_type: ""       # IBC construction type, e.g. Type IIA, VB
  project_type: ""            # new construction | renovation | addition | change of use
  building_height_stories: 0
  building_gross_area_sf: 0
  sprinklered: null           # true | false | partial | unknown
  year_of_design: ""          # infer from drawing date — determines code edition
  ahj:                        # Authority Having Jurisdiction
    building_department: ""
    fire_marshal: ""
    contact: ""               # if found in docs
```

If any required field cannot be found in the documents, ask the user before
proceeding. Do not assume occupancy group or construction type — these
determine which code provisions apply and an incorrect assumption cascades
through the entire analysis.

### 1b — Define the Research Scope

Parse the user's question to identify:

1. **Target scope** — which spec sections, drawing sheets, systems, or elements
   the engineer wants checked. Examples:
   - A spec section: "Section 09 67 23 Resinous Flooring"
   - A system: "all egress paths from the kitchen complex"
   - A trade package: "mechanical scope, Sections 23 00 00 through 23 80 00"
   - A code topic: "accessibility requirements for the toilet rooms"

2. **Research question** — what specifically the engineer is worried about.
   Examples:
   - "Am I missing any code requirements?"
   - "Does the spec cover the slip resistance requirements?"
   - "Are there fire separation requirements I haven't addressed?"

3. **Scopes in scope** — if the engineer is managing multiple scopes (e.g.,
   scopes A through C), confirm which ones this research covers.

Write to `.construction/code_research/scope_definition.yaml`:

```yaml
research_question: "Are there code requirements for resinous flooring that we haven't addressed?"
target_scope:
  spec_sections:
    - "09 67 23"               # primary section
    - "09 65 00"               # related sections if relevant
  drawing_sheets: []           # specific sheets if named
  systems: []                  # systems if question is system-based
  scope_packages: ["Scope C"]  # if engineer uses package designations
engineer_scopes: ["A", "B", "C"]  # all scopes the engineer manages

research_topics:
  # Generated from the target scope and project context — not hardcoded
  # These are discovered, not prescribed
  - slug: ""
    title: ""
    description: ""
    driven_by: ""  # what about the scope triggers this topic
```

Research topics are generated from the combination of:
- The work type (resinous flooring → surface profile requirements, slip
  resistance, chemical resistance, substrate preparation)
- The occupancy group (kitchen/food service → USDA/FDA/health department overlay)
- The project type (renovation → existing conditions, special inspections)
- The question framing (gap analysis → broader research than targeted check)

### 1c — USER CHECKPOINT: Confirm Scope

Present to the user:

```
I have enough context to start. Before I begin research, here's what I'm planning:

PROJECT
  Name:          [project_name]
  Location:      [city, state]
  Occupancy:     [group]
  Type:          [construction type]
  Sprinklered:   [yes/no/unknown]
  Code year:     [inferred from drawing date]

SCOPE I'LL RESEARCH
  Spec sections: [list]
  Sheets:        [list, or "none specified — I'll search for relevant sheets"]
  Your question: [restated in plain language]

RESEARCH TOPICS I'VE IDENTIFIED
  1. [topic] — because [reason derived from scope]
  2. [topic] — because [reason derived from scope]
  3. [topic] — because [reason derived from scope]
  [...]

TOPICS I'M NOT INCLUDING (and why)
  • [topic] — not applicable to this occupancy/type
  • [topic] — already confirmed complete by Spec 01 40 00

Before I spend time researching, please confirm:
  • Is the project context correct?
  • Should I add or remove any research topics?
  • Are there specific code concerns you already have that I should prioritize?
```

**Do not begin Phase 2 until the user responds.**

---

## Phase 2 — Project Document Extraction (Pass 1)

This phase reads what the project documents already say. It runs before web
research so the gap analysis has a firm baseline.

### 2a — Read All In-Scope Documents

For each spec section in scope:
- Read the full section (all parts — General, Products, Execution)
- Use pdfplumber for text-layer PDFs; use vision for scanned or image-heavy pages

For drawing sheets:
- Read title block, notes, schedules, and details relevant to the scope
- Use vision for plan sheets; extract text from schedules if text-layer

For referenced standards within spec sections:
- Note every standard cited (ASTM, ANSI, NFPA, UL, SMACNA, etc.) with its
  edition year as cited in the spec

### 2b — Extract All Code and Standard Citations

For each document read, extract every code reference, standard citation, and
requirement into a structured inventory:

```yaml
# .construction/code_research/pass1_project_inventory.yaml

source_documents_read:
  - path: "specs/09_67_23_resinous_flooring.pdf"
    type: "spec_section"
    section: "09 67 23"
    pages_read: "all"

code_citations_found:
  - citation: "ASTM C 579"
    context: "Compressive strength testing method — 09 67 23 §2.1-D-1"
    edition_specified: "current"
    how_cited: "test method for physical property compliance"

  - citation: "ASTM F 1869"
    context: "Moisture vapor emission rate testing — 09 67 23 §3.1-B-3"
    edition_specified: null
    how_cited: "substrate acceptance criterion (max 7 lb/1000 sf/24hr)"

  - citation: "ACI 503R"
    context: "Bond strength requirement — 09 67 23 §2.1-D-10"
    edition_specified: null
    how_cited: "bond strength test method (400 psi minimum)"

requirements_stated:
  - topic: "installer qualification"
    requirement: "Certified in writing by resinous flooring manufacturer"
    source: "09 67 23 §1.3-B-1"
    code_basis: null  # project-imposed requirement, not code-derived

  - topic: "substrate preparation"
    requirement: "Shot-blast surfaces per manufacturer instructions"
    source: "09 67 23 §3.1-B-1-a"
    code_basis: null

  - topic: "vapor barrier"
    requirement: "Vapor barrier must be present for slabs on or below grade"
    source: "09 67 23 §1.5-C"
    code_basis: null

  - topic: "slip resistance"
    requirement: null  # NOT FOUND in spec — this becomes a potential gap
    source: null
    code_basis: null
    note: "No slip resistance requirement found in 09 67 23 or related sections"

topics_not_addressed:
  # Pre-populate this during extraction — anything the researcher expects
  # to see in a spec section of this type but didn't find
  - "slip resistance / coefficient of friction"
  - "VOC content limitations"
  - "health department requirements"
  - "fire classification / flame spread"
```

**Critical extraction discipline:**
- Record what IS there (citations found, requirements stated)
- Also record what is ABSENT that you would expect to find
- Do not interpret absence as compliance — absence is a potential gap
- Note edition years as specified — a correct requirement cited against the
  wrong edition is a potential gap

### 2c — Build the "Already Addressed" Inventory

Summarize Pass 1 into a flat inventory used for gap diffing in Phase 4:

```yaml
# .construction/code_research/pass1_summary.yaml

topics_addressed:
  compressive_strength:
    addressed: true
    by: "ASTM C 579 cited in 09 67 23 §2.1-D-1"
    gap_risk: low

  moisture_testing:
    addressed: true
    by: "ASTM F 1869 and ASTM F 2170 both cited"
    gap_risk: low

  installer_qualification:
    addressed: true
    by: "Manufacturer written cert required per §1.3-B-1"
    gap_risk: low

  slip_resistance:
    addressed: false
    by: null
    gap_risk: high    # food service/kitchen = high-traffic, wet, regulatory

  voc_content:
    addressed: false
    by: null
    gap_risk: medium  # Div 01 may cover this globally

  flame_spread:
    addressed: false
    by: null
    gap_risk: medium

  health_department_overlay:
    addressed: false
    by: null
    gap_risk: high    # kitchen complex = AHJ may include health dept
```

---

## Phase 3 — Code Research (Pass 2)

### 3a — Research Jurisdiction and Adopted Codes

Before researching requirements, establish which edition of each code is
adopted by the jurisdiction. This is non-negotiable — code requirements
vary significantly between editions.

Search for:
```
"{state} building code adopted edition {year}"
"{city} {state} local building code amendments"
"{state} IBC adoption effective date"
"{state} fire code adopted edition"
"{state} accessibility code requirements"
```

Write to `.construction/code_research/jurisdiction.yaml`:

```yaml
state: ""
jurisdiction: ""
adopted_codes:
  building_code:
    name: ""            # IBC, or state-specific (CBC, NYC Building Code, etc.)
    edition: 0          # year, e.g. 2021
    adoption_date: ""
    state_amendments: ""
    local_amendments: ""
    source: ""          # URL where this was verified

  fire_code:
    name: ""
    edition: 0
    source: ""

  accessibility:
    federal: "ADA 2010 Standards"
    state_code: ""      # if state has additional requirements
    exceeds_ada: null
    source: ""

  referenced_standards:
    # Which editions of NFPA, ANSI, ASCE, etc. are adopted
    # via the building code reference chain
    - name: ""
      edition: 0
      adopted_via: ""   # e.g. "IBC 2021 Chapter 35"

confidence: ""          # confirmed | inferred | uncertain
confidence_notes: ""
```

If jurisdiction code adoption cannot be confirmed via web search, mark as
`uncertain` and note this prominently in the report. Do not assume the latest
published edition is what's adopted.

### 3b — Research Requirements for Each Topic

For each topic in the confirmed research outline, research what the applicable
codes require. Work through topics in batches of 2-3.

**For each topic:**

1. Search for code requirements specific to this work type, occupancy, and
   construction type:
   ```
   "{code name} {edition} {topic keyword} {occupancy group}"
   "{code name} {edition} {topic keyword} {work type}"
   ```

2. Fetch specific code sections when a section number is identified, to
   get exact requirement language rather than paraphrases.

3. Check for referenced standards that the code directs to for this topic.

4. Check for jurisdiction-specific overlays:
   ```
   "{state} requirements {topic keyword}"
   "{city} {state} {topic keyword} requirements"
   "AHJ requirements {topic keyword} {state}"
   ```

5. For topics involving health departments, USDA, FDA, or other regulatory
   bodies (food service, healthcare, hazardous materials), search those
   authorities separately — they operate independently of the building code.

Write to `.construction/code_research/topics/{slug}.yaml`:

```yaml
topic: "Slip Resistance"
research_findings:
  - code: "ADA 2010 Standards"
    section: "402.2"
    requirement: "Floor or ground surfaces shall be stable, firm, and slip resistant"
    specific_to_this_scope: true
    edition_confirmed: true
    source_url: ""

  - code: "IBC 2021"
    section: "1210.3"
    requirement: "Floor surfaces in commercial kitchens shall have a static
                  coefficient of friction of not less than 0.60"
    specific_to_this_scope: true
    edition_confirmed: true
    source_url: ""

  - code: "ASTM C 1028 / DCOF AcuTest"
    section: null
    requirement: "Test method for measuring slip resistance — DCOF ≥ 0.42
                  commonly referenced for wet floors"
    specific_to_this_scope: true
    edition_confirmed: false
    source_url: ""
    note: "ASTM C 1028 withdrawn 2014; DCOF AcuTest per ANSI A137.1 now standard
           for tile, but resinous flooring has no equivalent standard — verify
           what test method AHJ requires"

  - code: "USDA/FDA Food Service Requirements"
    section: null
    requirement: "Floors in food preparation areas must be non-slip; specific
                  requirements vary by state health department"
    specific_to_this_scope: true
    edition_confirmed: false
    source_url: ""
    note: "Maryland Department of Health has food service facility regulations —
           project kitchen (Rooms 1411-1419) likely subject to these"

applicable_test_standards:
  - "DCOF AcuTest per ANSI A137.1 (tile)"
  - "No industry standard specific to urethane mortar systems — manufacturer
     test data typically used"

gaps_identified:
  - "No COF or slip resistance requirement in 09 67 23"
  - "No test method for slip resistance specified"
  - "No mention of food service/health department requirements despite
     scope including kitchen complex"
```

### 3c — USER CHECKPOINT: Interim Findings

After each batch of 2-3 topics, report to the user:

```
Completed research on [topic 1], [topic 2], and [topic 3].

PRELIMINARY GAPS IDENTIFIED SO FAR
  ⚠  HIGH   Slip resistance — no COF requirement found in spec; IBC §1210.3
             and ADA require slip-resistant floors in kitchens and ADA paths
  ⚠  HIGH   Health department overlay — kitchen complex may be subject to
             Maryland Dept. of Health food service regs; not mentioned in scope
  ○  MEDIUM  VOC content — 09 67 23 does not cite VOC limits; Division 01
             may address this globally (will check)

NO GAP (already addressed in spec)
  ✓  Moisture testing — ASTM F 1869 and F 2170 both required (§3.1-B)
  ✓  Compressive strength — ASTM C 579 requirement at 7,700 psi (§2.1-D)
  ✓  Bond strength — ACI 503R at 400 psi (§2.1-D-10)

UNCERTAIN (couldn't confirm code language)
  ?  Baltimore City amendments to IBC §1210 — could not confirm if local
     amendments modify the slip resistance requirement

Continuing with [next batch]: [topic 4], [topic 5].
Do you want me to dig deeper on any of these before continuing, or shall I proceed?
```

---

## Phase 4 — Gap Analysis (Pass 3)

### 4a — Diff Research Against Project Inventory

Compare every research finding from Phase 3 against the Pass 1 project
inventory. Classify each:

```yaml
# .construction/code_research/gap_analysis.yaml

gaps:
  - id: "GAP-001"
    topic: "Slip Resistance"
    severity: HIGH
    confidence: confirmed
    
    code_requirement:
      code: "IBC 2021 §1210.3"
      text: "Floor surfaces in commercial kitchens shall have a static
             coefficient of friction of not less than 0.60"
    
    project_status:
      addressed: false
      in_documents: null
      note: "09 67 23 specifies physical properties (compressive strength,
             bond strength, hardness) but contains no COF or slip resistance
             requirement. No reference to slip resistance test method."
    
    recommended_action: "Add COF requirement to 09 67 23 §2.1 System
                         Characteristics and specify test method. Verify with
                         manufacturer what COF their system achieves wet."
    
    engineer_action_required: true
    pe_decision_required: false   # factual gap, not an interpretation

  - id: "GAP-002"
    topic: "Health Department Requirements — Kitchen Complex"
    severity: HIGH
    confidence: needs_review
    
    code_requirement:
      code: "Maryland Department of Health Food Service Facility Regs
             (COMAR 10.15.03)"
      text: "Floors in food preparation areas shall be smooth, easily cleanable,
             and nonabsorbent"
    
    project_status:
      addressed: false
      in_documents: null
      note: "Kitchen complex (Rooms 1411–1419) is within the resinous flooring
             scope. No reference to health department requirements or COMAR
             10.15.03 found in 09 67 23 or in project manual."
    
    recommended_action: "Confirm with Owner whether food service permit is
                         required. If yes, coordinate with health department
                         AHJ on floor system acceptability before spec is
                         finalized."
    
    engineer_action_required: true
    pe_decision_required: true   # requires AHJ coordination

  - id: "GAP-003"
    topic: "VOC Content Limitations"
    severity: MEDIUM
    confidence: confirmed
    
    code_requirement:
      code: "IBC 2021 §1210.2 (via Section 01 61 16)"
      text: "VOC content of floor coatings shall comply with applicable
             regulations"
    
    project_status:
      addressed: partial
      in_documents: "Spec 01 61 16 — VOC Content Restrictions references
                     limits; 09 67 23 §1.5-C references vapor barrier but
                     does not reference 01 61 16 or state VOC limits"
      note: "Division 01 likely covers this globally. Confirm that 09 67 23
             is governed by 01 61 16 and that the resinous system products
             meet those limits."
    
    recommended_action: "Add cross-reference to Section 01 61 16 in 09 67 23
                         §1.1 or §1.5. Confirm manufacturer's VOC data for
                         Stonclad UT system against limits in 01 61 16."
    
    engineer_action_required: false
    pe_decision_required: false

already_addressed:
  - topic: "Moisture Vapor Emission Testing"
    addressed_by: "ASTM F 1869 and ASTM F 2170 both cited in §3.1-B-3 with
                   specific limits (7 lb/1000 sf/24hr and 85% RH)"
    confidence: confirmed
    note: "Well covered. Both test methods included."

  - topic: "Substrate Preparation"
    addressed_by: "Shot-blast requirement per §3.1-B-1-a; self-priming
                   noted; patching material specified"
    confidence: confirmed

uncertain:
  - topic: "Baltimore City Amendments to Slip Resistance"
    note: "Could not confirm whether Baltimore City has local amendments
           that modify IBC §1210.3. Recommend confirming with building
           department AHJ."
    recommended_action: "Call Baltimore City building department or consult
                         project architect who should have local amendment
                         knowledge."
```

### 4b — Classify Each Gap

Each gap gets a severity and confidence rating:

**Severity:**
- `HIGH` — a code requirement clearly applies, is not addressed in the project
  documents, and creates regulatory or safety risk if unresolved
- `MEDIUM` — a code requirement likely applies but may be addressed elsewhere
  (e.g., in a Division 01 section not yet reviewed) or its applicability
  depends on a condition that hasn't been confirmed
- `LOW` — a code reference that could be added for completeness but whose
  absence is unlikely to cause a compliance issue

**Confidence:**
- `confirmed` — the code requirement is definitively established (correct
  jurisdiction, correct edition, correct applicability) and the project
  document status is definitively established (read the full section)
- `needs_review` — the requirement likely applies but requires information
  not available in the current documents (AHJ confirmation, additional spec
  sections not provided, etc.)
- `uncertain` — conflicting sources, could not confirm jurisdiction's
  adopted code edition, or the code's applicability to this specific scope
  is genuinely ambiguous

### 4c — USER CHECKPOINT: Review Gaps Before Report

Before generating the report, present the gap summary:

```
GAP ANALYSIS COMPLETE

HIGH-CONFIDENCE GAPS (take action)
  GAP-001 ⚠ HIGH    Slip resistance — no COF requirement in 09 67 23
                     IBC §1210.3 requires 0.60 COF in commercial kitchens
                     Recommended action: add COF requirement and test method

  GAP-002 ⚠ HIGH    Health department — kitchen complex not addressed
                     Maryland COMAR 10.15.03 may apply; needs AHJ confirmation
                     Recommended action: confirm with Owner whether food
                     service permit required

MEDIUM-CONFIDENCE GAPS (confirm and close)
  GAP-003 ○ MEDIUM   VOC content — 09 67 23 may need cross-ref to 01 61 16
                      Likely covered globally; confirm and add cross-reference

UNCERTAIN (need more information)
  ?  Baltimore City amendments to slip resistance — couldn't confirm locally

ALREADY ADDRESSED (no action needed)
  ✓  Moisture vapor emission testing — well covered, both test methods
  ✓  Substrate preparation — shot-blast, priming, patching all specified
  ✓  Compressive strength — ASTM C 579 at 7,700 psi
  ✓  Bond strength — ACI 503R at 400 psi
  ✓  Installer qualification — manufacturer written cert required

Before I write the report:
  • Are any of these gaps ones you were already aware of and have addressed
    outside the documents I reviewed?
  • Should I research any topic further before finalizing?
  • Any gaps you want to remove from the report?
```

---

## Phase 5 — Report

### 5a — Generate Gap Report

Write to `.construction/code_research/report_{scope}_{date}.md`:

```markdown
# Code Gap Analysis Report

**Scope Researched:** Section 09 67 23 — Resinous Flooring (Kitchen Complex)
**Engineer's Question:** Are there code requirements for this scope that are missing?
**Project:** [Name] | [City, State] | [Date]
**Occupancy:** [Group] | **Construction Type:** [Type] | **Sprinklered:** [Yes/No]
**Prepared:** [ISO date]

---

## Applicable Codes (Jurisdiction Confirmed)

| Code | Edition | Adopted By |
|------|---------|-----------|
| [Code name] | [year] | [jurisdiction, date] |
| ... | ... | ... |

---

## Gaps — Action Required

### GAP-001 · HIGH · Confirmed
**Topic:** Slip Resistance
**Code Requirement:** IBC 2021 §1210.3 — Floor surfaces in commercial kitchens
shall have a static coefficient of friction ≥ 0.60.
**Project Status:** Not addressed. Section 09 67 23 specifies physical properties
(compressive strength, bond strength, Shore D hardness) but contains no COF or
slip resistance requirement and no test method reference.
**Recommended Action:** Add minimum COF = 0.60 (wet) to 09 67 23 §2.1 System
Characteristics. Specify test method (coordinate with manufacturer — no industry
standard exists for urethane mortar systems; manufacturer test data typically
used). Confirm AHJ accepts manufacturer-provided test data.
**Engineer Decision Required:** No (factual addition to spec)
**PE/Architect Decision Required:** No (factual addition to spec)

### GAP-002 · HIGH · Needs Review
**Topic:** Health Department Overlay — Kitchen Complex
**Code Requirement:** Maryland COMAR 10.15.03 (Food Service Facility Regulations)
— floors in food preparation areas shall be smooth, easily cleanable, and
nonabsorbent. Specific requirements may require AHJ pre-approval of floor system.
**Project Status:** Not addressed. Rooms 1411–1419 (kitchen complex) are within
the resinous flooring scope. No reference to health department requirements found
in 09 67 23 or in the project manual.
**Recommended Action:** Confirm with Owner whether a food service permit is
required for the kitchen complex. If yes, coordinate with Maryland Department of
Health AHJ before spec is finalized. Obtain written approval of the Stonhard
Stonclad UT system from the health department, or identify an alternative system
that has prior approval.
**Engineer Decision Required:** Yes — confirm permit requirement with Owner
**PE/Architect Decision Required:** Yes — AHJ coordination and possible system substitution

---

## Gaps — Confirm and Close

### GAP-003 · MEDIUM · Confirmed
**Topic:** VOC Content Cross-Reference
**Code Requirement:** IBC 2021 §1210.2 and project Spec 01 61 16 establish
VOC content limits for floor coatings applied within the building envelope.
**Project Status:** Partial. Division 01 Section 01 61 16 addresses VOC limits
globally, but Section 09 67 23 does not reference 01 61 16 and does not
independently state VOC limits for the Stonclad UT system components.
**Recommended Action:** Add cross-reference to Section 01 61 16 in 09 67 23
§1.1 or §2.1. Obtain VOC content documentation from Stonhard for all system
components and confirm compliance with limits in 01 61 16.
**Engineer Decision Required:** No (administrative cross-reference)

---

## Uncertain — Requires AHJ Confirmation

| Item | Question | Who Confirms |
|------|----------|-------------|
| Baltimore City amendments to slip resistance | Does Baltimore City have local amendments that modify IBC §1210.3? | Building department AHJ |

---

## Already Addressed — No Action Needed

| Topic | How Addressed | Source |
|-------|---------------|--------|
| Moisture vapor emission testing | ASTM F 1869 (max 7 lb/1000 sf/24hr) and ASTM F 2170 (max 85% RH) both required | 09 67 23 §3.1-B-3 |
| Substrate preparation | Shot-blast per manufacturer; self-priming; patching material specified | 09 67 23 §3.1-B |
| Compressive strength | ASTM C 579 at 7,700 psi after 7 days | 09 67 23 §2.1-D-1 |
| Bond strength | ACI 503R at 400 psi minimum, 100% concrete failure | 09 67 23 §2.1-D-10 |
| Installer qualification | Manufacturer written certification required before production | 09 67 23 §1.3-B-1 |

---

## Documents Reviewed

| Document | Type | Pages / Sheets |
|----------|------|---------------|
| Spec Section 09 67 23 | Specification | Full section |
| Spec Section 01 61 16 | Specification | §1.1, §2.1 |
| Drawing A-3.1 | Finish Schedule | Full sheet |
| [any other documents read] | | |

---

## Disclaimer

This report presents code research findings for informational purposes only.
Gap identifications are based on the documents reviewed and web research
conducted on [date]. All findings require review and confirmation by the
licensed design professional of record. Code interpretations and compliance
determinations are the responsibility of the Architect and Engineer of Record.
Confirm jurisdiction-specific code adoptions and local amendments with the
Authority Having Jurisdiction before finalizing design documents.
```

### 5b — Write Graph Entry

```bash
${CLAUDE_SKILL_DIR}/../../bin/construction-python \
  ${CLAUDE_SKILL_DIR}/../../scripts/graph/write_finding.py \
  --type "code_gap_analysis" \
  --title "Code gap analysis: {scope} — {n_gaps} gaps identified" \
  --data '{
    "scope": "[spec sections or topic]",
    "topics_researched": 0,
    "already_addressed": 0,
    "gaps_high": 0,
    "gaps_medium": 0,
    "gaps_low": 0,
    "uncertain": 0,
    "jurisdiction_confirmed": true
  }'
```

---

## Resumption

Check for `.construction/code_research/` before starting:

| Files Present | State | Action |
|---------------|-------|--------|
| Nothing | Fresh start | Begin Phase 1 |
| `scope_definition.yaml` only | Scope confirmed, research not started | Begin Phase 2 |
| `pass1_summary.yaml` | Project extraction done | Begin Phase 3 |
| `topics/` partial | Research in progress | Resume from next unresearched topic |
| All topics complete, no `gap_analysis.yaml` | Research done | Begin Phase 4 |
| `gap_analysis.yaml` exists | Gaps identified | Present to user, go to Phase 5 |
| `report_*.md` exists | Complete | Offer to update or re-run |

---

## Discipline Notes

**On jurisdiction — never assume:**
The IBC edition adopted by a state is not always the most recently published
edition. States and cities adopt codes on their own schedules and with their
own amendments. A requirement confirmed against the wrong edition is not
confirmed. Always establish jurisdiction first (Phase 3a) before researching
requirements.

**On scope boundaries:**
The gap analysis is only as good as the documents reviewed in Pass 1. If the
engineer's scope includes drawings that weren't provided, or spec sections that
weren't read, those gaps cannot be identified. State clearly in the report
which documents were reviewed and which were not.

**On regulatory overlays:**
The building code is not the only applicable authority. Depending on scope,
relevant regulators may include: fire marshal, health department, USDA, FDA,
EPA, OSHA, utility company, state DOT, state environmental agency, and others.
These operate independently of the building code and are frequently missed
in standard code research. Flag the possibility of regulatory overlays whenever
the scope involves: food service, healthcare, hazardous materials, fuel systems,
elevators, pressure vessels, or work in public rights-of-way.

**On Pass 1 completeness:**
Before declaring a topic "not addressed," confirm that the relevant spec
section was read in full (all three parts), that related spec sections were
checked (Division 01 sections often cover topics globally), and that relevant
drawing notes and schedules were reviewed. A premature "not found" in Pass 1
becomes a false positive gap in Pass 3.

**On confidence levels:**
`confirmed` means: (1) the correct code edition for this jurisdiction has been
verified, (2) the code section has been read (not paraphrased from secondary
sources), (3) the project document status has been verified by reading the
actual document. Anything short of all three is `needs_review` or `uncertain`.
