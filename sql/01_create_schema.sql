-- DSS150P Lab 01 - Schema for customers.csv
-- Types and constraints are based on profiling results in docs/source_profile.md

CREATE SCHEMA IF NOT EXISTS lab;

CREATE TABLE IF NOT EXISTS lab.customers (
    customer_id      VARCHAR(10) PRIMARY KEY,
    first_name       TEXT NOT NULL,
    last_name        TEXT NOT NULL,
    email            TEXT,
    city             TEXT,
    signup_date      DATE NOT NULL,
    customer_segment TEXT NOT NULL,
    CONSTRAINT ck_customer_id_format CHECK (customer_id LIKE 'C%'),
    CONSTRAINT ck_signup_date_not_future CHECK (signup_date <= CURRENT_DATE)
);

-- Notes on design decisions:
-- customer_id is VARCHAR because values look like 'C0001', not integers.
-- customer_id is declared PRIMARY KEY, but the raw file has only 247 distinct
-- values across 250 rows and 2 fully duplicated rows. A future pipeline must
-- deduplicate before loading or this constraint will reject the data.
-- email and city allow NULL because profiling found 3 and 2 missing values.
-- first_name, last_name, signup_date and customer_segment had zero nulls,
-- so NOT NULL is justified by evidence.