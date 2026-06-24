import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        print(f"\n{'='*50}")
        print(file)

        df = pd.read_csv(os.path.join(folder, file))

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nShape:")
        print(df.shape)

        print("\nFirst 5 rows:")
        print(df.head())