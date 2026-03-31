# Scope File: Division 11 — Equipment

**Load when:** Query references commercial kitchen equipment, foodservice, laundry equipment, athletic equipment, laboratory equipment, or any project-specific equipment per spec section 11 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Architectural plans — equipment room layouts, clearances, service access.
- Equipment schedule — manufacturer, model, utility requirements (gas, water, waste, electric), weight.
- Spec 11 40 00 — Foodservice Equipment.
- Spec 11 30 00 — Residential/Commercial Laundry Equipment.
- Spec 11 60 00 — Laboratory Equipment.
- Spec 11 66 00 — Athletic and Recreational Equipment.
- Structural plans — floor loading, housekeeping pad sizes, vibration isolation supports.
- Division 22 — Plumbing connections (water, waste, grease waste, floor drains near equipment).
- Division 23 — HVAC requirements (exhaust hoods, make-up air, equipment cooling loads).
- Division 26 — Electrical connections (voltage, amperage, phase, receptacle type, dedicated circuits).
- Division 21 — Fire suppression at commercial kitchen hoods (Ansul/wet chemical).
- **Submittal register** — check for approved equipment submittals with utility requirement confirmation.
- **RFI log** — check for RFIs about equipment utility requirements, clearances, or substitutions.

---

## Absence Detection Checklist

- [ ] Equipment schedule complete with all items and utility requirements.
- [ ] Structural floor loading verified for heavy equipment.
- [ ] Utility rough-in locations coordinated with equipment connection points.
- [ ] Equipment clearances verified (service access, code, ADA reach ranges).
- [ ] Exhaust hood and make-up air system designed for kitchen heat loads.
- [ ] Fire suppression under commercial kitchen hoods. (pe_behavior.md Matrix #22)
- [ ] Vibration isolation for rotating/compressor equipment.
- [ ] OFCI/OFOI/contractor-furnished clearly designated.
- [ ] Approved equipment submittals with utility confirmation (check register).

---

## Sequencing Context

```
Utility rough-in during MEP rough-in phase
  → POINT OF NO RETURN: Rough-in locations must match equipment connection points
    ├── Gas stub-out location and size per equipment schedule
    ├── Water supply and waste connections per equipment schedule
    ├── Electrical receptacle or hardwire connection per equipment schedule
    └── Exhaust hood duct connection per equipment schedule
  → Slab/floor complete
  → Equipment delivery and setting (often late in schedule — verify delivery timeline)
  → Final connections by each MEP trade
  → POINT OF NO RETURN: OFCI equipment — Owner procurement timeline must align with project schedule
```

**Critical rule:** Kitchen equipment is the most complex equipment coordination on most projects. Every piece has unique utility requirements (voltage, gas BTU, water supply size, waste pipe size, ventilation CFM). A single equipment substitution can cascade to all four MEP trades.

---

## Coordination Overlaps

- **With Structural (Div 03/05):** Equipment loads, housekeeping pads, floor reinforcement. (pe_behavior.md Matrix #17)
- **With All MEP (Div 21–26):** Every equipment item has utility requirements. (pe_behavior.md Matrix #17)
- **With Fire Suppression (Div 21):** Commercial hood suppression. (pe_behavior.md Matrix #22)
- **With Division 01:** OFCI/OFOI delivery and installation responsibilities.
