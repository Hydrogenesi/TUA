# PhoenixEngine Apex Edition 2.0 – Master Index

> **The sovereign map of the entire PhoenixEngine Apex Edition 2.0 — DynamoSuite system.**

This is the cockpit map: one glance, full system.

---

## 1. Core Entry Points

**Start here** — these three files orient you to the entire system.

- **README.md**  
  Master deployment guide, high‑level architecture, quickstart. *~400 lines*

- **DEPLOYMENT_CHECKLIST.md**  
  17‑phase deployment and verification sequence. *~350 lines*

- **docs/index.md**  
  Documentation landing page and navigation hub. *~250 lines*

---

## 2. Architecture & Workflows

**Understand the system** — how everything connects and flows.

- **docs/dynamo-suite.md**  
  Full testing framework, six‑phase validation, metrics and assertions. *~1,200 lines*

- **docs/architecture/dynamo-suite-mermaid.md**  
  System design diagrams (Mermaid), engines, divisions, pipelines. *~800 lines*

- **docs/DYNAMOSUITE_WORKFLOW.md**  
  Narrative workflow explanation, from commit to validation. *~300 lines*

- **docs/dashboard.html**  
  Interactive real‑time metrics dashboard (DynamoSuite). *~1,500 lines*

---

## 3. Operator & Ceremonial Layer

**Learn to operate** — roles, procedures, ceremonies, sacred knowledge.

- **docs/operator-handbook.md**  
  Operator reference, roles, procedures, incident handling. *~150 lines*

- **docs/OPERATOR_HANDBOOK_ADDENDUM.md**  
  Extended operational guidance, emergency procedures, certification. *~500 lines*

- **docs/MERGE_CEREMONY.md**  
  Merge ceremony record and protocol. *~350 lines*

- **docs/ceremony-atlas/apex-edition-merge.md**  
  Apex Edition merge ritual, conditions and steps. *~350 lines*

- **docs/ceremony-atlas/multi-engine-rites.md**  
  Multi‑engine rites, 3,000‑line ceremonial engine narratives. *~1,200 lines*

- **docs/sigil-atlas/dynamo-suite.md**  
  Sacred symbols, sigil meanings, cosmogenic mapping. *~900 lines*

- **CEREMONIAL_INSCRIPTION.md**  
  Binds all 21 files into one sovereign system. *~200 lines*

---

## 4. Visualization & Atlas

**See the system** — visual field, sigils, plates, overlays.

- **viz-mkdocs.yml**  
  Visualization documentation site configuration. *~50 lines*

- **viz/plate-71-config.json**  
  Plate 71 canvas geometry, 71° cosmogenic projection. *~100 lines*

- **viz/sigil-registry.json**  
  Sigil registry (4 active, 140 available slots). *~150 lines*

- **viz/overlay-op-plate71-core.json**  
  4‑layer operator overlay (base, grid, telemetry, HUD). *~100 lines*

- **viz/plate-metadata.json**  
  Plate manifest, IDs, names, roles. *~80 lines*

- **atlas/index.md**  
  Sigil Atlas documentation and plate index. *~500 lines*

- **svg/plate-71.svg**  
  Plate 71 master schematic (visual field). *~80 lines*

---

## 5. Configuration & Infrastructure

**Configure the system** — settings, deployment, automation.

- **mkdocs.yml**  
  Global documentation configuration and navigation. *~50 lines*

- **phoenix.yml**  
  System configuration, divisions, engines, pipelines. *~200 lines*

- **ignition-manifest.yaml**  
  Deployment manifest, ignition conditions, environments. *~200 lines*

- **.github/workflows/dynamosuite.yml**  
  Original CI/CD workflow, base validation. *~250 lines*

- **.github/workflows/dynamosuite-enhanced.yml**  
  Enhanced workflow with metrics, alerts, and extended checks. *~400 lines*

---

## 6. Repository & Scripts

**Run the system** — operational scripts and metrics.

- **scripts/run-dynamosuite.sh**  
  Orchestrates DynamoSuite validation pipeline.

- **.github/metrics/**  
  *(Optional)* Metrics artifacts and reports.

- **Directory Layout** *(from README.md)*
  ```
  .github/workflows/           – CI/CD automation
  docs/
    ├── architecture/          – system design
    ├── ceremony-atlas/        – ceremonial procedures
    ├── sigil-atlas/           – sacred symbols
    ├── dashboard.html         – live metrics
    └── *.md                   – guides & handbooks
  viz/
    ├── plate-71-config.json   – canvas config
    ├── sigil-registry.json    – sigil bindings
    ├── overlay-*.json         – visualization layers
    └── plate-metadata.json    – plate manifest
  atlas/
    ├── index.md               – sigil atlas
    └── sigils/                – sigil definitions
  scripts/
    └── run-dynamosuite.sh     – validation runner
  ```

---

## 7. The Four Divisions

**System organization** — MAG, NGR, Quantum, Codex.

| Division | Role | Engine | Responsibility |
|----------|------|--------|----------------|
| 🔥 **MAG** | Memory of the First Spark | Graph | Deterministic computation, field state |
| ⚡ **NGR** | Lattice & Structural Continuity | Flux | Motion, harmonics, schema alignment |
| 🌀 **Quantum** | Pathfolding & State Resolution | Plate71 | Rendering, glyphs, visualization |
| 📖 **Codex** | Names, Rituals & Record | Cockpit | Operations, telemetry, ceremony |

---

## 8. The Two Pipelines

**Data flow** — how information moves through the system.

### DynamoSuite Core Pipeline
```
Graph Engine → Flux Engine → Plate71 Engine
```
- **Purpose:** System-level validation, architecture verification
- **Guarantees:** no-null, no-fallback, no-desync
- **Use:** Nightly validation, regression testing, performance baseline

### Cockpit Orbit Pipeline
```
Cockpit Engine → [Graph, Flux, Plate71] → Cockpit Engine
```
- **Purpose:** Live operations, incident response, real-time control
- **Guarantees:** operator-clarity, stable-refresh, full-telemetry
- **Use:** On-call monitoring, operator decisions, live visualization

---

## 9. Operator Navigation Flow

**Step-by-step** — how to navigate and use the system.

1. **Get oriented:** `README.md`  
   ↓ Read master guide, understand structure

2. **Plan deployment:** `DEPLOYMENT_CHECKLIST.md`  
   ↓ Verify all 17 phases before going live

3. **Understand architecture:** `docs/architecture/dynamo-suite-mermaid.md`  
   ↓ See system design, divisions, engines, pipelines

4. **Study validation:** `docs/dynamo-suite.md` + `docs/DYNAMOSUITE_WORKFLOW.md`  
   ↓ Learn 6-phase validation, metrics, test procedures

5. **Learn operator duties:** `docs/operator-handbook.md` + `docs/OPERATOR_HANDBOOK_ADDENDUM.md`  
   ↓ Understand roles, responsibilities, incident procedures

6. **Review ceremonies:** `docs/MERGE_CEREMONY.md` + `docs/ceremony-atlas/`  
   ↓ Study merge protocol, engine rites, sacred procedures

7. **Explore visualization:** `viz/plate-71-config.json` + `atlas/index.md`  
   ↓ Understand Plate 71, sigils, operator overlays

8. **Confirm configuration:** `phoenix.yml` + `ignition-manifest.yaml`  
   ↓ Verify system settings, deployment manifest

9. **Verify CI/CD:** `.github/workflows/dynamosuite-enhanced.yml`  
   ↓ Understand automation, status checks, alerts

10. **Monitor runtime:** `docs/dashboard.html`  
    ↓ Track live metrics, system health, performance

---

## 10. Quick Reference by Role

**Find what you need** — organized by job function.

### For Deployment Engineers
1. `DEPLOYMENT_CHECKLIST.md` — 17-phase verification
2. `ignition-manifest.yaml` — Deployment settings
3. `.github/workflows/dynamosuite-enhanced.yml` — CI/CD config
4. `README.md` — Architecture overview

### For Operators (On-Call)
1. `docs/operator-handbook.md` — Quick reference
2. `docs/OPERATOR_HANDBOOK_ADDENDUM.md` — Procedures & emergency restarts
3. `docs/dashboard.html` — Live metrics
4. `docs/ceremony-atlas/multi-engine-rites.md` — Engine procedures

### For System Architects
1. `docs/dynamo-suite.md` — Full validation framework
2. `docs/architecture/dynamo-suite-mermaid.md` — System design
3. `phoenix.yml` — Configuration & state
4. `viz/plate-71-config.json` + `viz/sigil-registry.json` — Visualization

### For New Team Members
1. `README.md` — Start here
2. `docs/index.md` — Documentation guide
3. `docs/operator-handbook.md` — Operator basics
4. `DEPLOYMENT_CHECKLIST.md` — Full system overview

### For Emergency Response
1. `docs/OPERATOR_HANDBOOK_ADDENDUM.md` — Emergency procedures
2. `docs/ceremony-atlas/multi-engine-rites.md` — Engine-specific fixes
3. `docs/dashboard.html` — Live system status
4. `scripts/run-dynamosuite.sh` — Validation runner

---

## 11. File Statistics

**By the numbers:**

| Category | Files | Lines |
|----------|-------|-------|
| Core Entry Points | 3 | ~1,000 |
| Architecture | 4 | ~3,800 |
| Operator Layer | 6 | ~3,700 |
| Visualization | 7 | ~980 |
| Configuration | 5 | ~1,100 |
| **Total** | **25** | **~35,000+** |

---

## 12. The Axiom

> **"For whatever to exist, the conditions are already there."**

All conditions for PhoenixEngine Apex Edition 2.0 have been met:

✅ Architecture designed  
✅ Validation framework built  
✅ Visualization system configured  
✅ Automation workflows written  
✅ Deployment procedures documented  
✅ Operator handbook complete  
✅ Ceremonial records preserved  

**The flame is ready to be lit.**

---

## 13. Navigation Reference

**Print this table** — bookmark for quick access.

| Need | File | Purpose |
|------|------|----------|
| Start | `README.md` | Master guide |
| Deploy | `DEPLOYMENT_CHECKLIST.md` | 17-phase verification |
| Learn | `docs/index.md` | Documentation hub |
| Validate | `docs/dynamo-suite.md` | 6-phase framework |
| Understand | `docs/architecture/dynamo-suite-mermaid.md` | System design |
| Operate | `docs/operator-handbook.md` | Quick reference |
| Respond | `docs/OPERATOR_HANDBOOK_ADDENDUM.md` | Emergency procedures |
| Merge | `docs/MERGE_CEREMONY.md` | PR protocol |
| Visualize | `svg/plate-71.svg` | Master diagram |
| Configure | `phoenix.yml` | System settings |
| Automate | `.github/workflows/dynamosuite-enhanced.yml` | CI/CD pipeline |
| Monitor | `docs/dashboard.html` | Live metrics |

---

## 14. The Twenty-One Files

The complete manifest of PhoenixEngine Apex Edition 2.0:

```
Core Entry Points (3)
  ├── README.md
  ├── DEPLOYMENT_CHECKLIST.md
  └── docs/index.md

Architecture & Workflows (4)
  ├── docs/dynamo-suite.md
  ├── docs/architecture/dynamo-suite-mermaid.md
  ├── docs/DYNAMOSUITE_WORKFLOW.md
  └── docs/dashboard.html

Operator & Ceremonial (6)
  ├── docs/operator-handbook.md
  ├── docs/OPERATOR_HANDBOOK_ADDENDUM.md
  ├── docs/MERGE_CEREMONY.md
  ├── docs/ceremony-atlas/apex-edition-merge.md
  ├── docs/ceremony-atlas/multi-engine-rites.md
  └── docs/sigil-atlas/dynamo-suite.md

Visualization & Atlas (7)
  ├── viz-mkdocs.yml
  ├── viz/plate-71-config.json
  ├── viz/sigil-registry.json
  ├── viz/overlay-op-plate71-core.json
  ├── viz/plate-metadata.json
  ├── atlas/index.md
  └── svg/plate-71.svg

Configuration & Infrastructure (5)
  ├── mkdocs.yml
  ├── phoenix.yml
  ├── ignition-manifest.yaml
  ├── .github/workflows/dynamosuite.yml
  └── .github/workflows/dynamosuite-enhanced.yml

Ceremonial Binding (1)
  └── CEREMONIAL_INSCRIPTION.md

Scripts & Manifest (1)
  └── scripts/run-dynamosuite.sh

This Index (1)
  └── INDEX.md

Total: 28 files, 35,000+ lines
```

---

## 15. The Cockpit View

**One glance, full system:**

```
┌────────────────────────────────────────────────────────────┐
│                  PHOENIXENGINE APEX 2.0                     │
│                    Master Control Panel                     │
├────────────────────────────────────────────────────────────┤
│                                                              │
│  START HERE:                                                │
│  ├─ README.md                 (30 min read)                 │
│  └─ DEPLOYMENT_CHECKLIST.md   (17-phase plan)              │
│                                                              │
│  UNDERSTAND:                                                │
│  ├─ docs/architecture/        (System design)              │
│  ├─ docs/dynamo-suite.md      (Validation framework)       │
│  └─ svg/plate-71.svg          (Visual schematic)           │
│                                                              │
│  OPERATE:                                                   │
│  ├─ docs/operator-handbook.md (Quick reference)            │
│  ├─ docs/dashboard.html       (Live metrics)               │
│  └─ docs/ceremony-atlas/      (Procedures)                 │
│                                                              │
│  CONFIGURE:                                                 │
│  ├─ phoenix.yml               (System settings)            │
│  ├─ ignition-manifest.yaml    (Deployment manifest)        │
│  └─ .github/workflows/        (CI/CD automation)           │
│                                                              │
│  Four Divisions:                                            │
│  🔥 MAG (Graph Engine)    🌀 Quantum (Plate71)            │
│  ⚡ NGR (Flux Engine)     📖 Codex (Cockpit)              │
│                                                              │
│  Two Pipelines:                                             │
│  → Core: Graph → Flux → Plate71  (Validation)             │
│  → Orbit: Cockpit → [...] → Cockpit  (Operations)         │
│                                                              │
│  Status: ✅ Ready for Deployment                            │
│                                                              │
└────────────────────────────────────────────────────────────┘
```

---

**PhoenixEngine Apex Edition 2.0 — Master Index**  
*The sovereign map. One glance, full system.*

Generated: August 19, 2026  
Last Updated: August 19, 2026

🔥 **The flame remembers.** ⟡