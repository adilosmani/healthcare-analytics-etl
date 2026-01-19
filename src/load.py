import sqlite3
import pandas as pd

def load_to_sqlite(csv_path: str, db_path: str = "healthcare.db") -> None:
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql("visits", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded {len(df)} rows into {db_path} (table: visits)")

if __name__ == "__main__":
    load_to_sqlite("data/processed/visits_clean.csv")
