# Source Profile Interpretation

## customers.csv

The file has 250 rows but only 247 distinct `customer_id` values, and 2 rows are exact duplicates. This means `customer_id` cannot be trusted as a primary key without cleaning first. A pipeline that loads this straight into a table with a unique constraint would fail.

Every column came in as text, including `signup_date`. CSV files store no type information, so dates must be parsed manually. If parsing is skipped, date comparisons would sort alphabetically instead of chronologically.

There are also 3 missing emails and 2 missing cities, so any step that assumes those fields are always present would break.

## orders.json

The `shipping` column is not a simple value. It holds a nested object with `region` and `method` inside it. A relational database cannot store this directly, so the pipeline must flatten it into separate columns before loading.

`customer_id` has only 159 distinct values across 250 orders, which shows customers place more than one order. This is the link between orders and customers, and it means any join must expect many orders per customer.

Like the CSV, `order_timestamp` arrived as text and needs parsing before it can be used for time-based filtering.

## products.parquet

This file has no missing values and no duplicate rows, making it the cleanest of the three.

Data types were preserved correctly without any parsing, because Parquet stores the schema together with the data. This is a real advantage over CSV and JSON for pipeline reliability.

The file is also much smaller at 14.3 KB for 200 rows, compared to 76.1 KB for 250 JSON records, which matters when moving large volumes of data.