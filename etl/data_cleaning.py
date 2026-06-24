import pandas as pd
import os

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

for file in os.listdir(RAW_FOLDER):

    if file.endswith(".csv"):

        filepath = os.path.join(RAW_FOLDER, file)

        df = pd.read_csv(filepath)

        # Convert date
        df["date"] = pd.to_datetime(
            df["date"],
            format="%d-%m-%Y"
        )

        # Sort by date
        df = df.sort_values("date")

        # Remove duplicates
        df = df.drop_duplicates()

        # Remove invalid NAV
        df = df[df["nav"] > 0]

        # Forward fill missing values
        df["nav"] = df["nav"].ffill()

        output_path = os.path.join(
            PROCESSED_FOLDER,
            file
        )

        df.to_csv(output_path, index=False)

        print(f"Cleaned: {file}")