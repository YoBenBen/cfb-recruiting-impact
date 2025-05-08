import pandas as pd

# Load recruiting + team stats data
recruiting = pd.read_csv("data/recruiting_data.csv")
team_stats = pd.read_csv("data/team_summary.csv")

# Shift recruiting year to match when players take effect
recruiting["impact_year"] = recruiting["year"] + 2

# Merge datasets on team + impact year
merged = pd.merge(
    team_stats,
    recruiting,
    left_on=["team", "year"],
    right_on=["team", "impact_year"],
    how="inner"
)

# Optional: print all columns once for debugging
# print("Columns in merged:", merged.columns.tolist())

# Keep only the columns you want and rename 'year_x' → 'year'
merged = merged[[
    "team", "year_x", "win", "games_played", "win_pct",
    "points_scored", "points_allowed", "point_diff",
    "rank", "points"
]].rename(columns={"year_x": "year"})

# Save final cleaned data
merged.to_csv("data/final_merged.csv", index=False)
print(f"✅ Merged dataset saved to data/final_merged.csv with {len(merged)} rows.")

