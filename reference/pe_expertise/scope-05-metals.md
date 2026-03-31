# Scope File: Division 05 — Metals / Structural Steel

**Load when:** Query references structural steel, miscellaneous metals, metal stairs, handrails, guardrails, metal fabrications, steel framing, columns, beams, joists, decking, connections, embeds, or any spec section 05 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

### Drawings
- Structural framing plans at each level, steel details, connection details, bracing plans.
- Architectural plans — stair locations/configurations, handrail locations, canopy locations, screen walls.
- Architectural details — handrail/guardrail details, canopy details, metal panel support framing.

### Specifications
- Spec 05 10 00 — Structural Metal Framing.
- Spec 05 12 00 — Structural Steel Framing (W shapes, HSS, angles, channels).
- Spec 05 21 00 — Steel Joist Framing (bar joists, joist girders).
- Spec 05 31 00 — Steel Decking (roof, floor, composite).
- Spec 05 40 00 — Cold-Formed Metal Framing (if structural scope).
- Spec 05 50 00 — Metal Fabrications (misc steel: lintels, embeds, angles, brackets, bollards, equipment supports, roof hatches/ladders).
- Spec 05 51 00 — Metal Stairs.
- Spec 05 52 00 — Metal Railings.
- Spec 05 58 00 — Formed Metal Fabrications (metal pan stairs, grating, floor plates).
- Spec 07 81 00 — Applied Fireproofing.
- Spec 09 96 00 or structural notes — Fireproofing (SFRM or intumescent).
- Division 03 — Anchor bolt plans, embed details in concrete.
- Structural general notes — design loads, steel grades, welding standards, connection design responsibility.
- Special inspections schedule — welding inspection, high-strength bolting.

### RFI/Submittal Checks
- **Submittal register** — check for approved steel shop drawings, misc metals shop drawings, stair/railing shop drawings, and connection design calculations (if delegated).
- **RFI log** — check for RFIs about connections, member sizes, embed locations, or coordination conflicts.

---

## Absence Detection Checklist

- [ ] Connection design responsibility clearly assigned (EOR vs. fabricator delegated design).
- [ ] Steel grade specified per member type (A992 W shapes, A500 HSS, A36 misc).
- [ ] Fireproofing type, thickness, and UL assembly rating for all protected members.
- [ ] Corrosion protection specified (galvanizing, primer, or coating) per exposure condition.
- [ ] Base plate and anchor bolt details for all column bases.
- [ ] Roof and floor deck gauge, type (B, N, composite), and attachment.
- [ ] Shear stud layout for composite deck.
- [ ] Misc steel schedule/details for all lintels, shelf angles, embeds, equipment supports.
- [ ] Handrail/guardrail loading (IBC: 200 lb point, 50 plf distributed).
- [ ] Stair details: pan thickness, concrete fill, nosing, handrail mounting.
- [ ] Welding requirements and inspection level (AWS D1.1, visual vs. UT/MT).
- [ ] Approved steel shop drawings (check register — these are on the critical path).
- [ ] Delegated design calculations reviewed by EOR (check register).

---

## Sequencing Context

See pe_behavior.md §3.2 (Structural Steel → Envelope Sequence) for the full chain.

```
Concrete foundations complete with anchor bolts cast
  → Verify anchor bolt locations against steel shop drawings BEFORE grouting base plates
  → POINT OF NO RETURN: Anchor bolt survey
    └── Out-of-tolerance anchor bolts require engineering resolution before steel erection
Steel erection
  → Connections made (bolted or welded per shop drawings)
  → POINT OF NO RETURN: MEP hangers before fireproofing
    ├── All hangers attached to structure BEFORE SFRM application
    ├── Or: patching protocol must be specified and assigned
    └── Fireproofing is inspected before it gets covered — access is critical
Metal decking
  → Shear studs welded for composite action
  → Deck openings reinforced per structural details
  → POINT OF NO RETURN: Deck pour
    └── All slab embeds, sleeves, and edge conditions in place before elevated slab pour
Misc metals
  → Lintels, shelf angles, equipment supports fabricated per approved shop drawings
  → Embed plates cast in concrete at correct locations (see Div 03 sequencing)
  → Stair pans and railings fabricated — long lead items
```

**Critical timing:** Steel shop drawing review and fabrication is typically 12–16 weeks from contract award to first delivery. This is almost always on the critical path. Delays in shop drawing approval directly delay the project.

---

## Coordination Overlaps

- **With Concrete (Div 03):** Anchor bolt and embed placement before pour. Grout under base plates. Column grid alignment. (pe_behavior.md Matrix #3)
- **With Masonry (Div 04):** Shelf angle and lintel sizing for masonry loads. Deflection criteria. (pe_behavior.md Matrix #5)
- **With Fireproofing (Div 07):** UL assembly designations, MEP attachment coordination through SFRM. (pe_behavior.md Matrix #7)
- **With MEP (Div 21–26):** Opening reinforcement for large penetrations. Equipment support steel (dunnage) scope assignment.
- **With Curtain Wall/Metal Panels (Div 07/08):** Support framing for cladding systems. Connection details between cladding support and primary structure.
