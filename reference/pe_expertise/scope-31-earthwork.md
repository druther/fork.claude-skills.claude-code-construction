# Scope File: Division 31 — Earthwork

**Load when:** Query references excavation, fill, grading, compaction, soil stabilization, dewatering, shoring, underpinning, piles, caissons, ground improvement, or any spec section 31 XX 00.

**Red flags and coordination matrix are in pe_behavior.md (always loaded).**

---

## Cross-Reference Triggers

- Civil grading and drainage plans — existing and proposed grades, cut/fill quantities.
- Geotechnical report — bearing capacity, fill requirements, compaction specs, groundwater, dewatering.
- Structural foundation plans — foundation depths, footing elevations.
- Spec 31 10 00 — Site Clearing.
- Spec 31 20 00 — Earth Moving.
- Spec 31 23 00 — Excavation and Fill.
- Spec 31 25 00 — Erosion and Sedimentation Controls.
- Spec 31 50 00 — Excavation Support and Protection (shoring, underpinning).
- Spec 31 60 00 — Special Foundations and Load-Bearing Elements (piles, caissons, ground improvement).
- Division 33 — Underground utility locations affecting excavation.
- Division 07 — Below-grade waterproofing (backfill material/compaction adjacent to waterproofed walls).
- **Submittal register** — check for approved shoring design, fill material certifications, and pile/caisson installation plans.
- **RFI log** — check for RFIs about soil conditions, bearing capacity, or dewatering.

---

## Absence Detection Checklist

- [ ] Geotechnical report referenced and recommendations incorporated.
- [ ] Fill material specs (gradation, moisture content, compaction requirements).
- [ ] Compaction testing requirements and acceptance criteria.
- [ ] Dewatering plan (if groundwater above excavation bottom).
- [ ] Erosion and sedimentation control plan (SWPPP if applicable).
- [ ] Excavation support (shoring) for excavations adjacent to structures/utilities.
- [ ] Subgrade preparation requirements under slabs and pavements.
- [ ] Special inspection for deep foundations (piles, caissons) if applicable.
- [ ] Approved fill material and shoring submittals (check register).

---

## Sequencing Context

Earthwork is the foundation of everything — literally.

```
Site clearing and erosion controls
  → Erosion and sedimentation controls in place BEFORE any disturbance
  → POINT OF NO RETURN: Shoring design and installation
    ├── Shoring must be designed and installed BEFORE excavation below adjacent footings/utilities
    ├── Underpinning of adjacent structures if required by proximity
    └── Dewatering system operational before excavation below water table
  → Excavation to subgrade
  → Subgrade verification by geotechnical engineer (bearing capacity confirmation)
  → POINT OF NO RETURN: Subgrade acceptance
    └── If subgrade fails verification, remediation (over-excavation, compaction, ground improvement) required before foundations
  → Foundation construction begins (Div 03)
  → Backfill after foundation and waterproofing
  → POINT OF NO RETURN: Backfill at waterproofed walls
    ├── Waterproofing, protection board, and drainage must be complete BEFORE backfill
    ├── Backfill material must not damage membrane (no large rocks, no heavy compaction against wall)
    └── Foundation drain installed BEFORE backfill covers it
```

---

## Coordination Overlaps

- **With Concrete (Div 03):** Subgrade under SOG. Foundation excavation depths.
- **With Utilities (Div 33):** Underground utilities located before excavation. Trench backfill requirements.
- **With Waterproofing (Div 07):** Backfill protection of waterproofed walls. (pe_behavior.md Matrix #4)
