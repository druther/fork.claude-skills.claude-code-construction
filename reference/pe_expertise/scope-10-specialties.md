# Scope File: Division 10 — Specialties

**Load when:** Query references toilet accessories, signage, fire extinguishers/cabinets, corner guards, wall/door protection, lockers, toilet partitions, visual display units, or any spec section 10 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Architectural plans and interior elevations — accessory locations and mounting heights.
- Architectural details — accessory mounting, blocking requirements.
- Spec 10 14 00 — Signage (ADA, room ID, wayfinding, exit).
- Spec 10 21 00 — Toilet Compartments.
- Spec 10 28 00 — Toilet, Bath, and Laundry Accessories.
- Spec 10 44 00 — Fire Protection Specialties (extinguishers, cabinets).
- Spec 10 26 00 — Wall and Door Protection (corner guards, bumpers, crash rails).
- Spec 10 51 00 — Lockers.
- Spec 10 11 00 — Visual Display Units (marker boards, tack boards).
- Division 06 — Blocking requirements for all wall-mounted accessories.
- ADA — mounting heights, clear floor space, accessible stall configuration.
- **Submittal register** — check for approved accessory, signage, and toilet partition submittals.
- **RFI log** — check for RFIs about accessory locations, ADA compliance, or mounting details.

---

## Absence Detection Checklist

- [ ] Toilet accessory schedule with quantities matching fixture counts (soap, towel, tissue per fixture).
- [ ] ADA toilet compartment layout with grab bars at correct heights/lengths.
- [ ] Mounting heights per ADA (towel 48" max, mirrors 40" max to bottom, grab bars 33"–36").
- [ ] Fire extinguisher locations per code (75' travel, ADA mounting height).
- [ ] ADA signage at all room/facility ID locations (tactile + Braille, 48"–60" AFF, latch side).
- [ ] Corner guards and wall protection at high-traffic, corridor, and loading areas.
- [ ] Blocking identified for ALL accessories (cross-ref Div 06).
- [ ] Approved accessory and partition submittals (check register).

---

## Sequencing Context

```
Blocking installed during framing (Div 06) — BEFORE drywall closure
  → Drywall complete, painted
  → Toilet partitions installed (floor-mounted or ceiling-hung — verify structural support for ceiling-hung)
  → Accessories installed after paint (last phase of finishes)
  → POINT OF NO RETURN: Blocking
    └── If blocking was missed, accessor installation requires wall opening, blocking, patching, repainting
```

---

## Coordination Overlaps

- **With Carpentry (Div 06):** Every accessory needs a blocking callout. (pe_behavior.md Matrix #11)
- **With Drywall (Div 09):** Locations confirmed before second-side closure.
- **With Plumbing (Div 22):** Fixture counts in toilet rooms match accessory counts.
- **With Electrical (Div 26):** Power for electric hand dryers, heated dispensers, motorized dispensers. (pe_behavior.md §7.2)
