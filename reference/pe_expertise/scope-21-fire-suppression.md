# Scope File: Division 21 — Fire Suppression

**Load when:** Query references fire sprinklers, standpipes, fire pumps, clean agent systems, fire suppression piping, FDC, sprinkler heads, or any spec section 21 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

### Drawings
- Life safety plans — sprinkler coverage zones, hazard classification by area (light, ordinary, extra hazard).
- Architectural plans — room layouts (head placement and coverage).
- RCPs — sprinkler head locations relative to ceiling grid, light fixtures, diffusers.
- Structural plans — member depths (clearance for mains above structure).
- Civil/site plans — FDC location, water service and main size.

### Specifications
- Spec 21 10 00 — Water-Based Fire-Suppression Systems.
- Spec 21 12 00 — Fire-Suppression Standpipes.
- Spec 21 13 00 — Fire-Suppression Sprinkler Systems.
- Spec 21 22 00 — Clean-Agent Fire Extinguishing Systems.
- Spec 21 30 00 — Fire Pumps.
- Division 26 — Fire pump electrical service, jockey pump, controller power.
- Division 28 — Fire alarm integration (flow switches, tamper switches, supervisory signals).

### RFI/Submittal Checks
- **Submittal register** — check for approved sprinkler shop drawings (hydraulic calculations, head layout), fire pump submittal, and clean agent system submittals.
- **RFI log** — check for RFIs about hazard classification, head type/coverage, or FDC location.

---

## Absence Detection Checklist

- [ ] Design criteria specified (density, area of application, hazard classification per space).
- [ ] System type per area (wet, dry, pre-action, deluge).
- [ ] Head type per condition (concealed in finished spaces, upright in unfinished, sidewall where noted).
- [ ] Fire pump sizing and location (if required by hydraulic calculations).
- [ ] Standpipe locations per code (stairways, roof, hose connections).
- [ ] FDC location on site plan and architectural plans.
- [ ] Coverage in all concealed spaces per code (above ceilings, below stages, closets).
- [ ] Clean agent system for server/telecom rooms (if applicable).
- [ ] Approved sprinkler shop drawings with hydraulic calculations (check register).

---

## Sequencing Context

```
Underground water service and fire main installed (Div 33)
  → Fire pump installed (if required) with electrical service (Div 26)
  → Sprinkler risers and mains installed
  → POINT OF NO RETURN: Main routing above structure
    ├── Mains must clear structural members — verify clearance
    ├── Mains and ductwork share plenum space — verify no conflicts with Div 23
    └── Main routing affects ceiling height — verify adequate plenum dimension
  → Branch lines installed after ceiling grid layout is coordinated
  → Heads installed — concealed heads require specific ceiling tile openings
  → System testing and flushing
  → POINT OF NO RETURN: Flow/tamper switch monitoring by fire alarm (Div 28)
    └── System cannot be placed in service until monitored by fire alarm
  → AHJ inspection
```

**Critical coordination:** Sprinkler head layout is the last piece of the ceiling coordination puzzle. Heads must clear ceiling grid members, avoid light fixtures and diffusers, and meet coverage spacing requirements simultaneously. This often requires multiple coordination iterations.

---

## Coordination Overlaps

- **With Structural (Div 05):** Main routing above/through structural members. (pe_behavior.md §4.4)
- **With Ceilings (Div 09):** Head locations coordinated with grid layout. (pe_behavior.md Matrix #12)
- **With HVAC (Div 23):** Mains and ductwork share plenum — verify clearances.
- **With Fire Alarm (Div 28):** Every zone requires flow/tamper switch monitoring. (pe_behavior.md Matrix #15)
- **With Kitchen Equipment (Div 11):** Commercial hood fire suppression is SEPARATE from building sprinkler. (pe_behavior.md Matrix #22)
- **With Plumbing (Div 22):** Combined vs. separate domestic/fire water service — verify at building entry.
