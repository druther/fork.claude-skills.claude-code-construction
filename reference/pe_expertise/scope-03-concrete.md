# Scope File: Division 03 — Concrete

**Load when:** Query references foundations, footings, slab-on-grade, elevated slabs, concrete walls, concrete stairs, cast-in-place or precast concrete, reinforcement, formwork, mix design, curing, embeds, anchor bolts, cast-in items, or any spec section 03 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded). This file provides detailed cross-reference lists and absence checklists.**

---

## Cross-Reference Triggers

When a query involves concrete work, pull ALL of the following:

### Drawings
- Structural foundation plans, framing plans at each level, structural sections and details.
- Geotechnical report — bearing capacity, soil conditions, water table, foundation type recommendations.
- Architectural plans — slab depression locations (wet areas, tile transitions, thresholds), floor finish schedule (for FF/FL requirements).
- Architectural details — slab edge conditions, curb details, depressed slab details, housekeeping pads.
- Civil/site plans — building pad elevation, SOG elevation relative to site drainage.
- MEP plans — underslab plumbing, electrical conduit in slab, mechanical equipment pads, expansion joint locations relative to MEP routing.

### Specifications
- Spec 03 10 00 — Concrete Forming and Accessories.
- Spec 03 11 00 — Concrete Forming (form ties, rustication strips).
- Spec 03 20 00 — Concrete Reinforcing (rebar and post-tensioning).
- Spec 03 30 00 — Cast-In-Place Concrete (mix designs, placement, finishing, curing).
- Spec 03 35 00 — Concrete Finishing (FF/FL tolerances).
- Spec 03 40 00 — Precast Concrete (if applicable).
- Spec 03 05 00 — Common Work Results for Concrete (vapor retarder, curing compounds, joint sealants).
- Spec 07 10 00 — Dampproofing and Waterproofing (below-grade).
- Spec 07 11 00 — Dampproofing.
- Spec 07 13 00 / 07 14 00 / 07 16 00 — Waterproofing (sheet, fluid-applied, cementitious).
- Spec 07 18 00 — Traffic Coatings (parking/plaza decks).
- Division 05 sections — embed plates, anchor bolts, connection hardware cast into concrete.

### RFI/Submittal Checks
- **Submittal register** — check for approved concrete mix designs, rebar shop drawings, post-tensioning shop drawings, vapor retarder product, and form tie/accessory submittals.
- **RFI log** — check for RFIs about foundation conditions, slab elevations, embed locations, or concrete mix modifications.

---

## Absence Detection Checklist

- [ ] Concrete mix design(s) specified with compressive strength, slump, air entrainment, and exposure class.
- [ ] Reinforcing steel grade, cover requirements, and lap splice lengths specified.
- [ ] Slab-on-grade vapor retarder specified (typically 15-mil per ASTM E1745).
- [ ] FF/FL tolerances specified by area (higher for polished concrete, LVT, thin-set tile).
- [ ] Control joint and construction joint layout on structural plans.
- [ ] Expansion joint locations with architectural joint cover details.
- [ ] Curing method and duration specified.
- [ ] Embed/anchor bolt schedule or details for all cast-in items.
- [ ] Waterstop specified at below-grade construction joints.
- [ ] Post-tensioning shop drawing requirements (if PT system used).
- [ ] Housekeeping pad sizes and locations for all floor-mounted equipment.
- [ ] Slab depressions at wet areas verified (depth accounts for waterproofing + mortar bed + tile vs. adjacent finish thickness).
- [ ] Cold weather and hot weather concrete placement procedures specified.
- [ ] Concrete testing frequency and acceptance criteria (per ACI 318).
- [ ] Approved mix design submittal (check register).
- [ ] Approved rebar shop drawing submittal (check register).

---

## Sequencing Context

Concrete work contains the highest concentration of points of no return in any project. See pe_behavior.md §3.2 for the full Foundation→Structure and Slab-on-Grade sequences.

### Foundation Sequence
```
Excavation complete, bearing verified by geotech
  → Formwork and reinforcement placed
  → POINT OF NO RETURN — EMBEDS AND SLEEVES:
    ├── Structural steel anchor bolts (Div 05) — placed now or drilled at 10x cost
    ├── MEP underslab sleeves (Div 22, 26) — placed now or cored later
    ├── Elevator pit sump and drain (Div 14/22) — placed now or never
    ├── Grounding electrode conductor (Div 26) — encased in footing now or alternative needed
    └── Waterstop at construction joints (Div 07) — placed now or waterproofing compromised
  → PRE-POUR CHECKLIST:
    ├── Embed schedule verified against ALL disciplines
    ├── Reinforcement inspected (cover, spacing, lap lengths, chairs)
    ├── Vapor retarder inspected (laps, seals, no punctures)
    ├── Slab depressions verified at correct locations and depths
    ├── Housekeeping pads formed at all equipment locations
    └── Special inspection scheduled (if required)
  → Concrete pour — everything below is now permanent
```

### Elevated Slab Sequence
```
Deck/formwork in place
  → Reinforcement placed (conventional or PT)
  → POINT OF NO RETURN — PENETRATIONS AND EMBEDS:
    ├── All floor penetrations (sleeves) for MEP placed
    ├── Slab edge embeds for curtain wall/cladding support
    ├── Post-tensioning tendons stressed (if PT) before MEP attachment
    └── Shear studs welded (if composite deck)
  → Pour — penetrations through elevated slab now require coring (structural impact)
```

**Critical timing:** Post-tensioning stressing typically occurs 3–7 days after pour. MEP trades cannot core or attach to PT slabs until stressing is complete AND the PT shop drawings are consulted to locate tendons. Coring through a PT tendon is a structural emergency.

---

## Coordination Overlaps

- **With Waterproofing (Div 07):** Below-grade concrete requires coordinated waterproofing. Verify membrane termination, protection board, drainage mat. Concrete surface prep for membrane adhesion. (pe_behavior.md Matrix #4)
- **With Structural Steel (Div 05):** Embed plates, anchor bolts, base plates must be placed before pour. Verify anchor bolt plans match foundation embed callouts. (pe_behavior.md Matrix #3)
- **With MEP (Div 21–26):** Underslab plumbing and electrical before SOG pour. Sleeves through elevated slabs, walls, foundations before pour. Verify sleeve schedule matches MEP penetration requirements. (pe_behavior.md Matrix #2)
- **With Flooring (Div 09):** Slab depression depths must account for FULL assembly (not just tile — include membrane + mortar bed). FF/FL tolerances must match flooring requirements. (pe_behavior.md Matrix #1, #20)
- **With Earthwork (Div 31):** Subgrade preparation and compaction per geotechnical recommendations.
