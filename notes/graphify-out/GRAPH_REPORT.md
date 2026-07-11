# Graph Report - /opt/data/obsidian-vault/notes  (2026-06-27)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 42 nodes · 28 edges · 21 communities (5 shown, 16 thin omitted)
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]

## God Nodes (most connected - your core abstractions)
1. `Navigator (COO)` - 9 edges
2. `Marketer (CMO)` - 4 edges
3. `Shared Google Drive` - 4 edges
4. `Production Agent` - 3 edges
5. `Finance Agent (CFO)` - 3 edges
6. `Ruslan (Sales/Designer)` - 3 edges
7. `Shared Obsidian Vault` - 3 edges
8. `JNN Factory Architecture (2026-06-12)` - 2 edges
9. `Google Drive Audit Report` - 2 edges
10. `Sales Agent` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Navigator (COO)` --references--> `Shared Google Drive`  [EXTRACTED]
  Агенты.md → JNN-Architecture-2026-06-12.md
- `Nurlan (CEO)` --calls--> `Navigator (COO)`  [EXTRACTED]
  Команда.md → Агенты.md
- `JNN Communication Protocol v1.0` --references--> `Shared Google Drive`  [EXTRACTED]
  COMMUNICATION-PROTOCOL-v1.md → JNN-Architecture-2026-06-12.md
- `JNN Factory Architecture (2026-06-12)` --references--> `Shared Obsidian Vault`  [EXTRACTED]
  JNN-Architecture-2026-06-12.md → Obsidian-Vault-Назначение.md
- `Memory Upgrade (2026-06-03)` --references--> `Shared Obsidian Vault`  [EXTRACTED]
  Апгрейд-памяти-2026-06-03.md → Obsidian-Vault-Назначение.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **JNN Agent Orchestration Flow** — agent_navigator, agent_marketer, agent_sales, agent_production, agent_finance, agent_hr, agent_rop, agent_habit [EXTRACTED 0.95]
- **JNN Data Synchronization Pattern** — google_drive_shared, obsidian_vault_shared, jnn_dashboard [EXTRACTED 0.90]
- **IT Services Sales & Delivery Flow** — human_ruslan, human_nurlan, agent_navigator, it_services_readme, ruslan_it_instruction [EXTRACTED 0.85]

## Communities (21 total, 16 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.29
Nodes (7): Marketer (CMO), Production Agent, ROP Agent (Sales Director), Aigerim (Marketing/Sales), Timur (Marketing/Production), Marketing Overview, Production Overview

### Community 1 - "Community 1"
Cohesion: 0.40
Nodes (6): JNN Communication Protocol v1.0, Google Drive Audit Report, Shared Google Drive, JNN Factory Architecture (2026-06-12), Memory Upgrade (2026-06-03), Shared Obsidian Vault

### Community 2 - "Community 2"
Cohesion: 0.40
Nodes (5): Habit Control Agent, HR Agent, Navigator (COO), HR Overview, Nurlan (CEO)

### Community 3 - "Community 3"
Cohesion: 0.50
Nodes (4): Sales Agent, Ruslan (Sales/Designer), IT Services README, IT Sales Instruction for Ruslan

### Community 4 - "Community 4"
Cohesion: 0.67
Nodes (3): Finance Agent (CFO), Finance Overview, Alina (Finance)

## Knowledge Gaps
- **26 isolated node(s):** `JNN Communication Protocol v1.0`, `Google Cloud Setup`, `JNN Obsidian Vault Purpose`, `AI-Agents JNN`, `Memory Upgrade (2026-06-03)` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Navigator (COO)` connect `Community 2` to `Community 0`, `Community 1`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.289) - this node is a cross-community bridge._
- **Why does `Shared Google Drive` connect `Community 1` to `Community 2`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Why does `Sales Agent` connect `Community 3` to `Community 2`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `Navigator (COO)` (e.g. with `Finance Agent (CFO)` and `Habit Control Agent`) actually correct?**
  _`Navigator (COO)` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `JNN Communication Protocol v1.0`, `Google Cloud Setup`, `JNN Obsidian Vault Purpose` to the rest of the system?**
  _28 weakly-connected nodes found - possible documentation gaps or missing edges._