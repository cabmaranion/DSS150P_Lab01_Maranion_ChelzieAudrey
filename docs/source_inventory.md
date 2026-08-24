# Source Inventory

## 1. customers.csv

- **Source name:** customers.csv
- **Source-system type:** Flat file given by the instructor
- **Data format:** CSV
- **Structure:** Structured
- **Expected update pattern:** One-time snapshot, does not change on its own
- **Likely acquisition method:** Read the file from data/raw using pandas
- **Schema location or owner:** No official schema. The header row is the only guide. Owner is the instructor.
- **Possible primary key:** customer_id
- **Schema-evolution risk:** Columns could be renamed, added, or reordered without warning since nothing enforces the format
- **Data-quality risk:** 3 missing emails, 2 missing cities, 2 duplicate rows, and only 247 distinct customer_id out of 250 rows

## 2. orders.json

- **Source name:** orders.json
- **Source-system type:** Flat file given by the instructor
- **Data format:** JSON
- **Structure:** Semi-structured
- **Expected update pattern:** One-time snapshot
- **Likely acquisition method:** Read the file from data/raw using pandas
- **Schema location or owner:** No official schema. Structure is implied by the file itself. Owner is the instructor.
- **Possible primary key:** order_id (250 distinct values in 250 rows)
- **Schema-evolution risk:** The nested shipping object could gain or lose fields, which would break code that expects certain keys
- **Data-quality risk:** No nulls or duplicates, but order_timestamp is stored as text and the nested shipping object must be flattened before loading into a table

## 3. products.parquet

- **Source name:** products.parquet
- **Source-system type:** Flat file given by the instructor
- **Data format:** Parquet
- **Structure:** Structured
- **Expected update pattern:** One-time snapshot
- **Likely acquisition method:** Read the file from data/raw using pandas with pyarrow
- **Schema location or owner:** The schema is stored inside the Parquet file itself
- **Possible primary key:** product_id (200 distinct values in 200 rows)
- **Schema-evolution risk:** Low, because the file carries its own schema and types are enforced
- **Data-quality risk:** Very low. No missing values and no duplicate rows.

## 4. REST API (JSONPlaceholder /posts)

- **Source name:** https://jsonplaceholder.typicode.com/posts
- **Source-system type:** Public REST API over the internet
- **Data format:** JSON
- **Structure:** Semi-structured
- **Expected update pattern:** Live. Data can change at any time and must be fetched again to stay current.
- **Likely acquisition method:** HTTP GET request using the requests library
- **Schema location or owner:** Documented on the JSONPlaceholder website. Owned by that service, not by us.
- **Possible primary key:** id
- **Schema-evolution risk:** High. The service can change fields or shut down and we have no control over it.
- **Data-quality risk:** The request can fail or time out. The data is fake sample data, not real business data.
- **Retrieved at (UTC):** 2026-08-24T15:32:47.371086+00:00

## 5. PostgreSQL table: support_tickets

- **Source name:** support_tickets
- **Source-system type:** Relational database running in Docker
- **Data format:** SQL table
- **Structure:** Structured
- **Expected update pattern:** Continuous. New tickets are added and existing ones updated as they are resolved.
- **Likely acquisition method:** SQL query through SQLAlchemy or psql
- **Schema location or owner:** Stored formally in information_schema. Owned by the database user dss150p.
- **Possible primary key:** ticket_id
- **Schema-evolution risk:** Low in the short term, because the database enforces column types and NOT NULL rules
- **Data-quality risk:** assigned_agent and resolved_at can be NULL. 4 tickets have no agent assigned, and open tickets have no resolution time yet.