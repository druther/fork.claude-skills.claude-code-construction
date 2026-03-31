# Scope File: Division 22 — Plumbing

**Load when:** Query references plumbing fixtures, piping, water heaters, roof drains, sanitary waste, storm drainage, gas piping, backflow preventers, grease interceptors, or any spec section 22 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

### Drawings
- Plumbing plans at each level — fixture locations, pipe routing, riser diagrams.
- Plumbing fixture schedule — types, manufacturers, model numbers, connections.
- Plumbing details and riser diagrams — pipe sizes, water heater connections, backflow prevention.
- Architectural plans — fixture locations, toilet room layouts (verify plumbing matches arch fixture counts and locations).
- Architectural details — countertop cutouts for sinks, floor drain locations in wet areas.
- Structural plans — floor/wall penetrations, slab depressions for showers and floor drains.
- Civil/site plans — water service entry, sanitary sewer connection, storm sewer connection, grease interceptor location.

### Specifications
- Spec 22 05 00 — Common Work Results for Plumbing.
- Spec 22 10 00 — Plumbing Piping.
- Spec 22 11 00 — Facility Water Distribution (domestic hot and cold).
- Spec 22 13 00 — Facility Sanitary Sewerage.
- Spec 22 14 00 — Facility Storm Drainage.
- Spec 22 30 00 — Plumbing Specialties (cleanouts, floor drains, interceptors, backflow preventers, expansion tanks).
- Spec 22 34 00 — Fuel-Fired Domestic Water Heaters.
- Spec 22 40 00 — Plumbing Fixtures (WC, lavs, sinks, urinals, DFs, showers).
- Spec 22 11 16 — Domestic Water Piping Insulation.
- Division 26 — Electrical connections for water heaters, recirculation pumps, electric fixtures.
- Division 23 — Piping routing coordination with ductwork in shared ceiling spaces.
- ADA — Accessible fixture mounting heights, insulated undersink piping, accessible DF provisions.

### RFI/Submittal Checks
- **Submittal register** — check for approved fixture submittals, water heater submittals, piping material submittals, and backflow preventer submittals.
- **RFI log** — check for RFIs about fixture selections, pipe routing, floor drain locations, or gas piping.

---

## Absence Detection Checklist

- [ ] Plumbing fixture schedule matching all fixtures on plans.
- [ ] Fixture counts matching architectural plans (every WC, lav, urinal, sink, DF, hose bibb on arch = on plumbing). (pe_behavior.md Matrix #21)
- [ ] Domestic hot water system type and capacity (water heater schedule).
- [ ] Hot water recirculation system (required per code for most commercial buildings).
- [ ] Backflow prevention at all code-required locations (domestic entry, irrigation, boiler fill, process).
- [ ] Floor drains at code-required locations (mech rooms, water heater rooms, toilet rooms — check local code). (pe_behavior.md Red Flag §4.4)
- [ ] Cleanouts per code (base of stacks, direction changes, mandated spacing).
- [ ] Roof drain sizing and overflow drain provisions.
- [ ] Grease interceptor/trap for food service (sized per local code).
- [ ] Gas piping to all gas-fired equipment (water heaters, boilers, kitchen equipment, generator).
- [ ] Insulation on DHW piping, chilled water piping, condensation-prone piping.
- [ ] ADA fixtures (17"–19" WC seat height, insulated undersink piping, knee clearance at lavs).
- [ ] Hose bibbs and wall hydrants at exterior and interior locations.
- [ ] Sanitary and storm riser diagrams with pipe sizing.
- [ ] Approved fixture and water heater submittals (check register).

---

## Sequencing Context

```
Underground/underslab plumbing
  → POINT OF NO RETURN: All underslab waste and vent piping installed BEFORE slab pour
    ├── Sanitary waste lines below SOG
    ├── Storm drainage below SOG
    ├── Floor drain bodies set to correct elevation (flush with finished floor, accounting for flooring thickness)
    └── Verify locations match architectural plans — post-pour relocation requires saw-cutting
  → (See pe_behavior.md §3.2 Slab-on-Grade Sequence)

Rough-in phase (in-wall and above-ceiling)
  → Water supply, waste, and vent piping roughed in
  → Roof drain bodies set (coordinates with roofing — Div 07C)
  → Gas piping roughed in and tested
  → POINT OF NO RETURN: Piping in walls before second-side drywall
    └── All in-wall piping complete and tested before closure

Trim-out phase (after finishes)
  → Fixtures set (WC, lavs, sinks, DFs)
  → Faucets and trim installed
  → Final connections to equipment (water heaters, kitchen equipment)
  → System testing, balancing, and disinfection
```

**Critical coordination:** Roof drain bodies must be set by the plumber BEFORE the roofer can tie in the membrane at drain locations. If the plumber is not scheduled ahead of the roofer, roofing cannot be completed at drain locations. This is a frequently missed two-trade dependency.

---

## Coordination Overlaps

- **With Architectural (Div 09):** Fixture locations must match. Countertop cutouts for sinks. Slab depressions at showers and recessed drains. (pe_behavior.md Matrix #21)
- **With Structural (Div 03/05):** Floor/wall penetrations, underslab routing, post-tensioning conflicts.
- **With HVAC (Div 23):** Piping and ductwork in shared ceiling spaces — verify clearance. Condensate drain connections.
- **With Fire Suppression (Div 21):** Combined vs. separate domestic/fire water at building entry.
- **With Kitchen Equipment (Div 11):** Utility rough-in for all kitchen equipment. (pe_behavior.md Matrix #17)
- **With Electrical (Div 26):** Power for water heaters, recirc pumps, sump pumps, sewage ejectors.
- **With Roofing (Div 07C):** Roof drain body placement before roofing membrane tie-in. (pe_behavior.md Matrix #19)
