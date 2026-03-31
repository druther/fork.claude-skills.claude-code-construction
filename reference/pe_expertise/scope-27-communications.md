# Scope File: Division 27 — Communications

**Load when:** Query references telecommunications, data cabling, structured cabling, audio/visual systems, distributed antenna systems, IT infrastructure, WAPs, telecom rooms, or any spec section 27 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Technology plans — data outlet locations, telecom room locations, cable tray routing, backbone pathways.
- Spec 27 10 00 — Structured Cabling.
- Spec 27 15 00 — Communications Horizontal Cabling.
- Spec 27 20 00 — Data Communications.
- Spec 27 41 00 — Audio-Visual Systems.
- Spec 27 51 00 — Distributed Audio-Video Systems.
- Division 26 — Power to telecom rooms, UPS systems, rack power.
- Division 23 — HVAC to telecom/server rooms (dedicated cooling).
- Architectural plans — telecom room sizes and locations, pathway routing.
- Furniture plans — data outlet locations relative to workstation layout.
- **Submittal register** — check for approved structured cabling, AV system, and WAP submittals.
- **RFI log** — check for RFIs about telecom room sizing, pathway routing, or AV requirements.

---

## Absence Detection Checklist

- [ ] Telecom room sizes adequate per TIA/EIA standards.
- [ ] Dedicated HVAC cooling for server/telecom rooms. (pe_behavior.md Red Flag §4.4)
- [ ] Backbone pathway (conduit or cable tray) between telecom rooms per floor.
- [ ] Data outlet quantities and locations matching furniture plans and operational needs.
- [ ] WAP locations shown on plans.
- [ ] AV system rough-in at conference rooms, training rooms, auditoriums.
- [ ] Incoming service entrance pathway (utility conduit from demarc to main telecom room).
- [ ] Telecom grounding and bonding per TIA/ANSI J-STD-607.
- [ ] Approved structured cabling submittal (check register).

---

## Sequencing Context

```
Telecom rooms framed and enclosed
  → Backboards, cable tray, and grounding bus installed
  → POINT OF NO RETURN: Backbone pathways
    ├── Conduit or cable tray between telecom rooms must be in place before ceilings close
    ├── Incoming service conduit from demarc must be installed during underground/rough-in
    └── Sleeves through rated walls/floors for telecom pathways
  → Horizontal cabling pulled (after ceiling grid but before tiles)
  → Outlets terminated
  → AV rough-in at all designated rooms (conduit, boxes, backing)
  → POINT OF NO RETURN: AV rough-in in walls before closure
    ├── Display mount blocking and conduit
    ├── Speaker wire and conduit
    ├── Control system wiring
    └── AV system rough-in is FREQUENTLY missed in the wall closure sequence
  → Testing and certification
```

**Critical rule:** Telecom infrastructure is often under-designed because it is typically a "design-build" or "performance specification" scope. The PE must verify that the skeleton (rooms, pathways, power, cooling) is in the base building design even if the cabling itself is design-build.

---

## Coordination Overlaps

- **With Electrical (Div 26):** Power to all telecom rooms, UPS sizing, dedicated circuits.
- **With HVAC (Div 23):** Cooling load in telecom/server rooms. Dedicated or supplemental cooling required.
- **With Architectural (Div 09):** Telecom room locations, above-ceiling cable tray clearances.
- **With Furniture (Div 12):** Data outlet locations aligned with workstation layout.
