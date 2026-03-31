# Scope File: Division 06 — Wood, Plastics & Composites / Rough Carpentry

**Load when:** Query references wood framing, blocking, sheathing, rough carpentry, architectural woodwork, casework, countertops, plywood, OSB, LVL, glulam, dimensional lumber, FRT, PT lumber, or any spec section 06 XX 00. Also load for any blocking-related query regardless of trade.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Structural plans — wood framing layout, shear wall schedule, hold-down schedule (wood-framed buildings).
- Architectural plans — blocking locations for wall-mounted items (grab bars, handrails, TV mounts, heavy shelving, toilet accessories, marker boards).
- Architectural interior elevations — casework layout, countertop dimensions, backsplash heights.
- Architectural details — casework sections, countertop edge profiles, blocking at special conditions.
- Spec 06 10 00 — Rough Carpentry (framing, blocking, sheathing, FRT lumber, PT lumber).
- Spec 06 16 00 — Sheathing.
- Spec 06 40 00 — Architectural Woodwork (casework, paneling, trim).
- Spec 06 17 00 — Shop-Fabricated Structural Wood (trusses, glulam, CLT).
- Spec 06 60 00 — FRP panels.
- Spec 12 30 00 — Casework (may be Division 12 instead of 06 — check both).
- Spec 12 36 00 — Countertops.
- Plumbing plans — fixture locations requiring countertop cutouts.
- Electrical plans — outlet locations relative to countertop/backsplash heights.
- **Submittal register** — check for approved casework shop drawings, countertop samples, and wood treatment certifications.
- **RFI log** — check for RFIs about blocking locations, casework dimensions, or countertop materials.

---

## Absence Detection Checklist

- [ ] Blocking plan or notes identifying ALL locations requiring wood blocking in metal stud walls.
- [ ] FRT lumber specified where required (wood in rated assemblies, wood blocking in noncombustible construction).
- [ ] PT lumber specified for all ground-contact and exterior-exposed applications.
- [ ] Countertop material, edge profile, and backsplash height specified.
- [ ] Casework grade specified (AWI Economy, Custom, or Premium).
- [ ] Plywood/sheathing grade and exposure rating specified.
- [ ] Blocking heights specified for each accessory type (grab bars, accessories, equipment).
- [ ] Approved casework shop drawings (check register).

---

## Sequencing Context

```
Metal stud framing complete (first side)
  → POINT OF NO RETURN: BLOCKING INSTALLATION
    ├── Grab bar blocking in ALL accessible toilet rooms (33"–36" AFF, extending beyond bar ends)
    ├── Toilet accessory blocking at all locations (Div 10)
    ├── TV mount blocking at specified locations
    ├── Casework support blocking at all wall-mounted cabinet locations
    ├── Marker board / tack board blocking
    ├── Handrail bracket blocking at all wall-mounted railing locations
    └── Any other wall-mounted items requiring structural support
  → MEP rough-in alongside/around blocking
  → Second-side drywall closes the wall — blocking is now inaccessible
```

**Critical rule:** Blocking is the single most commonly missed item in commercial construction. It costs $20 to install during framing and $2,000 to retrofit after drywall. The blocking plan must be a comprehensive master list assembled from architectural plans, interior elevations, toilet room details, Division 10 accessory schedules, and Division 12 casework drawings — no single drawing shows all blocking locations.

---

## Coordination Overlaps

- **With Drywall (Div 09):** Blocking must be in place before closure. ALL wall-mounted item locations identified with sizes/heights. (pe_behavior.md Matrix #11)
- **With Plumbing (Div 22):** Countertop cutouts for sinks, faucet holes, soap dispensers.
- **With Electrical (Div 26):** Outlet and switch locations relative to casework and countertop heights. ADA counter heights aligned with outlet placement.
- **With Specialties (Div 10):** Blocking for ALL accessories — grab bars, mirrors, dispensers, hand dryers.
