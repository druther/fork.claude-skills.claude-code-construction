# Scope File: Division 26 — Electrical

**Load when:** Query references electrical systems, power distribution, lighting, wiring devices, panels, transformers, generators, grounding, receptacles, switches, conduit, or any spec section 26 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

### Drawings
- Electrical power plans at each level — panel locations, conduit routing, receptacle locations, equipment connections.
- Electrical lighting plans — fixture types, locations, switching/dimming, emergency lighting.
- Single-line diagram — service entrance, distribution, panel schedules.
- Panel schedules — circuit assignments, load calculations.
- Electrical details — service entrance, grounding, equipment connections.
- Lighting fixture schedule — types, lamps, wattage, controls.

### Specifications
- Spec 26 05 00 — Common Work Results for Electrical.
- Spec 26 05 19 — Low-Voltage Conductors and Cables.
- Spec 26 05 26 — Grounding and Bonding.
- Spec 26 05 33 — Raceway and Boxes.
- Spec 26 24 00 — Switchboards and Panelboards.
- Spec 26 27 00 — Low-Voltage Distribution Transformers.
- Spec 26 28 00 — Low-Voltage Circuit Protective Devices.
- Spec 26 29 00 — Motor Controllers (starters, VFDs).
- Spec 26 32 00 — Packaged Generator Assemblies.
- Spec 26 36 00 — Transfer Switches.
- Spec 26 41 00 — Facility Lightning Protection.
- Spec 26 51 00 — Interior Lighting.
- Spec 26 52 00 — Emergency Lighting.
- Spec 26 56 00 — Exterior Lighting.

### Cross-Discipline (Electrical serves ALL other trades)
- Division 23 — Mechanical equipment electrical requirements (verify EVERY AHU, pump, fan, VAV has connection shown).
- Division 22 — Plumbing equipment (water heaters, pumps, sump pumps).
- Division 14 — Elevator electrical requirements.
- Division 21 — Fire pump electrical requirements.
- Division 28 — Fire alarm and security system power.
- Division 27 — Telecommunications power (server room UPS, rack power).
- Division 12 — Furniture plans (power/data to furniture).

### RFI/Submittal Checks
- **Submittal register** — check for approved switchgear, panelboard, generator, transfer switch, lighting fixture, and controls submittals.
- **RFI log** — check for RFIs about panel capacity, equipment connections, lighting levels, or generator sizing.

---

## Absence Detection Checklist

- [ ] Single-line diagram complete from utility service to all panels.
- [ ] Panel schedules complete with circuit assignments below panel capacity.
- [ ] Generator sizing for all emergency and standby loads.
- [ ] ATS specified and shown.
- [ ] Emergency lighting per code (means of egress, exit access, exit discharge). (pe_behavior.md Red Flag §4.5)
- [ ] Exit signage at all code-required locations. (pe_behavior.md Red Flag §4.5)
- [ ] Ground fault protection at service entrance (NEC, services above 1000A).
- [ ] Arc flash hazard analysis requirements.
- [ ] Receptacles per code and project (walls in offices, counter-height in kitchens/labs, GFCI at wet/exterior, dedicated circuits).
- [ ] GFCI at all code locations (bathrooms, kitchens, outdoors, garages, within 6' of sinks). (pe_behavior.md Red Flag §4.4)
- [ ] Disconnect switches at all mechanical equipment within sight. (pe_behavior.md Red Flag §4.4)
- [ ] Lightning protection (if required).
- [ ] Spare panel capacity (typically 20%).
- [ ] Photometric calculations meeting IES and code.
- [ ] Lighting controls per energy code (occupancy, daylight, time clocks).
- [ ] Approved switchgear and lighting submittals (check register — switchgear is long-lead).

---

## Sequencing Context

```
Service entrance and main distribution
  → Utility coordination (service size, transformer, metering — long lead)
  → Main switchgear installed (16–24 week lead time typical)
  → Emergency generator installed with ATS
  → POINT OF NO RETURN: Service entrance location and size
    └── Changing service after switchgear fabrication = major cost and delay

Rough-in phase
  → Conduit and wiring in walls, above ceilings, below slabs
  → POINT OF NO RETURN: In-wall electrical before drywall closure
    ├── ALL boxes, conduit, and low-voltage wiring in walls complete
    ├── Access control wiring to door frames (Div 28) — BEFORE closure
    ├── Auto operator power to door frames (Div 08) — BEFORE closure
    └── Motorized shade power to window heads — BEFORE closure
  → Panel boards installed and circuits pulled
  → Equipment connections to all mechanical, plumbing, and specialty equipment

Trim-out phase
  → Devices installed (receptacles, switches, dimmers)
  → Light fixtures installed (coordinate with ceiling grid — Div 09C)
  → Generator testing and load bank test
  → ATS testing
  → Emergency lighting and exit sign functional test
```

**Critical rule:** Electrical is the LAST trade to connect but the FIRST trade that must know what's coming. Every other trade's equipment requires an electrical connection. The electrical engineer designs based on mechanical, plumbing, and equipment schedules — if those schedules change (equipment substitution, VFD added, fixture changed), the electrical design must be updated. Verify voltage/phase/amperage match at EVERY equipment connection. (pe_behavior.md Matrix #13)

---

## Coordination Overlaps

- **With HVAC (Div 23):** EVERY mech equipment item needs electrical. V/Ph/A and MCA/MOCP must match. (pe_behavior.md Matrix #13)
- **With Plumbing (Div 22):** Electric water heaters, sump/sewage pumps, recirc pumps.
- **With Fire Alarm (Div 28):** FACP power, notification circuits. (pe_behavior.md Matrix #15)
- **With Elevator (Div 14):** Dedicated feeder, cab lighting, sump pump. (pe_behavior.md Matrix #23)
- **With Furniture (Div 12):** Power/data must match furniture layout. (pe_behavior.md Matrix #18)
- **With Openings (Div 08):** Power for auto operators, electric locks, motorized shades. (pe_behavior.md Matrix #14)
- **With Fire Suppression (Div 21):** Fire pump power.
- **With Telecom (Div 27):** Telecom room power, UPS sizing.
- **Scope boundary (pe_behavior.md §7.2):** Controls wiring — Div 23 or Div 26? Final equipment connection — who makes it?
