# Scope File: Division 02 — Existing Conditions / Demolition

**Load when:** Query references demolition, selective demolition, hazardous material abatement, existing conditions, "existing to remain," "remove," "salvage," "relocate," "protect," or work in/adjacent to existing structures. Also load for any spec section 02 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded). This file provides detailed cross-reference lists and absence checklists.**

---

## Cross-Reference Triggers

When a query involves demolition, abatement, or existing conditions, pull ALL of the following:

- Demolition plans (architectural and structural) — verify extent of removal matches across disciplines.
- Structural drawings — existing structural elements to remain, new connections to existing structure.
- MEP demolition plans — verify MEP systems to be demolished, capped, or relocated align with architectural demolition.
- Spec 01 50 00 — protection of existing construction, occupied areas.
- Hazardous materials report (typically referenced, not always included) — asbestos, lead paint, PCBs.
- Civil/site drawings — utilities to be abandoned, relocated, or protected.
- Geotechnical report — existing soil/subsurface conditions affecting demolition or excavation.
- Spec 02 41 00 — Demolition: methods, disposal, salvage requirements.
- Spec 02 82 00 — Asbestos Remediation (or similar hazmat sections).
- **RFI log** — check for RFIs about extent of demolition, existing conditions discovered, or hazmat findings.
- **Submittal register** — check for approved hazmat abatement plans, shoring designs if applicable.

---

## Absence Detection Checklist

- [ ] Demolition plans provided for each discipline (Architectural, Structural, Mechanical, Electrical, Plumbing).
- [ ] Extent of demolition clearly delineated (full vs. selective, what remains, what is removed).
- [ ] Disposition of demolished material defined (salvage, recycle, dispose, return to Owner).
- [ ] Protection requirements for adjacent existing construction.
- [ ] Temporary shoring/bracing requirements during demolition of structural elements.
- [ ] Hazardous material survey referenced or included.
- [ ] Disconnect/cap/abandon procedures for existing MEP systems.
- [ ] Existing utility locations identified and protection measures specified.
- [ ] Survey of existing conditions required before demolition (as-built verification).
- [ ] Notification/coordination requirements if building is partially occupied during demolition.
- [ ] Dust/noise/vibration control requirements specified.
- [ ] Approved hazmat abatement plan (check submittal register).

---

## Sequencing Context

Demolition is typically the FIRST construction activity. Everything depends on it being complete and correct.

```
Hazmat survey and abatement (if required)
  → Must be complete BEFORE any general demolition in affected areas
  → POINT OF NO RETURN: Abatement must be verified and clearance testing passed
Utility disconnect
  → All MEP systems serving demolition area disconnected, capped, and locked/tagged out
  → POINT OF NO RETURN: Verify no active services run through demolition zone
  → Verify "cap and abandon" vs. "remove entirely" is consistent across disciplines
Structural demolition
  → POINT OF NO RETURN: Shoring must be in place before removing any load-bearing element
  → Verify demolition sequence with structural engineer if removing bearing walls/columns
  → Temporary bracing for adjacent structure that shares demolished elements
Selective demolition
  → Protection of finishes and systems designated "existing to remain"
  → Accurate survey of existing conditions for new work to tie into
```

**Critical rule:** Existing conditions are NEVER exactly as shown on the drawings. The drawings show design intent from the original construction. Hidden conditions (concealed structure, abandoned utilities, hazardous materials not in the survey, different framing than documented) are the norm, not the exception. Flag any query that assumes existing conditions match drawings as requiring field verification.

---

## Coordination Overlaps

- **With Structural (Division 05/03):** Demolition of existing structural elements requires engineer-approved shoring plan. (pe_behavior.md Red Flag §4.1)
- **With MEP trades (Divisions 21–28):** Existing MEP disconnection/capping BEFORE architectural demolition. "Cap and abandon" vs. "remove entirely" must be consistent across all disciplines.
- **With Sitework (Division 31/33):** Underground utility abandonment/removal must align with new utility routing.
- **With Division 01:** Phasing requirements — partial demolition in occupied buildings requires detailed sequencing.
