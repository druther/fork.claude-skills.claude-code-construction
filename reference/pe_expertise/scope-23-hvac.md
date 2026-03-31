# Scope File: Division 23 — HVAC

**Load when:** Query references heating, ventilation, air conditioning, ductwork, mechanical equipment, AHU, RTU, VAV, thermostats, BAS, building automation, diffusers, grilles, exhaust fans, chillers, boilers, or any spec section 23 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

### Drawings
- Mechanical plans at each level — equipment locations, duct routing, piping routing, diffuser/grille locations.
- Mechanical schedules — AHU, RTU, fan coil, VAV, exhaust fan, pump schedules with capacities and utility requirements.
- Mechanical details and sections — duct sizes at tight conditions, equipment connections, piping details.
- Mechanical riser diagrams — chilled water, hot water, refrigerant, steam (if applicable).
- RCPs — diffuser and return grille locations (verify mechanical plans match RCP).
- Structural plans — equipment loads, roof curbs/dunnage, floor/wall/roof penetrations.
- Architectural plans — room layouts for ventilation requirements, ceiling heights for ductwork routing.

### Specifications
- Spec 23 05 00 — Common Work Results for HVAC.
- Spec 23 07 00 — HVAC Insulation.
- Spec 23 09 00 — Instrumentation and Control (BAS/BMS, DDC, thermostats, sensors).
- Spec 23 21 00 — Hydronic Piping and Pumps.
- Spec 23 23 00 — Refrigerant Piping.
- Spec 23 31 00 — HVAC Ducts and Casings.
- Spec 23 33 00 — Air Duct Accessories (dampers, access doors, turning vanes).
- Spec 23 34 00 — HVAC Fans.
- Spec 23 36 00 — Air Terminal Units (VAV boxes).
- Spec 23 37 00 — Air Outlets and Inlets (diffusers, grilles, registers).
- Spec 23 64 00 — Packaged Water Chillers.
- Spec 23 73 00 — Indoor Central-Station AHUs.
- Spec 23 74 00 — Packaged Outdoor AHUs.
- Spec 23 81 00 — Decentralized Unitary Equipment (splits, PTACs, heat pumps).
- Division 26 — Electrical connections for ALL mechanical equipment, VFDs, disconnects.
- Division 28 — Fire/smoke damper locations, duct smoke detector locations.
- Energy code — ventilation rates, efficiency, economizer requirements.
- Commissioning plan (if applicable).

### RFI/Submittal Checks
- **Submittal register** — check for approved equipment submittals (AHUs, RTUs, VAVs, chillers, boilers, pumps, fans), ductwork submittals, controls/BAS submittals, and diffuser/grille submittals.
- **RFI log** — check for RFIs about equipment sizing, duct routing, control sequences, or ventilation rates.

---

## Absence Detection Checklist

- [ ] Equipment schedule complete with all equipment shown on plans.
- [ ] Supply, return, and exhaust CFM values per space (per ASHRAE 62.1 or local code).
- [ ] Outdoor air ventilation rates per ASHRAE 62.1 or applicable code.
- [ ] Ductwork sizing on plans (or "size by contractor" with design criteria).
- [ ] Fire/smoke dampers at all rated wall and floor penetrations (match life safety plans). (pe_behavior.md Red Flag §4.4)
- [ ] Access doors at all dampers, VAV boxes, coils, and filters. (pe_behavior.md Red Flag §4.4)
- [ ] Duct insulation and lining per application (supply, exterior, return).
- [ ] Vibration isolation for all rotating equipment.
- [ ] Equipment maintenance clearance (per manufacturer and code).
- [ ] Thermostat/sensor locations (avoid exterior walls, sunlight, heat sources).
- [ ] BAS control sequences specified.
- [ ] TAB requirements specified.
- [ ] Commissioning scope defined.
- [ ] Kitchen exhaust and make-up air (if commercial kitchen present).
- [ ] Toilet room and janitor closet exhaust per code.
- [ ] Mechanical room ventilation (cooling and combustion air).
- [ ] Approved equipment submittals with electrical data confirmation (check register).

---

## Sequencing Context

```
Structural framing complete
  → Rooftop equipment curbs/dunnage installed (who provides — Div 23 or Div 07? See pe_behavior.md §7.2)
  → Major equipment set (AHUs, RTUs, chillers, boilers)
  → POINT OF NO RETURN: MEP hangers before fireproofing (Div 07D)
    └── All duct/pipe hangers attached to structure BEFORE SFRM

Above-ceiling rough-in
  → Main ductwork installed
  → Branch ductwork to VAV boxes
  → Hydronic piping installed
  → POINT OF NO RETURN: Duct routing determines plenum space
    ├── Ductwork clearance above ceiling grid — verify adequate plenum dimension
    ├── Ductwork cannot conflict with sprinkler mains, plumbing, electrical
    └── Diffuser locations coordinated with ceiling grid BEFORE grid installation
  → Fire/smoke dampers installed at ALL rated penetrations
  → Access doors installed at ALL dampers, VAVs, coils, filters

Controls and commissioning
  → BAS/DDC controllers installed and wired
  → Sensors and thermostats installed
  → System startup and TAB
  → Functional performance testing (commissioning)
  → POINT OF NO RETURN: BAS programming must match control sequences in spec
    └── Incorrect sequences = building doesn't perform as designed (energy, comfort, safety)
```

**Critical coordination:** The mechanical-electrical interface is the most commonly miscoordinated item on commercial projects. EVERY piece of mechanical equipment requires an electrical connection, and the voltage/phase/amperage on the mechanical schedule must EXACTLY match the electrical panel schedule and single-line diagram. A mismatch discovered at startup = expensive re-work. (pe_behavior.md Matrix #13)

---

## Coordination Overlaps

- **With Structural (Div 03/05):** Equipment loads, curbs/dunnage, penetrations, clearance for duct routing. 
- **With Ceilings (Div 09):** Diffuser/grille locations on grid. Plenum adequacy. (pe_behavior.md Matrix #12)
- **With Electrical (Div 26):** EVERY equipment item needs electrical. Verify V/Ph/A and disconnect for each. (pe_behavior.md Matrix #13)
- **With Plumbing (Div 22):** Condensate drains, piping routing in shared spaces.
- **With Fire Alarm (Div 28):** Duct smoke detectors, damper monitoring, HVAC shutdown on alarm. (pe_behavior.md Matrix #15)
- **With Fire Suppression (Div 21):** Mains and ductwork share plenum — verify clearances.
- **With Openings (Div 08):** CW spandrel conditions, louver locations for OA intake/exhaust/relief.
- **Scope boundary (pe_behavior.md §7.2):** Roof curb responsibility. Controls wiring responsibility (Div 23 vs. Div 26).
