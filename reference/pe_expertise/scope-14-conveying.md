# Scope File: Division 14 — Conveying Equipment

**Load when:** Query references elevators, escalators, dumbwaiters, material lifts, or any spec section 14 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Architectural plans — elevator/escalator locations, pit depths, overhead clearances, machine room locations.
- Architectural details — hoistway sections, cab interior finishes, entrance details.
- Structural plans — hoistway framing, pit depth, machine room floor loading, overhead beam/support steel.
- Spec 14 20 00 — Elevators (traction, hydraulic, MRL).
- Spec 14 30 00 — Escalators and Moving Walks.
- Spec 14 10 00 — Dumbwaiters.
- Division 26 — Elevator electrical service (dedicated feeder, disconnects, cab lighting, emergency power).
- Division 28 — Elevator recall (fire alarm integration, firefighter's service Phase I and II).
- Division 21 — Sprinkler protection in hoistway and machine room (if required by AHJ).
- Division 23 — Machine room ventilation/cooling, hoistway pressurization/ventilation.
- ADA — cab size, door width, control panel height, audible/visual signals.
- **Submittal register** — check for approved elevator shop drawings (these are long-lead and on the critical path).
- **RFI log** — check for RFIs about hoistway dimensions, pit conditions, or fire recall integration.

---

## Absence Detection Checklist

- [ ] Elevator schedule with capacity, speed, travel, stops, door configuration.
- [ ] Hoistway plan and section with all critical dimensions (pit depth, overhead clearance, hoistway dimensions).
- [ ] Machine room or controller room location with ventilation and floor loading.
- [ ] Emergency power provisions (generator, automatic transfer).
- [ ] Fire recall system integration (Phase I and Phase II). (pe_behavior.md Matrix #23)
- [ ] ADA cab size and controls compliance.
- [ ] Seismic requirements (seismic switches, rail bracket spacing).
- [ ] Sump pump in elevator pit. (pe_behavior.md Red Flag §4.4)
- [ ] Pit waterproofing (below-grade pits).
- [ ] Pit ladder per code.
- [ ] Approved elevator shop drawings (check register — 16–24 week lead time typical).

---

## Sequencing Context

```
Hoistway structure complete (concrete or steel shaft walls)
  → Pit waterproofing and sump pump installed
  → POINT OF NO RETURN: Hoistway dimensions
    ├── Hoistway must be plumb and within tolerance for rail installation
    ├── Pit depth and overhead clearance are structural — cannot be changed after pour
    └── Machine room (or controller space for MRL) must be accessible and ventilated
  → Guide rails installed
  → Electrical service and disconnect installed (Div 26)
  → Car and equipment installation (long lead — 16–24 weeks from shop drawing approval)
  → Fire alarm recall wiring and testing (Div 28)
  → Cab finishes (often last — matched to lobby finishes)
  → Inspection and acceptance by AHJ
```

**Critical timing:** Elevators are almost always on the critical path for building occupancy. The certificate of occupancy typically cannot be issued until the elevator passes state inspection. Late elevator delivery = late building turnover.

---

## Coordination Overlaps

- **With Structural (Div 03/05):** Hoistway framing, pit depth, overhead beam, machine room loading.
- **With Electrical (Div 26):** Dedicated feeder, cab lighting, sump pump power. (pe_behavior.md Matrix #23)
- **With Fire Alarm (Div 28):** Phase I/II recall integration. (pe_behavior.md Matrix #23)
- **With HVAC (Div 23):** Machine room ventilation/cooling, hoistway pressurization (high-rise).
- **With Plumbing (Div 22):** Pit sump pump and drain.
- **With Waterproofing (Div 07):** Below-grade pit waterproofing.
