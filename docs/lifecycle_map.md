# Data Engineering Lifecycle Map

| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
|---|---|---|---|---|
| Source system | Data that comes from somewhere else. We get it, we did not make it. | customers.csv, orders.json, products.parquet, and the REST API given by our instructor | The three raw files and the API endpoint | The API could stop working, or a file could come with different columns than our code expects |
| Ingestion/acquisition | Reading the data into our program so we can work with it | Loading the CSV and JSON files, reading the Parquet file, and calling the API to get data | pandas for CSV and JSON, pyarrow for Parquet, requests for the API | Wrong file path so the file is not found, or the internet drops while calling the API |
| Storage | Where the data is kept so we can use it again later | The PostgreSQL database running in Docker, and the data/raw folder that holds the original files | Docker container dss150p-postgres, and the data/raw folder | The container stops running, or the volume is deleted and the data is gone |
| Processing/transformation | Changing raw data into a cleaner form that is easier to use | Joining customers with their orders, fixing date formats, renaming columns to match | pandas and SQL queries | A bad join makes duplicate rows, or changing a data type quietly ruins the values |
| Data quality/validation | Checking if the data is correct before we trust it | Counting missing values, checking data types, and looking for duplicate IDs in each source | profile_sources.py and SQL checks | Nobody checks the data, so wrong values reach a report and someone makes a bad decision |
| Delivery | Giving the finished data to whoever needs it | The tables we create in PostgreSQL that someone can query | SQL tables from 01_create_schema.sql | The data arrives too late to be useful, or in a format the user cannot open |
| Consumer | The person or app that actually uses the data at the end | An analyst running SQL queries, or a dashboard showing sales per customer | SQL client or reporting tool | They misunderstand what a column means because it was never documented |

## Diagram

```
customers.csv ────┐
orders.json ──────┤
products.parquet ─┤──> [ Pipeline / Process ] ──> [ PostgreSQL Storage ] ──> [ Analyst / Dashboard ]
REST API ─────────┘      (read, clean, load)         (dss150p_lab)              (consumer)
```