import requests
import pandas as pd

# current fpl data
official_FPL_API = "https://fantasy.premierleague.com/api/bootstrap-static/"
official_API_Data = requests.get(official_FPL_API).json()

# print(official_API_Data.keys())
# ['chips', 'events', 'game_settings', 'game_config', 'phases', 'teams', 'total_players', 'element_stats', 'element_types', 'elements']
official_Teams = official_API_Data['teams']
official_Players = official_API_Data['elements']

odf_Teams = pd.DataFrame(official_Teams)
odf_Players = pd.DataFrame(official_Players)

print(odf_Players['known_name'])
print('\n')
print(odf_Teams[['id', 'name', 'short_name']])

# season 25/26
season_25_26_URL = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/cleaned_players.csv"
fpl_25_26_Data = pd.read_csv(season_25_26_URL)
print(fpl_25_26_Data[['first_name', 'second_name',
      'goals_scored', 'assists', 'total_points', 'minutes', 'clean_sheets', 'element_type']].head(20))
highest_FPL_points_26 = fpl_25_26_Data['total_points'] >= 150
print('\n')
print(fpl_25_26_Data[highest_FPL_points_26][['first_name', 'second_name',
      'goals_scored', 'assists', 'total_points', 'minutes', 'clean_sheets', 'element_type']].sort_values('total_points', ascending=False))
