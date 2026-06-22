import requests
import pandas as pd
import os

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    os.makedirs("data/raw", exist_ok=True)

    nav_df.to_csv(
        "data/raw/sbi_bluechip_nav.csv",
        index=False
    )

    print("NAV data saved successfully!")
    print(nav_df.head())

else:
    print("Failed to fetch data")