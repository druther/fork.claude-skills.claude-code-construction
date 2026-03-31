# Scope File: Division 08 — Openings

**Load when:** Query references doors, door frames, door hardware, access control hardware, windows, curtain wall, storefronts, skylights, glass, glazing, U-factor, SHGC, keying, panic hardware, or any spec section 08 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Sub-Scope 08A: Doors, Frames & Hardware

### Cross-Reference Triggers

- Door schedule — verify every door has mark, size, type, frame type, fire rating, hardware set, finish.
- Hardware schedule — verify every set includes all required items (lockset/latchset, closer, hinges, stops, seals, threshold, viewer, kick plate, signage).
- Architectural plans — door locations with marks matching schedule.
- Architectural details — frame profiles, sill/threshold, transom, sidelight conditions.
- Life safety plans — rated door requirements, exit hardware (panic devices), hold-open devices, automatic closers.
- Spec 08 11 00 — Metal Doors and Frames (hollow metal).
- Spec 08 14 00 — Wood Doors.
- Spec 08 31 00 — Access Doors and Panels.
- Spec 08 71 00 — Door Hardware.
- Spec 08 71 13 — Automatic Door Operators.
- Division 26/28 — Electric hardware power and low-voltage connections (mag locks, electric strikes, auto operators).
- Division 28 — Access control hardware (card readers, REX devices, door position switches).
- ADA — clear width, threshold height, hardware mounting height, closer sweep time.
- **Submittal register** — check for approved door/frame submittals, hardware submittals, and keying schedule.
- **RFI log** — check for RFIs about door ratings, hardware sets, or frame conditions.

### Absence Detection

- [ ] Every door mark on plans has corresponding schedule entry.
- [ ] Every schedule entry has hardware set assigned.
- [ ] Fire-rated doors have rated frames, hardware, and labels (20/45/60/90-min).
- [ ] Rated door hardware includes listed closers, positive latching, no unapproved hold-opens.
- [ ] ADA hardware at accessible doors (levers, thresholds ≤ 1/2", 5-sec minimum sweep).
- [ ] Smoke seals and gasketing at rated doors.
- [ ] Panic hardware at all exit doors per code.
- [ ] Keying schedule or keying conference requirements.
- [ ] Auto operators at accessible entrances.
- [ ] Frame anchoring method per wall type (masonry, metal stud, concrete).
- [ ] Sound-rated doors at acoustically sensitive rooms (STC rating).
- [ ] Access panel schedule for concealed valves, dampers, equipment.
- [ ] Approved hardware submittal with keying information (check register).

### Sequencing Context

```
Frames set during framing (or after masonry, depending on type)
  → Hollow metal frames typically set with stud framing, then drywall wraps to frame
  → Masonry frames set as masonry goes up — must be plumbed and braced
  → POINT OF NO RETURN: Frame type must match wall type
    └── Wrong frame profile for wall condition = field modification or replacement
Door hanging after finishes
  → Hardware installation — long lead for specialty hardware (access control, auto operators)
  → POINT OF NO RETURN: Electric hardware coordination
    ├── Low-voltage wiring to frame from Division 28 must be in wall BEFORE closure
    ├── Power for auto operators must be provided to frame location
    └── Door position switches and REX devices require conduit/cable to frame
```

**Critical timing:** Door hardware is often the last item to be fully resolved (keying conference, access control programming) but the WIRING must be in the walls months earlier. If access control doors are not identified early, the low-voltage rough-in will be missed.

---

## Sub-Scope 08B: Glass & Glazing / Windows / Curtain Wall / Storefronts

### Cross-Reference Triggers

- Architectural elevations — window/CW/storefront locations, configurations, dimensions.
- Window schedule — type, size, operation, glass type, performance requirements.
- Architectural details — head, sill, jamb conditions per type.
- Architectural sections — curtain wall-to-floor slab relationship, spandrel conditions.
- Structural plans — embed/support steel for curtain wall, window lintels, structural openings.
- Spec 08 41 00 — Entrances and Storefronts.
- Spec 08 44 00 — Curtain Wall and Glazed Assemblies.
- Spec 08 50 00 — Windows (aluminum, vinyl, wood, steel).
- Spec 08 80 00 — Glazing.
- Spec 08 62 00 — Unit Skylights.
- Spec 07 92 00 — Joint Sealants (perimeter sealant).
- Spec 07 27 00 — Air Barriers (integration at frames).
- Division 07 — flashing at heads/sills, sill pan flashing.
- Energy code — U-factor, SHGC by orientation and climate zone.
- Wind load requirements from structural engineer (design pressure).
- **Submittal register** — check for approved window/CW/storefront submittals, glazing submittals, and structural calc submittals (delegated design).
- **RFI log** — check for RFIs about details, performance, substitutions, or structural support.

### Absence Detection

- [ ] Window schedule with all types, sizes, and performance requirements.
- [ ] Design pressure (wind load) per exposure condition.
- [ ] Thermal performance (U-factor, SHGC, VLT) per energy code.
- [ ] Glass type specified per location — tempered at all code-required locations (adjacent to doors, within 18" of floor, at guardrails, bathrooms).
- [ ] Sill pan flashing at all punched windows.
- [ ] Curtain wall anchor/embed details on structural drawings.
- [ ] Spandrel panel insulation and firesafing at CW spandrel conditions.
- [ ] Perimeter firesafing at CW/slab edge at each floor.
- [ ] Mock-up and field testing requirements (AAMA 501/503).
- [ ] Acoustical (STC/OITC) performance near noise sources.
- [ ] Blast resistance (if applicable).
- [ ] Approved CW/window submittal with structural calculations (check register).

### Sequencing Context

```
Structural support steel in place (embeds cast in concrete per Div 03/05)
  → CW/storefront anchors surveyed and adjusted to structure
  → POINT OF NO RETURN: Air barrier integration at window frames
    ├── Sill pan flashing installed BEFORE window
    ├── Air barrier terminated and sealed to rough opening BEFORE window installation
    └── Once window is installed, verifying air barrier behind frame is destructive
  → Frames installed, aligned, and anchored
  → Glazing installed
  → Perimeter sealant applied (last step — sealant over backer rod)
  → POINT OF NO RETURN: Perimeter firesafing at each floor
    ├── Firesafing between CW and slab edge at EVERY floor
    ├── Must be installed after CW and before interior finishes cover the slab edge
    └── Missing firesafing = code violation and fire/smoke spread path
```

**Critical timing:** Curtain wall is typically 16–24 weeks from shop drawing approval to first delivery. It is almost always on the critical path. The building cannot be enclosed (and interior finishes cannot begin) until the envelope is substantially complete.

---

## Division 08 Coordination Overlaps

- **With Structural (Div 05):** CW support steel, window lintels, structural openings. (pe_behavior.md Matrix #8, #9)
- **With Air/Vapor Barrier (Div 07):** Continuity from wall assembly into window/CW frame — #1 air leakage location. (pe_behavior.md Matrix #8)
- **With Electrical/LV (Div 26/28):** Power for auto operators, electric locks, access control, motorized shades. (pe_behavior.md Matrix #14)
- **With HVAC (Div 23):** CW spandrel must accommodate diffuser locations. Perimeter heating coordinates with mullion spacing.
- **With Firestopping (Div 07):** Perimeter firesafing at CW/storefront at every floor line. Rated frames with firestopping at wall interface. (pe_behavior.md Matrix #9)
