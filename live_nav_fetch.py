import requests
import pandas as pd
import os

# Mutual Fund Scheme Codes
schemes = {
    "125497": "fund_125497.csv",
    "119551": "fund_119551.csv",
    "120503": "fund_120503.csv",
    "118632": "fund_118632.csv",
    "119092": "fund_119092.csv",
    "120841": "fund_120841.csv"
}

# Create data/raw folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

for scheme_code, filename in schemes.items():
    try:
        url = f"https://api.mfapi.in/mf/{scheme_code}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "data" in data:
                df = pd.DataFrame(data["data"])

                file_path = os.path.join("data", "raw", filename)

                df.to_csv(file_path, index=False)

                print(f"✅ Saved {filename} | Rows: {len(df)}")

            else:
                print(f"⚠️ No NAV data found for scheme {scheme_code}")

        else:
            print(f"❌ Failed to fetch scheme {scheme_code}")

    except Exception as e:
        print(f"❌ Error fetching scheme {scheme_code}: {e}")

print("\n🎉 All scheme data fetched successfully!")