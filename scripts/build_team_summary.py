import pandas as pd

# Load game-level data
df = pd.read_csv("data/team_games.csv")

# Create two datasets: one for home teams, one for away teams
home = df[['year', 'home_team', 'home_points', 'away_points']].copy()
home.columns = ['year', 'team', 'points_scored', 'points_allowed']
home['win'] = (home['points_scored'] > home['points_allowed']).astype(int)

away = df[['year', 'away_team', 'away_points', 'home_points']].copy()
away.columns = ['year', 'team', 'points_scored', 'points_allowed']
away['win'] = (away['points_scored'] > away['points_allowed']).astype(int)

# Combine both into one full dataset
full = pd.concat([home, away])

# Group by team/year
summary = full.groupby(['team', 'year']).agg({
    'win': 'sum',
    'points_scored': 'sum',
    'points_allowed': 'sum',
    'team': 'count'  # total games played
}).rename(columns={'team': 'games_played'}).reset_index()

# Calculate win percentage and point diff
summary['win_pct'] = summary['win'] / summary['games_played']
summary['point_diff'] = summary['points_scored'] - summary['points_allowed']

# Save result
summary.to_csv("data/team_summary.csv", index=False)
print("✅ Saved team-level stats to data/team_summary.csv")
