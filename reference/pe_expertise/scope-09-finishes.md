# Scope File: Division 09 — Finishes

**Load when:** Query references interior partitions, drywall, gypsum board, metal studs, partition types, flooring, tile, carpet, VCT, LVT, terrazzo, acoustical ceilings, ACT, suspended ceilings, painting, coatings, wall coverings, or any spec section 09 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Sub-Scope 09A: Metal Studs & Drywall (Gypsum Board Assemblies)

### Cross-Reference Triggers

- Architectural plans — partition type designations at each wall.
- Partition type schedule — stud size, spacing, board layers, board type (regular, Type X, abuse-resistant, moisture-resistant, glass-mat), insulation, height, STC/fire rating.
- RCPs — soffit and bulkhead locations, ceiling height changes.
- Architectural details — head-of-wall conditions, partition-to-structure, rated partition details.
- Life safety plans — rated partition locations and hourly ratings.
- Spec 09 21 00 — Plaster and Gypsum Board Assemblies.
- Spec 09 22 00 — Supports for Plaster and Gypsum Board.
- Spec 09 29 00 — Gypsum Board.
- Spec 05 40 00 — Cold-Formed Metal Framing (if structural studs).
- Spec 07 21 00 — Thermal Insulation (acoustic in partitions).
- Spec 07 84 00 — Firestopping (at rated partition penetrations).
- Spec 09 51 00 — Acoustical Ceilings (coordination with head-of-wall).
- UL assembly designations for rated partitions.
- **Submittal register** — check for approved partition system submittals, board product data, and UL assembly documentation.
- **RFI log** — check for RFIs about partition types, head-of-wall conditions, or rating questions.

### Absence Detection

- [ ] Partition type schedule with all types referenced on plans.
- [ ] UL or GA assembly designation for every rated partition type.
- [ ] Head-of-wall detail per partition type (hard top vs. drift joint vs. deflection track).
- [ ] Rated partitions extend full height to structure (not ceiling grid).
- [ ] Abuse-resistant board in corridors, mechanical rooms, storage, high-traffic.
- [ ] Moisture-resistant or glass-mat board in wet areas and behind tile.
- [ ] Acoustic insulation in rated partitions and partitions requiring STC.
- [ ] Blocking shown at all wall-mounted item locations (cross-ref Div 06).
- [ ] Shaft wall construction for elevator, stair, and MEP shafts.
- [ ] Stud size/spacing adequate for wall height (verify engineering for partitions over 12'–14').
- [ ] Corner bead and trim profiles specified.

### Sequencing Context

See pe_behavior.md §3.2 (Interior Rough-In → Finish Sequence) for full chain.

```
Metal stud framing (first side board)
  → MEP rough-in, blocking, insulation
  → POINT OF NO RETURN: Second-side closure
    ├── ALL in-wall MEP complete and inspected
    ├── ALL blocking in place (Div 06)
    ├── Firestopping at rated partition penetrations (Div 07)
    ├── Acoustic insulation installed
    └── In-wall inspection complete
  → Taping, finishing, priming
  → Paint (after all penetrations, patches, and touch-ups)
```

---

## Sub-Scope 09B: Flooring

### Cross-Reference Triggers

- Floor finish plan — designations by room/area.
- Floor finish schedule — material, color, pattern, manufacturer, spec section per designation.
- Architectural details — transitions, thresholds, stair nosings, base conditions.
- Structural plans — slab depressions, housekeeping pads.
- Spec 09 30 00 — Tiling.
- Spec 09 63 00 — Masonry Flooring.
- Spec 09 65 00 — Resilient Flooring (VCT, LVT, rubber, linoleum).
- Spec 09 68 00 — Carpeting.
- Spec 09 66 00 — Terrazzo.
- Spec 09 67 00 — Fluid-Applied Flooring (epoxy, urethane, MMA).
- Spec 09 05 00 — Common Work Results for Flooring (substrate prep, moisture testing, leveling).
- Spec 03 35 00 — Concrete Finishing (FF/FL tolerances).
- Spec 07 14 00 / 07 18 00 — Waterproofing under tile at wet areas.
- Spec 09 06 00 — Floor Treatment (sealers, hardeners for polished concrete).
- **Submittal register** — check for approved flooring product submittals per designation.
- **RFI log** — check for RFIs about transitions, slab depressions, or moisture issues.

### Absence Detection

- [ ] Floor finish schedule complete — all designations on plans accounted for.
- [ ] Transition details between different types and thicknesses.
- [ ] Slab depression schedule matching thick-set assemblies.
- [ ] Substrate prep requirements (moisture testing ASTM F2170/F1869, leveling).
- [ ] Waterproof membrane under tile at ALL wet areas.
- [ ] FF/FL requirements specified by flooring type.
- [ ] Base type and height at all walls.
- [ ] Stair nosing profiles and materials.
- [ ] Anti-slip requirements at wet areas and entries (COF values).
- [ ] Carpet transition strips and edge conditions.
- [ ] Approved flooring submittals per designation (check register).

### Sequencing Context

```
Concrete slab cured (minimum 28 days typical, longer for moisture-sensitive flooring)
  → Moisture testing (ASTM F2170 relative humidity or F1869 calcium chloride)
  → POINT OF NO RETURN: Moisture testing must pass BEFORE flooring installation
    ├── Failed test = wait, apply moisture mitigation system, or change flooring spec
    ├── Installing flooring over wet slab = delamination, mold, failure
    └── Verify slab moisture specification against flooring manufacturer's requirements
  → Substrate preparation (grinding, leveling, patching)
  → Waterproofing membrane at wet areas (before tile)
  → Flooring installation (typically one of the last finish activities)
  → Base installation after flooring and wall paint
```

---

## Sub-Scope 09C: Acoustical Ceilings

### Cross-Reference Triggers

- RCPs — ceiling types, heights, grid layout, fixture/diffuser/sprinkler/access panel locations.
- Ceiling finish schedule — tile type, grid type, size, edge profile, NRC, CAC.
- Architectural sections — ceiling heights, plenum dimensions.
- Spec 09 51 00 — Acoustical Ceilings.
- Spec 09 54 00 — Specialty Ceilings.
- Division 23 — diffuser/grille locations (coordinate with grid).
- Division 26 — light fixture locations (coordinate with grid).
- Division 21 — sprinkler head locations (coordinate with grid).
- Division 28 — fire alarm devices in ceiling.
- **Submittal register** — check for approved ceiling system submittals.

### Absence Detection

- [ ] RCP provided for every occupied space.
- [ ] Ceiling type schedule with materials, sizes, edge profiles, ratings.
- [ ] Ceiling heights verified against ductwork, structure, and plumbing (adequate plenum).
- [ ] Access panels at all concealed valves, dampers, junction boxes, equipment.
- [ ] Seismic bracing for grid per code.
- [ ] Grid coordination with lights, diffusers, sprinkler heads (center in tiles or on grid lines).

### Sequencing Context

See pe_behavior.md §3.2 (Interior Rough-In → Finish — ceiling grid section).

```
All above-ceiling work complete:
  → Ductwork, piping, conduit, cable tray installed and tested
  → Fire/smoke dampers installed at rated penetrations
  → Access panels located at all dampers, valves, VAV boxes, junction boxes
  → Sprinkler mains and branches installed
  → POINT OF NO RETURN: Ceiling grid installation
    └── Grid layout MUST coordinate with lights, diffusers, sprinklers, speakers
  → Above-ceiling inspection complete
  → Tiles installed (last — tiles close access to plenum)
```

---

## Sub-Scope 09D: Painting & Wall Coverings

### Cross-Reference Triggers

- Finish schedule — colors, sheen, coats by room/surface.
- Spec 09 91 00 — Painting.
- Spec 09 96 00 — High-Performance Coatings.
- Spec 09 72 00 — Wall Coverings.
- Spec 09 97 00 — Special Coatings.
- **Submittal register** — check for approved paint color selections and product submittals.

### Absence Detection

- [ ] Paint system specified per substrate (GWB, CMU, concrete, metal, wood — different primers).
- [ ] Coats specified (primer + 2 finish coats standard commercial).
- [ ] Sheen per area (flat ceilings, eggshell walls, semi-gloss wet areas/trim).
- [ ] Moisture-resistant primer/coating at wet area walls not receiving tile.
- [ ] VOC limits per indoor air quality requirements.

---

## Division 09 Coordination Overlaps

- **With Concrete (Div 03):** Slab depressions, FF/FL tolerances, moisture testing. (pe_behavior.md Matrix #1, #20)
- **With Carpentry (Div 06):** Blocking before closure. (pe_behavior.md Matrix #11)
- **With Firestopping (Div 07):** Every penetration through rated partition requires listed firestop system. (pe_behavior.md Matrix #10)
- **With MEP (Div 21–26):** Partition closure sequence — rough-in before second side. Ceiling grid coordination. Plenum adequacy. (pe_behavior.md Matrix #12)
- **With Doors/Frames (Div 08):** Framing must accommodate frame type (wrap-around, welded, slip-on). Wall type must match anchor type.
