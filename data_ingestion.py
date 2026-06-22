import pandas as pd
import os

folder = "data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

print(f"Found {len(files)} CSV files")

for file in files:
    path = os.path.join(folder, file)

    df = pd.read_csv(path)

    print("\n" + "="*50)
    print(f"FILE: {file}")
    print("="*50)

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())