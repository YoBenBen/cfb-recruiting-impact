import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Load API key
load_dotenv()
API_KEY = os.getenv("CFBD_API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}

years = range(2015, 2024)
all_games = []

for year in years:
    url = f"https://api.collegefootballdata.com/games?year={year}&seasonType=both&division=fbs"
    response = requests.get(url, headers=headers)
    print(f"Year {year} status code: {response.status_code}")

    if response.status_code == 200:
        games = response.json()
        print(f"  -> Fetched {len(games)} games for {year}")

        if year == 2015 and len(games) > 0:
            print("🔍 Sample game:", games[0])

        for game in games:
            if game.get("homePoints") is not None and game.get("awayPoints") is not None:
                all_games.append({
                    "year": year,
                    "home_team": game["homeTeam"],
                    "home_points": game["homePoints"],
                    "away_team": game["awayTeam"],
                    "away_points": game["awayPoints"]
                })

# Save to CSV
if len(all_games) == 0:
    print("⚠️ No valid games found. Not saving file.")
else:
    df = pd.DataFrame(all_games)
    df.to_csv("data/team_games.csv", index=False)
    print(f"✅ Saved {len(df)} games to team_games.csv")



