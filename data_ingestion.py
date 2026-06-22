import pandas as pd
import os

folder = "data/raw"

# Get all CSV files
files = [file for file in os.listdir(folder) if file.endswith(".csv")]

print(f"\nFound {len(files)} CSV files\n")

for file in files:
    try:
        file_path = os.path.join(folder, file)

        df = pd.read_csv(file_path)

        print("=" * 60)
        print(f"FILE: {file}")
        print("=" * 60)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\n")

    except Exception as e:
        print(f"Error reading {file}: {e}")