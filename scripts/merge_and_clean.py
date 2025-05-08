import pandas as pd

recruit = pd.read_csv("data/recruiting_data.csv")
stats = pd.read_csv("data/team_stats.csv")

# Lag recruiting class by 2 years
recruit['impact_year'] = recruit['year'] + 2

# Merge on team name and year
merged = stats.merge(recruit, left_on=['team', 'year'], right_on=['team', 'impact_year'])

# Create win % and point differential
merged['win_pct'] = merged['wins'] / (merged['wins'] + merged['losses'])
merged['point_diff'] = merged['pointsScored'] - merged['pointsAllowed']

# Save merged data
merged.to_csv("data/merged_data.csv", index=False)
print("Merged data saved.")