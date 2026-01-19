import pandas as pd

def extract(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Extracted {len(df)} rows from {path}")
    return df

if __name__ == "__main__":
    extract("data/raw/patient_visits.csv")
