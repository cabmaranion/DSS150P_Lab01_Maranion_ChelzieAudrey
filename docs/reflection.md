# Reflection

## 1. Easiest source to integrate

For me the easiest source to integrate is the products.parquet. When I ran profile_sources.py, it came back with zero missing values, zero duplicate rows, and the correct data types straight away. unit_price showed as float64 and stock_quantity as int32 without me having to parse anything. This happens because Parquet stores the schema inside the file. The CSV, by contrast, gave every column back as str, including signup_date.

## 2. Greatest schema or data-quality risk

I suppose it is the customers.csv. The profiling output showed 250 rows but only 247 distinct customer_id values, plus 2 fully duplicated rows, 3 missing emails, and 2 missing cities. A CSV also has no enforced schema, so a renamed column in the header would break things silently. orders.json has its own risk in the nested shipping object, which actually crashed df.duplicated() when I first ran my script.

## 3. Risk of building before understanding the source

What I don't like is that it would fail, or worse, succeed with wrong data. That will probably happen when we build before understanding the source. For example, declaring customer_id as a primary key without deduplicating first would reject the file outright. Another is that treating signup_date as text would sort dates alphabetically. And assuming that shipping is a flat value would break the moment the pipeline hits a dictionary.

## 4. How the tools improve reproducibility

Git kept a record of every step I took. With nine commits I can look back at any point and see exactly what changed, which means nothing is lost if I break something later. The virtual environment kept pandas and the other packages inside .venv instead of the system Python. I saw this work when VS Code ran my script with the wrong interpreter and it failed with ModuleNotFoundError, which proved the separation is real. Docker made the database easy to recover. My container kept running even after I accidentally closed the terminal, and the support tickets were still there when I came back. But Docker also showed the other side of this. It would not start for over an hour because WSL was missing from my machine, and nothing downstream could run until that was fixed. Documentation matters for the same reason. I wrote down why I used psycopg instead of psycopg2, and I would not remember that in three weeks.