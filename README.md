# DSS150P Laboratory 01 — Environment Setup and Source Profiling

**Name:** Chelzie Audrey Maranion
**Student Number:** 2024108712

## Purpose

This laboratory sets up a reproducible local data-engineering environment and performs a first-pass technical assessment of five source systems. The goal is to understand each source's structure, schema, and data-quality risks before any pipeline is built.

## Software Requirements

- Python 3.14
- Git
- Docker Desktop with Docker Compose
- Visual Studio Code
- Windows PowerShell

## Steps to Reproduce the Environment

    git clone <repository-url>
    cd DSS150P_Lab01_Maranion_ChelzieAudrey
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    docker compose up -d
    Get-Content sql\seed_support_tickets.sql | docker exec -i dss150p-postgres psql -U dss150p -d dss150p_lab
    Get-Content sql\01_create_schema.sql | docker exec -i dss150p-postgres psql -U dss150p -d dss150p_lab

## Starting and Stopping PostgreSQL

    docker compose up -d      # start the database
    docker ps                 # confirm it is running
    docker compose down       # stop the database

## Running the Python Scripts

Run all scripts from the repository root with the virtual environment active.

    python src\verify_environment.py    # tests the PostgreSQL connection
    python src\profile_sources.py       # profiles the CSV, JSON and Parquet files
    python src\inspect_api.py           # fetches and inspects the REST API

## Sources

| Source | Format | Rows | Notes |
|---|---|---|---|
| customers.csv | CSV | 250 | 3 missing emails, 2 missing cities, 2 duplicate rows, 247 distinct customer_id |
| orders.json | JSON | 250 | Contains a nested shipping object with region and method |
| products.parquet | Parquet | 200 | No nulls or duplicates, schema stored inside the file |
| JSONPlaceholder /posts | REST API | 100 | Public test API, returns a JSON list |
| support_tickets | PostgreSQL | 250 | assigned_agent and resolved_at allow NULL |

## Known Limitations and Unresolved Questions

- The lab guide lists psycopg2-binary in requirements.txt, but psycopg[binary] was used instead because psycopg2 has no prebuilt wheel for Python 3.14. The connection string therefore uses postgresql+psycopg:// rather than postgresql+psycopg2://.
- The guide refers to a PostgreSQL table named inventory_snapshot. The starter repository ships support_tickets instead, so that table was inspected.
- The REST API URL was taken from the starter README rather than the LMS, since the README supplies a public endpoint.
- It is not confirmed whether the 2 duplicated rows in customers.csv are errors or valid repeat registrations. This needs the source owner to clarify.
- The schema in sql/01_create_schema.sql was created but not bulk-loaded, per the laboratory instructions.