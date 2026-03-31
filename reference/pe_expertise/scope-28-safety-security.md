# Scope File: Division 28 — Electronic Safety & Security

**Load when:** Query references fire alarm, security systems, access control, CCTV, mass notification, intercom, smoke detectors, strobes, pull stations, card readers, or any spec section 28 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Sub-Scope 28A: Fire Detection and Alarm

### Cross-Reference Triggers

- Fire alarm plans — device locations (smoke detectors, heat detectors, pull stations, notification appliances, speakers, strobes).
- Fire alarm riser diagram — system architecture, zones, addressable loops.
- Life safety plans — zone designations, smoke control zones, elevator recall zones.
- Spec 28 31 00 — Fire Detection and Alarm.
- Spec 28 46 00 — Fire Detection and Alarm Annunciation.
- Division 26 — FACP power, notification appliance circuits.
- Division 23 — Duct smoke detectors, fire/smoke damper monitoring, HVAC shutdown integration.
- Division 21 — Sprinkler flow/tamper switch monitoring.
- Division 14 — Elevator recall (Phase I and Phase II).
- Division 08 — Magnetic hold-open devices at rated doors.
- **Submittal register** — check for approved FACP, device, and notification appliance submittals.
- **RFI log** — check for RFIs about device coverage, integration requirements, or annunciator location.

### Absence Detection

- [ ] Device coverage per NFPA 72 (smoke detector spacing, notification appliance candela/dBA per room).
- [ ] Manual pull stations at all exit discharge locations.
- [ ] ADA notification appliances (visual strobes in public/common areas, sleeping rooms, restrooms). (pe_behavior.md Red Flag §4.6)
- [ ] Duct smoke detectors on all AHUs over 2000 CFM. (pe_behavior.md Red Flag §4.4)
- [ ] Integration with: elevator recall, HVAC shutdown, damper closure, door hold-open release, stairwell pressurization.
- [ ] Annunciator at fire department entrance. (pe_behavior.md Red Flag §4.5)
- [ ] Monitoring connection (central station, remote supervision).
- [ ] Emergency communication/mass notification (if required).
- [ ] Approved FACP submittal (check register).

### Sequencing Context

```
FACP installed with power (Div 26) and battery backup
  → Initiating device wiring (detector loops, pull station wiring)
  → Notification appliance circuit wiring
  → POINT OF NO RETURN: Integration wiring to other systems
    ├── Duct smoke detector wiring to AHUs (Div 23)
    ├── Flow/tamper switch wiring from sprinkler system (Div 21)
    ├── Elevator recall wiring (Div 14) — Phase I smoke detectors in lobbies and machine rooms
    ├── Fire/smoke damper monitor/control modules (Div 23)
    ├── Magnetic door hold-open devices (Div 08)
    └── Stairwell pressurization fan control (Div 23)
  → Device installation after finishes (detectors, pull stations, strobes)
  → Head-end programming (zones, sequences, annunciation)
  → System testing and acceptance
  → AHJ inspection
```

---

## Sub-Scope 28B: Access Control & Security

### Cross-Reference Triggers

- Security plans — camera locations, card reader locations, door contacts, intrusion detection.
- Spec 28 10 00 — Access Control.
- Spec 28 20 00 — Video Surveillance.
- Spec 28 30 00 — Electronic Detection and Alarm (intrusion).
- Division 08 — Door hardware for access control (electric strikes/locks, REX, DPS, mag hold-open).
- Division 26 — Security system power.
- **Submittal register** — check for approved access control, CCTV, and intrusion detection submittals.
- **RFI log** — check for RFIs about controlled door locations, camera coverage, or hardware integration.

### Absence Detection

- [ ] Access control at every controlled door: card reader + electric lock/strike + REX + DPS. (pe_behavior.md Matrix #14)
- [ ] CCTV camera coverage at all entry/exit points and critical areas.
- [ ] Intrusion detection zones defined (if applicable).
- [ ] Access control system head-end location with power, network, and HVAC.
- [ ] CCTV storage/server location with adequate power and cooling.
- [ ] Approved access control and CCTV submittals (check register).

### Sequencing Context

```
Low-voltage conduit and wiring in walls during rough-in
  → POINT OF NO RETURN: Access control wiring to door frames BEFORE drywall closure
    ├── Card reader conduit/cable to frame
    ├── Electric lock/strike power to frame
    ├── REX device wiring to frame
    ├── DPS (door position switch) wiring to frame
    └── This is the most commonly missed low-voltage rough-in item
  → CCTV conduit and cable to camera locations
  → Head-end equipment installed
  → Devices installed after finishes
  → Programming and commissioning
```

---

## Division 28 Coordination Overlaps

- **With Door Hardware (Div 08):** Access control requires fully coordinated hardware — electric locks, strikes, REX, DPS. This is one of the most complex coordination zones in construction. (pe_behavior.md Matrix #14)
- **With HVAC (Div 23):** Duct smoke detectors, damper monitoring, HVAC shutdown sequences. (pe_behavior.md Matrix #15)
- **With Fire Suppression (Div 21):** Flow and tamper switch monitoring. (pe_behavior.md Matrix #15)
- **With Elevator (Div 14):** Phase I/II firefighter's recall. (pe_behavior.md Matrix #23)
- **With Electrical (Div 26):** FACP power, battery backup, notification circuits, security system power.
