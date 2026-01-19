import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()

    # Parse timestamps
    df["admit_time"] = pd.to_datetime(df["admit_time"])
    df["discharge_time"] = pd.to_datetime(df["discharge_time"])

    # Feature: visit duration in hours
    df["visit_duration_hours"] = (df["discharge_time"] - df["admit_time"]).dt.total_seconds() / 3600

    # Basic cleaning rules
    df = df.drop_duplicates(subset=["visit_id"])
    df = df[df["cost"] >= 0]                   # no negative cost
    df = df[df["visit_duration_hours"] >= 0]   # remove invalid duration rows

    return df

if __name__ == "__main__":
    raw = pd.read_csv("data/raw/patient_visits.csv")
    cleaned = transform(raw)
    cleaned.to_csv("data/processed/visits_clean.csv", index=False)
    print(f"Saved {len(cleaned)} cleaned rows to data/processed/visits_clean.csv")
