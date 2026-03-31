# Scope File: Division 04 — Masonry

**Load when:** Query references brick, CMU, concrete masonry units, stone, stone veneer, unit masonry, mortar, grout, masonry reinforcement, masonry lintels, or any spec section 04 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Architectural elevations — patterns, coursing, color, joint profiles.
- Architectural wall sections and details — cavity wall assemblies, veneer anchoring, flashing, weeps, lintels, shelf angles.
- Structural plans — masonry bearing walls, reinforced masonry, grouted cells, lintel schedules.
- Spec 04 05 00 — Common Work Results for Masonry.
- Spec 04 20 00 — Unit Masonry (CMU and brick assemblies).
- Spec 04 43 00 / 04 42 00 — Stone Masonry / Exterior Stone Cladding.
- Spec 04 72 00 — Cast Stone (if applicable).
- Spec 04 05 23 — Masonry Accessories (reinforcement, ties, anchors, flashing).
- Spec 05 50 00 — Metal Fabrications (shelf angles, loose lintels).
- Spec 07 21 00 — Thermal Insulation (cavity insulation).
- Spec 07 27 00 — Air Barriers (within cavity wall assembly).
- Spec 07 60 00 / 07 62 00 — Flashing and Sheet Metal (through-wall, cap).
- Spec 07 92 00 — Joint Sealants (expansion/control joints, perimeter at openings).
- **Submittal register** — check for approved masonry unit samples, mortar mix, reinforcement, flashing, and sealant submittals.
- **RFI log** — check for RFIs about masonry patterns, flashing details, lintel sizes, or movement joints.

---

## Absence Detection Checklist

- [ ] Control joint layout on plans/elevations with spacing per standards.
- [ ] Expansion joint layout for clay masonry (brick expands; CMU shrinks — different joint types required).
- [ ] Through-wall flashing at shelf angles, lintels, base of wall, and window/door heads.
- [ ] Weep hole spacing and type (open head joint, wicking, or tube).
- [ ] Cavity drainage and ventilation strategy (air space dimensions, vents top and bottom).
- [ ] Lintel schedule with sizes, spans, bearing lengths, loose vs. masonry lintel designation.
- [ ] Shelf angle layout with relief angle dimensions and soft joint below.
- [ ] Mortar type specified by location (Type N, S, or M with rationale).
- [ ] Masonry reinforcement type and spacing (horizontal joint reinforcement, vertical grouted cells).
- [ ] Movement joint sealant specified (compatible with masonry, accommodates movement range).
- [ ] Sample panel/mock-up requirements for aesthetic masonry.
- [ ] Approved masonry unit and mortar submittals (check register).

---

## Sequencing Context

```
Foundation/backup wall complete
  → Shelf angles installed and surveyed for elevation (Div 05)
  → POINT OF NO RETURN: Through-wall flashing at base of wall
    └── Flashing must be installed BEFORE first course of masonry
  → Masonry laid course by course
  → POINT OF NO RETURN: Flashing at each shelf angle
    ├── Through-wall flashing placed on shelf angle
    ├── Soft joint (sealant, not mortar) immediately below shelf angle
    └── Weep holes at flashing level
  → POINT OF NO RETURN: Flashing at window/door heads
    ├── Lintel installed with bearing length verified
    ├── Through-wall flashing over lintel with end dams
    └── Weep holes above opening
  → Cavity insulation and air barrier (if cavity wall assembly)
  → Window/door frame installation coordinated with masonry coursing
  → Control/expansion joints sealed after masonry curing (minimum 28 days for movement joints)
```

**Critical rule:** Masonry flashing is the most commonly omitted element in cavity wall construction. Every horizontal interruption (shelf angle, lintel, window head, base of wall) requires through-wall flashing with end dams and weep holes. Missing any one creates a moisture path into the building.

---

## Coordination Overlaps

- **With Structural Steel (Div 05):** Shelf angle locations must align with framing. Deflection criteria L/600 for masonry support. (pe_behavior.md Matrix #5)
- **With Waterproofing/Air Barrier (Div 07):** Flashing material compatibility with mortar and sealants. Air barrier continuity through cavity. (pe_behavior.md Matrix #6)
- **With Openings (Div 08):** Frame anchoring to masonry, sealant joints at frames, lintel sizing for opening widths.
- **With MEP:** Penetrations through masonry require sleeving and firestopping if rated. Louver/vent/exhaust openings must be shown in masonry and structurally supported.
