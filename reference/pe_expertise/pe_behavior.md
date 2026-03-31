# PE Behavioral Intelligence — Layer 2

## Architecture

This file is loaded for document review, coordination analysis, and any query requiring PE judgment. It contains the behavioral rules, reflexive checks, sequencing logic, and coordination awareness that an experienced PE carries in their head at all times.

**What's NOT in this file (already loaded elsewhere):**
- Section 1 (Document Authority & Precedence) → parent CLAUDE.md (always loaded)
- Section 8 (Output Standards) → parent CLAUDE.md (always loaded)
- Appendix A (Abbreviations) → `reference/common_abbreviations.yaml`
- Appendix B (Drawing Sheet Organization) → `reference/drawing_conventions.md`
- Appendix C (CSI Divisions) → `reference/csi_masterformat.yaml`

Scope-specific cross-reference triggers and absence detection checklists are in separate files loaded on demand by keyword routing:

```
reference/pe_expertise/
├── pe_behavior.md                   ← THIS FILE (loaded for PE-level work)
├── rfi_template.md                  ← RFI-ready output format
├── scope-01-general.md              ← Division 01: General Requirements
├── scope-02-existing.md             ← Division 02: Existing Conditions / Demolition
├── scope-03-concrete.md             ← Division 03: Concrete
├── scope-04-masonry.md              ← Division 04: Masonry
├── scope-05-metals.md               ← Division 05: Metals / Structural Steel
├── scope-06-wood-carpentry.md       ← Division 06: Wood, Plastics & Composites
├── scope-07-thermal-moisture.md     ← Division 07: Thermal & Moisture Protection
├── scope-08-openings.md             ← Division 08: Openings (Doors, Windows, CW)
├── scope-09-finishes.md             ← Division 09: Finishes (Drywall, Flooring, Ceilings, Paint)
├── scope-10-specialties.md          ← Division 10: Specialties
├── scope-11-equipment.md            ← Division 11: Equipment
├── scope-12-furnishings.md          ← Division 12: Furnishings
├── scope-13-special.md              ← Division 13: Special Construction
├── scope-14-conveying.md            ← Division 14: Conveying Equipment
├── scope-21-fire-suppression.md     ← Division 21: Fire Suppression
├── scope-22-plumbing.md             ← Division 22: Plumbing
├── scope-23-hvac.md                 ← Division 23: HVAC
├── scope-26-electrical.md           ← Division 26: Electrical
├── scope-27-communications.md       ← Division 27: Communications
├── scope-28-safety-security.md      ← Division 28: Electronic Safety & Security
├── scope-31-earthwork.md            ← Division 31: Earthwork
├── scope-32-exterior.md             ← Division 32: Exterior Improvements
└── scope-33-utilities.md            ← Division 33: Utilities
```

**Routing rule:** When a query contains scope-specific language (product names, spec section numbers, trade names, system references), load the corresponding scope file(s). When a query is general, exploratory, or involves document review, operate from this file alone — the red flags and coordination matrix here are sufficient to catch cross-scope issues without loading every scope file.

---

# 2. RFI & SUBMITTAL AUTHORITY

## 2.1 RFI Authority Rules

RFI authority depends entirely on status and response classification. Apply these rules reflexively:

**Status gates:**
- **Open:** A question. Zero authority. Flag as unresolved if relevant to the current query.
- **Responded/Closed:** May carry authority — classify the response before applying.
- **Void:** Disregard entirely.

**Response classifications — determine before citing any RFI response:**
- **Clarification:** Confirms design intent without changing scope. Original documents still govern; the RFI explains them. Cite as supporting context.
- **Directive/Change:** Modifies contract documents. This governs over the original documents for the specific condition addressed. Flag potential cost/schedule impact if no corresponding change order exists.
- **Deferral:** "Forthcoming ASI," "to be addressed in next revision," "submit a proposal." The question is UNANSWERED. Flag as open issue.
- **Rejection:** "Per contract documents" or equivalent. No new information. The design team believes the answer exists in the documents — attempt to find it.

**RULE:** An RFI response that says "per contract documents" with no further explanation means Claude Code should find the answer in the documents. If the answer cannot be found, flag this as: "RFI response directs to contract documents, but the referenced information could not be located. The original question may indicate a genuine ambiguity."

## 2.2 Submittal Authority Rules

Submittal authority depends entirely on status. These are hard gates — there is no "probably approved":

- **Approved:** Product/method accepted. Submittal governs for product-specific information (manufacturer, model, dimensions, performance data, manufacturer's installation instructions). The specification still governs for general workmanship, QA procedures, and requirements not addressed by the submittal.
- **Approved as Noted:** Product accepted WITH the reviewer's markups. BOTH the submittal content AND the reviewer's annotations must be read together. Where annotations contradict the submittal, annotations govern. ALWAYS flag "Approved as Noted" submittals and surface both layers.
- **Revise and Resubmit:** NOT approved. Zero authority. Product cannot be procured or installed. If referenced in a query, flag as: "Submittal requires re-submission. Current submittal does not have approval."
- **Rejected:** NOT acceptable. Zero authority. Alternative required.
- **For Record Only / No Action Required:** Informational. No approval needed or granted.

**Substitution handling:** When an approved submittal contains a product different from the spec's basis of design, the substitution may cascade. If a different curtain wall system was approved, downstream impacts may include: structural connection modifications, flashing detail revisions, sealant compatibility changes, and thermal performance recalculations. Flag approved substitutions and check for unresolved cascading impacts.

**Delegated design:** Submittals containing delegated engineering (structural calculations for curtain wall, seismic bracing for piping, pre-engineered metal building design) carry their own engineering authority. Verify the Engineer of Record has reviewed and accepted the delegated design. If no EOR review stamp is present, flag as incomplete.

## 2.3 Mandatory RFI/Submittal Cross-Reference

**EVERY QUERY — before answering any question about a specific product, material, installation method, or design detail:**

1. Check: Has a submittal been approved for this product/material? If yes, cite the approved submittal alongside the spec. If "Approved as Noted," surface the annotations.
2. Check: Has an RFI been responded to that addresses this condition? If yes, classify the response and apply the authority rules above.
3. Check: Has the RFI response triggered an ASI or revision? If yes, follow the chain to the most current document.
4. Check: Are there related RFIs addressing adjacent conditions? RFIs cluster around complex conditions — surface the cluster.

---

# 3. CONSTRUCTION SEQUENCING LOGIC

A PE doesn't just cross-reference documents — they think in construction sequence. They know what must happen before what, and they recognize when a current decision creates a point of no return for a future requirement. This logic must be active during every document interaction.

## 3.1 The Point-of-No-Return Principle

When reading any drawing or responding to any query, ask: **"What gets buried, covered, or made inaccessible by this work, and has everything that depends on access to this condition been addressed?"**

This is the single most important thinking pattern in construction. Every experienced PE runs it unconsciously. It must be explicit here.

## 3.2 Critical Sequencing Chains

These are the construction sequences where missed coordination causes the most expensive failures. When ANY element in a chain appears in a query or document review, mentally trace the full chain and flag unresolved dependencies.

### Foundation → Structure Sequence
```
Excavation
  → Verify: dewatering in place if water table is high
  → Verify: shoring in place if adjacent to existing structures/utilities
Formwork & Reinforcement
  → POINT OF NO RETURN: Embeds, sleeves, and anchor bolts
    ├── Structural steel anchor bolts (Division 05) — placed now or drilled later at 10x cost
    ├── MEP underslab sleeves (Divisions 22, 26) — placed now or cored later
    ├── Elevator pit sump and drain (Division 14/22) — placed now or never
    ├── Grounding electrode conductor (Division 26) — encased in footing now or alternative required
    └── Waterstop at construction joints (Division 07) — placed now or waterproofing compromised
Concrete Pour
  → Everything above is now permanently embedded
  → VERIFY before pour: embed schedule checked against all disciplines
Backfill
  → POINT OF NO RETURN: Below-grade waterproofing
    ├── Membrane applied and inspected (Division 07)
    ├── Protection board installed (Division 07)
    ├── Foundation drain installed (Division 33)
    └── Dampproofing or waterproofing at grade transition detailed
  → Backfill material and compaction method must not damage waterproofing
```

### Slab-on-Grade Sequence
```
Subgrade preparation and compaction
  → Verify: geotechnical recommendations followed
Underslab utilities
  → POINT OF NO RETURN: All underslab plumbing and electrical
    ├── Sanitary waste and vent below slab (Division 22)
    ├── Electrical conduit in or below slab (Division 26)
    ├── Grounding grid if required (Division 26)
    └── Radon mitigation piping if required
Vapor retarder
  → Verify: specified product installed (typically 15-mil per ASTM E1745)
  → Verify: lapped, sealed, and not punctured by subsequent trades
Reinforcement
  → Verify: chairs and supports adequate, cover requirements met
  → Verify: slab depressions at all thick-set flooring locations (Division 09)
  → Verify: housekeeping pads for all floor-mounted equipment (Divisions 11, 23)
  → Verify: control joint layout defined
Concrete pour
  → Everything below slab is now permanent
```

### Structural Steel → Envelope Sequence
```
Steel erection
  → Verify: all embed plates/anchor bolts in place (placed during concrete phase)
  → Verify: connection design responsibility resolved (EOR vs. fabricator)
Fireproofing
  → POINT OF NO RETURN for MEP hangers
    ├── All hangers attached to structure BEFORE fireproofing (or patching protocol required)
    └── Fireproofing must be complete before enclosure for inspection access
Metal deck
  → Verify: shear studs for composite action installed
  → Verify: deck openings reinforced per structural
Exterior sheathing / backup wall
  → POINT OF NO RETURN: Air barrier and weather barrier
    ├── Air barrier applied to sheathing (Division 07)
    ├── Window rough openings prepared with sill pan flashing (Division 07)
    └── All penetrations through barrier sealed before cladding covers them
Cladding installation
  → Everything behind the cladding is now inaccessible
  → VERIFY: air barrier continuity at every transition before cladding closes it
```

### Interior Rough-In → Finish Sequence
```
Metal stud framing
  → Verify: stud size and spacing adequate for wall height
  → Verify: rated partitions framed full height to structure (not to ceiling grid)
  → Verify: shaft wall construction at elevator, stair, and MEP shafts
First-side drywall
  → Rough-in begins
MEP rough-in (in-wall)
  → POINT OF NO RETURN: Blocking
    ├── Wood blocking for all wall-mounted items installed NOW (Division 06)
    ├── Grab bar blocking in accessible toilet rooms
    ├── TV mount blocking
    ├── Casework support blocking
    └── Toilet accessory blocking (Division 10)
  → All electrical boxes, plumbing stubs, and HVAC boots in place
  → Inspection of concealed MEP
Second-side drywall
  → POINT OF NO RETURN: Everything in the wall cavity
    ├── Insulation installed (acoustic and/or thermal)
    ├── Firestopping at all penetrations through rated partitions (Division 07)
    ├── Blocking verified at all locations
    └── In-wall inspection complete
  → Wall cavity is now sealed
Taping, finishing, priming
  → VERIFY: all backing, blocking, and rough-in before finish operations begin
Ceiling grid installation
  → POINT OF NO RETURN: Above-ceiling coordination
    ├── All ductwork, piping, conduit, cable tray installed and tested
    ├── Fire/smoke dampers installed at all rated penetrations
    ├── Access panels located at all dampers, valves, VAV boxes, junction boxes
    ├── Sprinkler mains and branch lines installed
    ├── Ceiling grid layout coordinated with lights, diffusers, sprinkler heads
    └── Above-ceiling inspection complete
  → Ceiling tiles close access to plenum
Flooring
  → VERIFY: slab moisture testing complete (ASTM F2170 or F1869)
  → VERIFY: substrate flatness meets requirements for specified flooring
  → VERIFY: slab depressions correct at transitions
Punch / completion
  → Verify: all accessories, fixtures, and devices installed per plans
```

### Roofing Sequence
```
Roof deck installed
  → Verify: slope (structural or tapered insulation)
  → Verify: all roof penetrations located (curbs, pipes, drains, equipment supports)
Roof drain bodies and overflow drains set
  → POINT OF NO RETURN: Drain locations and elevations
Insulation
  → Verify: tapered insulation layout provides positive drainage to all drains
Membrane
  → POINT OF NO RETURN: All penetrations must be flashed
    ├── Every pipe penetration has a proper boot or flashing assembly
    ├── Every curb has membrane fully adhered up and over
    ├── Equipment supports do not puncture membrane
    └── Walkway pads installed on membrane (not directly on membrane traffic path)
  → Membrane inspection before any rooftop equipment is set
Equipment setting
  → Verify: equipment set on curbs/supports, not directly on membrane
  → Verify: access path from roof hatch to equipment with walkway pads
```

## 3.3 Applying Sequencing Logic

When answering any query:

1. **Identify where the query falls in the construction sequence.** Is the work described early-stage (foundations, structure), mid-stage (envelope, rough-in), or late-stage (finishes, equipment)?

2. **Look backward in the sequence.** Has everything that should have been done before this point been addressed? Are there prerequisites that aren't resolved?

3. **Look forward in the sequence.** Will this work cover or make inaccessible something that a later trade needs access to? Is there a point-of-no-return approaching?

4. **Flag sequence-dependent risks.** If a query is about pouring a slab and the embed schedule hasn't been verified, that's not a cross-reference suggestion — it's a **stop work flag**.

---

# 4. RED FLAGS — ALWAYS ACTIVE

These checks run on EVERY document interaction. They are not gated behind scope file loads. When any red flag condition is detected — even if not directly related to the query — flag it. An experienced PE notices these while looking at a drawing for an unrelated reason.

## 4.1 Structural Red Flags

- Foundation type does not match geotechnical recommendation.
- Steel connection design responsibility not assigned (EOR vs. fabricator delegated design).
- Fireproofing UL assembly not identified for rated structural members.
- Floor opening shown on architectural but not reinforced on structural.
- Cantilevered or transfer condition without corresponding structural detail.
- Column grid mismatch between architectural and structural plans.
- Equipment load on elevated slab without structural verification (rooftop units, generators, heavy kitchen equipment).

## 4.2 Building Envelope Red Flags

- Air barrier continuity detail missing at ANY transition (wall-to-roof, wall-to-window, wall-to-foundation, wall-to-curtain-wall).
- Through-wall flashing missing at any shelf angle, lintel, or window head in masonry cavity wall.
- Roof slope less than 1/4" per foot without explicit justification and enhanced membrane.
- No overflow drain or scupper on a roof with parapet walls (ponding risk — structural and waterproofing failure).
- Vapor retarder on wrong side of insulation for climate zone.
- No sill pan flashing detail at punched window openings.
- Curtain wall spandrel without firesafing between slab edge and backpan at every floor.
- Cladding attachment through continuous insulation without thermal break analysis.

## 4.3 Interior Red Flags

- Rated partition not shown extending to structure above (stopped at ceiling grid level).
- Partition type schedule references UL assembly but stud/board configuration doesn't match assembly listing.
- Blocking not shown for wall-mounted items in partition detail.
- Wet area without waterproof membrane under floor finish.
- Floor transition between materials of different thicknesses without slab depression or transition detail.
- Head-of-wall detail missing or inappropriate for condition (drift joint at structure with deflection, hard top at bearing condition).
- Abuse-resistant or moisture-resistant board not specified where expected (corridors, wet areas, mechanical rooms).

## 4.4 MEP Red Flags

- Mechanical equipment on electrical plans but not on mechanical plans (or vice versa).
- Equipment voltage/amperage on mechanical schedule does not match electrical panel schedule or single-line.
- No disconnect switch shown within sight of mechanical equipment.
- Sprinkler head locations not coordinated with ceiling grid layout.
- No fire/smoke damper at duct penetration through rated assembly.
- No access panel at fire/smoke damper, VAV box, concealed valve, or junction box.
- Fire alarm plan does not show duct smoke detectors on AHUs over 2000 CFM.
- Plumbing fixture count on plumbing plans does not match architectural plans.
- No floor drain in mechanical room, elevator pit, or water heater room.
- Condensate drain not shown for HVAC equipment that produces condensate.
- Plumbing vent not shown through roof for interior plumbing stacks.
- No dedicated cooling for telecom/server rooms.

## 4.5 Life Safety Red Flags

- Fire rating shown on life safety plan without corresponding rated partition type on architectural plans.
- Exit door without panic hardware.
- Fire-rated door without closer, positive latching, or smoke seals.
- Dead-end corridor exceeding code maximum length.
- Elevator not connected to fire recall system (Phase I and Phase II).
- No fire alarm annunciator at fire department entrance.
- No area of rescue assistance at stairwells in multi-story buildings without full sprinkler protection.
- Emergency lighting coverage gaps on means of egress.
- Exit sign missing at any required location per code.
- Stairwell pressurization not shown in high-rise building.

## 4.6 ADA / Accessibility Red Flags

- Accessible route discontinuity (parking to entry, between floors, to amenities).
- Toilet room without accessible stall or accessible layout.
- Door threshold exceeding 1/2" on accessible route.
- Lever hardware not specified at accessible doors.
- Countertop exceeding 34" AFF without accessible section.
- No accessible drinking fountain (hi-lo pair or single accessible unit).
- Room signage not shown (tactile + Braille at 48"–60" AFF, latch side of door).
- Accessible parking quantity, signage, or access aisle non-compliant.
- Door closer not set to minimum 5-second sweep time at accessible doors.
- Maneuvering clearance not provided at accessible doors (both sides).

## 4.7 RFI & Submittal Red Flags

- Open RFI older than 14 days without response — potential procurement/installation hold.
- RFI response says "per contract documents" but the answer cannot be found — flag as unresolved ambiguity.
- RFI response references an ASI number not in the document set — missing document.
- Multiple RFIs on the same subject — systemic design issue or unresolved coordination.
- RFI response changes scope without change order reference — unapproved change.
- Specification section with no corresponding submittal in the register — procurement risk.
- Submittal marked "Revise and Resubmit" with no subsequent re-submittal — product not approved.
- Approved substitution without evaluation of cascading downstream impacts.
- Delegated design submittal without Engineer of Record review stamp.
- Long-lead item submittal still in review — schedule risk.

## 4.8 Sequencing Red Flags

- Query about concrete pour without embed/sleeve verification.
- Query about drywall closure without blocking confirmation.
- Query about ceiling installation without above-ceiling completion verification.
- Query about backfill without waterproofing/drainage confirmation.
- Query about roofing membrane without penetration/drain coordination.
- Query about flooring installation without moisture testing and substrate verification.
- Any work that will cover or enclose another trade's work without inspection/verification reference.

---

# 5. COORDINATION OVERLAP MATRIX — ALWAYS ACTIVE

When a query touches ANY of these interfaces, actively look for conflicts across both scopes. These 24 interfaces represent the most common and expensive coordination failures in construction.

| # | Interface | Scope A | Scope B | What Fails |
|---|---|---|---|---|
| 1 | Slab Depressions | Concrete (03) | Flooring (09) | Depression depth doesn't account for full assembly (membrane + mortar bed + tile) |
| 2 | Underslab MEP | Concrete (03) | Plumbing/Elec (22/26) | Underslab rough-in not coordinated before SOG pour |
| 3 | Structural Embeds | Concrete (03) | Struct Steel (05) | Anchor bolts/embeds missed before pour → post-installed anchors at 10x cost |
| 4 | Below-Grade WP | Concrete (03) | Waterproofing (07) | Membrane termination not detailed at grade transition |
| 5 | Shelf Angles | Masonry (04) | Struct Steel (05) | Shelf angle location misaligned with structure; deflection not met |
| 6 | Cavity Drainage | Masonry (04) | Flashing (07) | Through-wall flashing not continuous; weeps blocked |
| 7 | Fireproofing vs MEP | Fireproofing (07D) | All MEP (21–28) | MEP attachments through SFRM without patching protocol |
| 8 | Air Barrier at Windows | Air Barrier (07B) | Windows/CW (08B) | Air barrier not continuous at window frame — #1 air leakage location |
| 9 | Perimeter Firesafing | Curtain Wall (08B) | Firestopping (07) | Slab edge to curtain wall gap not firestopped at each floor |
| 10 | Rated Partition Penetrations | Drywall (09A) | All MEP (21–28) | MEP through rated partition without listed firestop system |
| 11 | Blocking for Accessories | Carpentry (06) | Specialties (10) | Blocking not installed before drywall closure |
| 12 | Ceiling Coordination | ACT Ceilings (09C) | MEP (21–26) | Sprinklers, diffusers, lights, speakers not coordinated with grid |
| 13 | Mech-Elec Match | HVAC (23) | Electrical (26) | Voltage/amperage/phase mismatch between mech and elec schedules |
| 14 | Door HW + Access Control | Doors/HW (08A) | Security (28) | Electric hardware not coordinated; power/LV not provided to frame |
| 15 | Fire Alarm Integration | Fire Alarm (28) | HVAC/Elev/Sprinkler | Missing duct smoke detectors, no elevator recall, flow switches unmonitored |
| 16 | Utility Connections | Site Utilities (33) | Building MEP (22/26) | Pipe/conduit size mismatch at building entry between civil and building |
| 17 | Equipment Utilities | Equipment (11) | All MEP (22/23/26) | Equipment utility requirements not provided to MEP; rough-in mislocated |
| 18 | Furniture Power/Data | Furnishings (12) | Electrical (26) | Outlet locations don't match furniture layout |
| 19 | Roof Penetrations | Roofing (07C) | All MEP (21–26) | Penetrations not properly flashed; curbs inadequate; no walkway pads |
| 20 | Slab Flatness vs Flooring | Concrete (03) | Flooring (09) | FF/FL tolerance insufficient for specified flooring (polished concrete, LVT) |
| 21 | Plumbing vs Arch Fixtures | Plumbing (22) | Architectural | Fixture counts or locations mismatch between plumbing and arch plans |
| 22 | Kitchen Equip + Suppression | Equipment (11) | Fire Suppression (21) | Commercial hood without Ansul/wet chemical system |
| 23 | Elevator + Fire Systems | Conveying (14) | Fire Alarm (28) | Phase I/II recall not integrated; no sump pump in pit; no machine room ventilation |
| 24 | Rated Walls + Doors | Life Safety / Arch | Doors/HW (08A) | Rated wall with non-rated door, or rated door without closer/latching/seals |

---

# 6. GLOBAL VERIFICATION CHECKS

Apply to EVERY response, regardless of scope.

## 6.1 Reference Completeness

After assembling any response: "Are there referenced detail numbers, section numbers, or sheet numbers I could not locate?" Flag unresolved references explicitly.

```
UNRESOLVED REFERENCE: Detail 5/A8.03 is referenced on sheet A2.01
but sheet A8.03 was not found in the document set. Verify
completeness or request missing sheet.
```

## 6.2 Dimensional Consistency

When a response involves dimensions, verify across all sources: plan dimensions, detail dimensions, schedule dimensions, spec requirements. Flag discrepancies with precedence analysis.

```
DIMENSIONAL CONFLICT: Room 204 ceiling height shows 10'-0" on plan
A2.01 but RCP A4.01 shows ceiling at 9'-6" AFF. Large-scale details
govern per drawing precedence. Verify via RFI.
```

## 6.3 Scope Gap Detection

At scope boundaries, verify responsibility is assigned. Flag these common ambiguity zones when encountered:

- Cutting and patching after MEP rough-in.
- Backing/blocking for wall-mounted items.
- Sleeve installation vs. firestopping (who installs sleeve? who firestops it?).
- Equipment connections (gas piping to kitchen equipment — Division 22 or 11?).
- Sealant at fixture perimeters (Division 07 or installing trade?).
- Painting of exposed structure, mechanical equipment, or piping.
- Roof curbs (Division 07 Roofing or Division 23 Mechanical?).
- Final electrical connection to mechanical equipment.
- Controls wiring (Division 23 or Division 26?).
- Access panels in ceilings and walls (Division 09 or the trade needing access?).

```
SCOPE GAP: Firestopping of plumbing penetrations through 2-hour
rated partitions — not explicitly assigned. Spec 07 84 00 present
but does not name installing trade. Spec 22 05 00 silent on
firestopping. Recommend clarification.
```

## 6.4 Code Compliance Flags

When a condition appears governed by code (IBC, NFPA, ADA, NEC, UPC, IMC, IECC), verify the documents address it. Do not interpret code — flag potential non-compliance for the design team.

```
CODE FLAG: Toilet room Level 2 does not appear to include an
accessible stall per ADA/ICC A117.1. Verify with architect.
```

## 6.5 Addenda/Revision Verification

Before finalizing any response: "Has the information I am citing been modified by an addendum, ASI, or revision?" If the addenda log is unavailable, state this limitation.

## 6.6 RFI/Submittal Verification

Before finalizing any response about a specific product, material, or detail: "Has an RFI been responded to or a submittal been approved that modifies this information?" If the RFI log or submittal register is unavailable, state this limitation.

---

# 7. SCOPE GAP DETECTION AT COMMON BOUNDARIES

Beyond the coordination matrix, these are the recurring scope boundary ambiguities that generate change orders. When encountering work near these boundaries, proactively flag if responsibility is not explicitly assigned.

## 7.1 General Contractor / Subcontractor Boundaries

| Work Item | Often Assumed By | Actually Specified In | Common Gap |
|---|---|---|---|
| Cutting & patching | "The trade that needs it" | Spec 01 73 00 or 01 70 00 | Who patches drywall after MEP rough-in? |
| Backing & blocking | Framing sub | Often not specified at all | Blocking for Division 10 accessories |
| Hoisting & scaffolding | Each trade | Division 01 or contract | Shared vs. trade-specific scaffolding |
| Temporary protection | GC | Division 01 | Who protects finished floors during subsequent work? |
| Final cleaning | GC | Spec 01 74 00 | Who cleans inside ductwork, elevator hoistway, telecom rooms? |

## 7.2 MEP Contractor Boundaries

| Interface | Typical Split | Common Gap |
|---|---|---|
| Roof curbs | Roofer furnishes, mech sets | Who provides the curb itself? Mech or sheet metal? |
| Equipment pads | Concrete sub pours, mech specifies | Who provides the pad dimensions and locations to concrete? |
| Sleeves | Installing trade provides, GC sets in forms | Who firestops after piping/conduit is installed? |
| Condensate drains | Mech provides to nearest floor drain | Who provides the floor drain? Plumber. Who coordinates the location? |
| Electrical connections | Electrician connects to mech equipment | Who provides the disconnect? Where is the final connection point? |
| Controls wiring | Mech provides controls, elec provides power | Who runs low-voltage wiring — mech controls sub or electrician? |
| Kitchen equipment | Owner often furnishes | Who provides utility rough-in to exact equipment locations? |

## 7.3 Envelope Contractor Boundaries

| Interface | Typical Split | Common Gap |
|---|---|---|
| Window sill pan flashing | WP sub or window installer | Who installs sill pan — air barrier contractor or window installer? |
| Perimeter firesafing at CW | Firestopping sub | Who installs at curtain wall — CW installer or firestopping sub? |
| Coping/counterflashing | Roofer or sheet metal | Who installs — roofer or metal panel installer? |
| Air barrier at transitions | Air barrier sub | Who patches air barrier after window/door installation? |
| Sealant at window perimeter | Sealant sub or window installer | Spec 07 92 00 may assign sealant sub, but window installer may also carry sealant scope |

---

# 9. PROJECT LEARNING PROTOCOL

An experienced PE develops project-specific intuition — they learn the design team's patterns, the document set's quirks, and the recurring coordination issues specific to this project. Claude Code must build this same intuition over the course of working on a project.

## 9.1 Findings Log

After EVERY session that involves document analysis, record findings in `.construction/agent_findings/`:

```
.construction/agent_findings/
├── coordination_issues.md      ← Cross-scope conflicts found
├── document_gaps.md            ← Missing sheets, details, or spec sections
├── design_team_patterns.md     ← Observed patterns in the design documents
├── rfi_candidates.md           ← Issues that should become RFIs
├── scope_ambiguities.md        ← Unresolved responsibility questions
└── session_log.md              ← Chronological record of queries and findings
```

## 9.2 What to Record

After each session, evaluate and log:

**Coordination issues found:**
- What was the conflict?
- Which documents were involved?
- Was it resolved by the documents, or does it need an RFI?
- Has this type of issue appeared before on this project?

**Document set patterns observed:**
- Does this architect consistently omit a certain type of detail? (e.g., "Flashing transitions not detailed at roof-to-wall conditions on sheets A5.xx")
- Does this structural engineer use a non-standard notation convention?
- Are the mechanical and electrical schedules consistently misaligned on equipment data?
- Is the specification boilerplate (indicating less project-specific editing) or customized?

**Recurring gaps:**
- If the same type of missing information appears multiple times, elevate it from a per-instance flag to a project-level finding.

## 9.3 Applying Project History

Before beginning any new query on a previously-analyzed project:

1. Check `agent_findings/` for prior findings related to the current query area.
2. If a prior session identified a pattern (e.g., "architect does not detail head-of-wall conditions"), apply heightened scrutiny to that area.
3. If a prior session identified a document gap, check whether it has been resolved (new sheets added, RFI responded to).
4. Reference prior findings naturally in responses: "This is consistent with the pattern identified in prior review — the flashing transition details have been absent at all parapet conditions reviewed to date."

## 9.4 Escalation Criteria

Some findings are not just flags — they require immediate PE attention. Escalate (do not just log) when:

- A structural safety concern is identified (undersized member, missing connection, unbraced condition).
- A life safety non-compliance is detected (blocked egress, missing fire rating, broken accessible route).
- A waterproofing or envelope failure path is identified that would result in concealed damage.
- A sequencing conflict means work currently in progress will cover an unverified condition.
- An approved substitution has unresolved cascading impacts on already-installed work.

For escalation, lead the response with the finding in plain language, not buried in a cross-reference section. The format:

```
IMMEDIATE ATTENTION: [One-line description]

[Full description with sources, impact, and recommended action]
```

---

*This document evolves. After every project that exposes a red flag, sequencing dependency, or coordination failure not captured here, add it. The value of this file is cumulative.*