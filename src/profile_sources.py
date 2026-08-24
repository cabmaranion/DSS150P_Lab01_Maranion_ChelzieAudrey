from pathlib import Path
import pandas as pd

RAW = Path("data/raw")

sources = {
    "customers.csv": pd.read_csv(RAW / "customers.csv"),
    "orders.json": pd.read_json(RAW / "orders.json"),
    "products.parquet": pd.read_parquet(RAW / "products.parquet"),
}

for name, df in sources.items():
    size_kb = (RAW / name).stat().st_size / 1024
    print(f"\n=== {name} ===")
    print(f"file size: {size_kb:.1f} KB")
    print("rows:", df.shape[0], "columns:", df.shape[1])
    print("columns in order:", list(df.columns))
    print("\ndata types:")
    print(df.dtypes)
    print("\nmissing values per column:")
    print(df.isna().sum())
    hashable = df.copy()
    nested_cols = []
    for col in hashable.columns:
        if hashable[col].apply(lambda v: isinstance(v, (dict, list))).any():
            nested_cols.append(col)
            hashable[col] = hashable[col].astype(str)
    if nested_cols:
        print("\nnested columns (converted to text for counting):", nested_cols)
    print("\nfully duplicated rows:", hashable.duplicated().sum())
    print("\ndistinct values per column:")
    print(hashable.nunique())
    print("\nfirst five records:")
    print(df.head())

    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        print("\nnumeric min/max:")
        print(pd.DataFrame({"min": numeric.min(), "max": numeric.max()}))

    for col in df.columns:
        if "date" in col.lower() or "time" in col.lower() or "_at" in col.lower():
            parsed = pd.to_datetime(df[col], errors="coerce")
            if parsed.notna().any():
                print(f"\n{col}: earliest {parsed.min()}, latest {parsed.max()}")