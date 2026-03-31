# Scope File: Division 33 — Utilities

**Load when:** Query references underground utilities, water service, sanitary sewer, storm sewer, gas service, electrical duct banks, telecom duct banks, fire hydrants, or any spec section 33 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Civil utility plans — water, sanitary, storm, gas, electric, and telecom routing and connections.
- Civil utility profiles — invert elevations, pipe sizes, slopes, materials.
- Spec 33 10 00 — Water Utilities (water main, hydrants, valves).
- Spec 33 30 00 — Sanitary Sewerage Utilities.
- Spec 33 40 00 — Storm Drainage Utilities.
- Spec 33 50 00 — Fuel-Distribution Utilities (gas piping).
- Spec 33 70 00 — Electrical Utilities.
- Spec 33 80 00 — Communications Utilities.
- Division 22 — Plumbing connections at building entry (verify pipe size and invert match).
- Division 26 — Electrical service entrance (verify conduit size and routing match).
- Division 31 — Trench excavation and backfill requirements.
- **Submittal register** — check for approved pipe material, utility connection, and backfill submittals.
- **RFI log** — check for RFIs about utility conflicts, connection locations, or invert elevations.

---

## Absence Detection Checklist

- [ ] Utility connection points and sizes matching between civil and building MEP. (pe_behavior.md Matrix #16)
- [ ] Utility invert elevations at building entry matching plumbing/electrical drawings.
- [ ] Fire hydrant locations per code (spacing, distance from building, access).
- [ ] Utility easement locations identified and respected.
- [ ] Trench backfill and compaction requirements.
- [ ] Pipe material and bedding requirements per utility type.
- [ ] Stormwater management system meeting jurisdictional requirements.
- [ ] Utility permits and AHJ requirements identified.
- [ ] Approved pipe material and connection submittals (check register).

---

## Sequencing Context

Utilities are typically the FIRST site work activity and the LAST thing that can be easily changed.

```
Utility locate (call before you dig — 811)
  → Existing utilities identified and protected
  → POINT OF NO RETURN: Utility routing and connections
    ├── Water main and service tap — utility company coordination required
    ├── Sanitary sewer connection — invert elevation must match building plumbing
    ├── Storm sewer connection — must accommodate site drainage design
    ├── Gas service — utility company installs to meter, contractor from meter to building
    ├── Electrical service — utility company installs primary to transformer
    └── Telecom service — utility company installs to demarc
  → Trench excavation
  → Pipe installation with proper bedding
  → Testing (pressure test for water, mandrel test for sewer, air test as required)
  → Backfill and compaction
  → POINT OF NO RETURN: Backfill over utilities
    └── Post-backfill changes require re-excavation — expensive and disruptive
  → Connection to building at entry points
  → POINT OF NO RETURN: Building entry connections must match EXACTLY
    ├── Water service size on civil must match plumbing
    ├── Sewer invert on civil must match plumbing riser diagram
    ├── Electrical conduit size on civil must match electrical service entrance
    └── Mismatch = field modification at building foundation (costly)
```

**Critical rule:** The utility-to-building interface is one of the most common mismatch points in construction. The civil engineer designs the site utilities. The MEP engineers design the building systems. They are often different firms. Verify that pipe sizes, invert elevations, and connection locations match at every building entry point. (pe_behavior.md Matrix #16)

---

## Coordination Overlaps

- **With Plumbing (Div 22):** Water, sanitary, storm, and gas connections at building entry — size and invert must match. (pe_behavior.md Matrix #16)
- **With Electrical (Div 26):** Electrical service conduit and transformer location.
- **With Earthwork (Div 31):** Trench excavation, backfill, and compaction requirements.
- **With Exterior Improvements (Div 32):** All underground work complete before paving.
- **With Telecom (Div 27):** Incoming service pathway from demarc to building.
