# Scope File: Division 12 — Furnishings

**Load when:** Query references furniture, window treatments, casework (if specified in Div 12 rather than 06), countertops, rugs/mats, site furnishings, or any spec section 12 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Furniture plans — layout, types, power/data requirements.
- Spec 12 20 00 — Window Treatment (blinds, shades).
- Spec 12 30 00 — Casework.
- Spec 12 36 00 — Countertops.
- Spec 12 48 00 — Rugs and Mats.
- Spec 12 50 00 — Furniture.
- Spec 12 93 00 — Site Furnishings.
- Division 26 — Power/data outlets coordinated with furniture layout.
- ADA — accessible workstation and counter heights.
- **Submittal register** — check for approved furniture, casework, and window treatment submittals.
- **RFI log** — check for RFIs about furniture layout, power/data coordination, or ADA compliance.

---

## Absence Detection Checklist

- [ ] Furniture plan provided for all occupied spaces.
- [ ] Power/data outlet locations coordinated with furniture plan. (pe_behavior.md Matrix #18)
- [ ] ADA-accessible workstations/counters at required quantities.
- [ ] Window treatment mounting details and blocking (cross-ref Div 06).
- [ ] OFCI/OFOI designations clear for all items.
- [ ] Approved furniture and casework submittals (check register).

---

## Sequencing Context

```
Electrical rough-in based on furniture plan (Div 26)
  → POINT OF NO RETURN: Outlet locations in floor and walls
    └── System furniture power entry points MUST match outlet locations — misalignment = useless outlets
  → Finishes complete (paint, flooring, ceilings)
  → Furniture delivery and installation (last activity before occupancy)
  → Window treatment installation (after painting, before furniture — access needed)
```

---

## Coordination Overlaps

- **With Electrical (Div 26):** Outlet locations must match furniture plan. (pe_behavior.md Matrix #18)
- **With Carpentry (Div 06):** Blocking for window treatments and wall-mounted casework.
- **With Plumbing (Div 22):** Countertop cutouts for sinks if casework is in Div 12.
