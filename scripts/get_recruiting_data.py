import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()
API_KEY = os.getenv("CFBD_API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}

years = range(2012, 2024)  # go back further to ensure we can match lag years
all_data = []

for year in years:
    url = f"https://api.collegefootballdata.com/recruiting/teams?year={year}"
    response = requests.get(url, headers=headers)
    print(f"Year {year} status: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for row in data:
            row['year'] = year
        all_data.extend(data)
    else:
        print(f"⚠️ Failed for year {year}")

# Save to CSV if anything was downloaded
if all_data:
    df = pd.DataFrame(all_data)
    df.to_csv("data/recruiting_data.csv", index=False)
    print(f"✅ Saved {len(df)} recruiting rows to recruiting_data.csv")
else:
    print("❌ No recruiting data fetched. Check your API key or endpoint.")
