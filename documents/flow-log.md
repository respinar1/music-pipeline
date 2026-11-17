> # **Flow Log Document**
> ## **Intention:**
> This document will be used to track my "flow state" framework for each goal as I complete this project. Will help getting back on track if I take hiatus.

> ## **Framework:**
> - **Goal:**
>   - Goal set and completion testing.
> - **Reasoning:**
>   - Why the goal matters to the project.
> - **Study:**
>   - Materials needed to achieve the goal.
> - **Feedback System:**
>   - Reflection on the work I have done. Using an Example-Effect-Change/Continue (EEC) feedback model.

---

## Background:
So far:
- Work environment from scratch:
    - IDE (VSCODE), 
    - Programming Language & Libraries (Python), 
    - Containerization (Docker), 
    - Warehouse (Postgres), and 
    - Documentation System (Git)

- Choose the Data Architecture:
    - Medallion Model

- Initialized Pipeline Development:
    - Connected to Source Data API
    - Connected to Postgres Data Warehouse

Everything below will be new and used to reflect growth of project

---

> ## Start Date 17/11/2026
> - **Goal:** Pull 100 US artists from MusicBrainz API and store them in a Postgres Table.
>   - *Done when: "SELECT COUNT()" returns 100, and rerun returns the same count.*
> - **Reasoning:** Completing this goal establishes: successful limited data ingestion, tables in Postgres, and understanding of idempotency.
> - **Study Needed:**
>   - Skim MusicBrainz API doc again for pagination for limited search goal.
>   - Study up on psycopg2 library documentation.
>   - Study PostgreSQL documentation for JSON column types.
> - **Feedback System:**
> 
>End Date - Current