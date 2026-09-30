import pandas as pd
import requests
import numpy as np

# pulling league name and manager data
# https://draft.premierleague.com/api/league/14352/details the api to pull the data

league_details_api = "https://draft.premierleague.com/api/league/14352/details"
league_details_request = requests.get(league_details_api)
league_details = league_details_request.json()

# print(league_details.keys()), prints out the key's needed to pull data
league_name = league_details['league']['name']  # pulls the leagues name
print(league_name)

# pulling the managers data and making it into a dataframe
league_entries = league_details['league_entries']
manager_list = []
for managers in league_entries:
    manager_dict = {
        "Name": managers['player_first_name']+" " + managers['player_last_name'],
        "ID": managers['entry_id'],
        "Team Name": managers['entry_name'],
        "Short Name": managers['short_name']
    }
    manager_list.append(manager_dict)
managers_df = pd.DataFrame(manager_list)
print(managers_df)


# getting manager players and player id's
# https://draft.premierleague.com/api/league/14352/element-status

player_element_id = "https://draft.premierleague.com/api/league/14352/element-status"
player_element_id_request = requests.get(player_element_id)
player_element_details = player_element_id_request.json()
# print(player_element_details.keys())
player_element_list = []
element_status = player_element_details['element_status']

# pulling the player and manager id's
for getting_players in element_status:
    if getting_players['owner'] is not None:
        player_id_dict = {
            "owner": getting_players['owner'],
            "player_id": getting_players['element']
        }
        player_element_list.append(player_id_dict)
player_element_df = pd.DataFrame(player_element_list)


# getting the players data
# connecting player id to players names and connecting them to managers
# https://fantasy.premierleague.com/api/bootstrap-static/ the official fpl api

fpl_api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
fpl_api_requests = requests.get(fpl_api_url)
fpl_api_details = fpl_api_requests.json()
#print(fpl_api_details.keys())
fpl_elements = fpl_api_details['elements']
managed_players_list = []
for player in fpl_elements:
    players_dict = {
        "ID": player['id'],
        "Name": player['first_name']+" "+player['second_name'],
        "Total Points": player['total_points'],
        # add mapping? for player position?
        "Position": player['element_type'],
        'Minutes': player['minutes'],
        "Goals": player['goals_scored'],
        "Assists": player['assists'],
        'Clean Sheet': player['clean_sheets'],
        # can add way more
    }
    managed_players_list.append(players_dict)

manage_player_df = pd.DataFrame(managed_players_list)

# getting prem team id's
fpl_api_teams = fpl_api_details['teams']
fpl_teams_list=[]
for team in fpl_api_teams:
    fpl_teams_dict = {
        "ID": team['id'],
        "Team Name": team['name'],
    }
    fpl_teams_list.append(fpl_teams_dict)
fpl_teams_df = pd.DataFrame(fpl_teams_list)


# connecting managers and players
fpl_manger_list = []
for manager in manager_list:
    for element in player_element_list:
        for player in managed_players_list:
            if manager['ID'] == element['owner'] and element['player_id'] == player['ID']:
                # print(
                # f"Name:  {manager['Name']} Player:  {player['Name']}  Team:  {manager['Team Name']}\n")
                fpl_m_dict = {
                    "Name": manager['Name'],
                    "Player": player['Name'],
                    "Team": manager['Team Name']
                }
                fpl_manger_list.append(fpl_m_dict)

fpl_m_df = pd.DataFrame(fpl_manger_list)
# print(fpl_m_df)


# read in the old seasons
# the total season totals
# url for the 25/26 season https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/players_raw.csv
season2526_cvs = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/players_raw.csv"
season2526 = pd.read_csv(season2526_cvs)

# pulling in data from the s 25/26 year

s2526_dict = {
    "assists": "Assists",
    "clean_sheets": "Clean Sheets",
    "clean_sheets_per_90": "Clean Sheets Per 90",
    "defensive_contribution": "Defensive Contribution",
    "defensive_contribution_per_90": "Defensive Contribution Per 90",
    "expected_assists": "Expected Assists",
    "expected_assists_per_90": "Expected Assists Per 90",
    "expected_goals": "Expected Goals",
    "expected_goals_per_90": "Expected Goals Per 90",
    "goals_scored": "Goals",
    "goals_conceded": "Goals Conceded",
    "goals_conceded_per_90": "Goal Conceded Per 90",
    "points_per_game": "Points Per Game",
    "total_points": "Total Points",
    "web_name": "Web Name",
    "element_type": "Position"
}


my_cols = [col for col in s2526_dict.keys() if col in season2526.columns]
s2526_df = season2526[my_cols].rename(columns=s2526_dict)

# print(s2526_df.head(10))
print(s2526_df.dtypes)

# print(s2526_df)
print(f" Manager df\n{managers_df.dtypes}")
print(f"fpl m \n{fpl_m_df.dtypes}")
print(f"{manage_player_df.dtypes}")
print(player_element_df.dtypes)

# url for the 25/24 season
# url https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/players_raw.csv
season2425_cvs = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/players_raw.csv"
season2425 = pd.read_csv(season2425_cvs)
s2425_dict = {
    "assists": "Assists",
    "clean_sheets": "Clean Sheets",
    "clean_sheets_per_90": "Clean Sheets Per 90",
    "expected_assists": "Expected Assists",
    "expected_assists_per_90": "Expected Assists Per 90",
    "expected_goals": "Expected Goals",
    "expected_goals_per_90": "Expected Goals Per 90",
    "goals_scored": "Goals",
    "goals_conceded": "Goals Conceded",
    "goals_conceded_per_90": "Goal Conceded Per 90",
    "points_per_game": "Points Per Game",
    "total_points": "Total Points",
    "web_name": "Web Name",
    "element_type": "Position"
}
s2425_col = [col for col in s2425_dict.keys() if col in season2425.columns]
s2425_df = season2425[s2425_col].rename(columns=s2425_dict)
print(s2425_df.dtypes)

# url for the 23/24 season
# https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/players_raw.csv
season2324_cvs = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/players_raw.csv"
season2324 = pd.read_csv(season2324_cvs)
s2324_dict = {
    "assists": "Assists",
    "clean_sheets": "Clean Sheets",
    "clean_sheets_per_90": "Clean Sheets Per 90",
    "expected_assists": "Expected Assists",
    "expected_assists_per_90": "Expected Assists Per 90",
    "expected_goals": "Expected Goals",
    "expected_goals_per_90": "Expected Goals Per 90",
    "goals_scored": "Goals",
    "goals_conceded": "Goals Conceded",
    "goals_conceded_per_90": "Goal Conceded Per 90",
    "points_per_game": "Points Per Game",
    "total_points": "Total Points",
    "web_name": "Web Name",
    "element_type": "Position"
}
s2324_col = [col for col in s2324_dict.keys() if col in season2324.columns]
s2324_df = season2324[s2324_col].rename(columns=s2324_dict)
print(s2324_df.dtypes)

# those were total data from the whole of those seasons


# gw 1 -38 seasons
# attempting to get gameweek 1 - 38 (GW) Season 25/26
# url for GW 1-38 https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/gws/merged_gw.csv
s2526_gw_url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/gws/merged_gw.csv"
s2526_gw_csv = pd.read_csv(s2526_gw_url)
print(s2526_gw_csv.keys())
s2526_dict_gw ={
"assists": "Assists",
    "clean_sheets": "Clean Sheets",
    "clean_sheets_per_90": "Clean Sheets Per 90",
    "defensive_contribution": "Defensive Contribution",
    "defensive_contribution_per_90": "Defensive Contribution Per 90",
    "expected_assists": "Expected Assists",
    "expected_assists_per_90": "Expected Assists Per 90",
    "expected_goals": "Expected Goals",
    "expected_goals_per_90": "Expected Goals Per 90",
    "goals_scored": "Goals",
    "goals_conceded": "Goals Conceded",
    "goals_conceded_per_90": "Goal Conceded Per 90",
    "points_per_game": "Points Per Game",
    "total_points": "Total Points",
    "name".lower(): "Name",
    "element_type": "Position",
    "GW": "Game Week",
    "was_home": "Was Home",
    'opponent_team': "Opponent Team",
    "element": "Player ID"
}

s2526_gw = [col for col in s2526_dict_gw.keys() if col in s2526_gw_csv.columns]
s2526_df_gw = s2526_gw_csv[s2526_gw].rename(columns=s2526_dict_gw)

print(s2526_df_gw.dtypes)



my_name = input("Enter a name: ")
ben = s2526_df_gw[
    s2526_df_gw["Name"] == my_name
]
with pd.option_context(
    "display.max_rows", None,
    "display.max_columns", None,
    "display.width", None
):
    print(ben)

print(f"BRUNO\n{ben[[
    "Game Week",
    "Opponent Team",
    "Was Home",
    "Goals",
    "Assists",
    "Expected Goals",
    "Expected Assists",
    "Total Points"
]]}")

# gw for 24/25
# url https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/gws/merged_gw.csv
s2425_url_gw = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/gws/merged_gw.csv"
s2425_gw_csv = pd.read_csv(s2425_url_gw)
s2425_dict_gw ={
    "assists": "Assists",
    "clean_sheets": "Clean Sheets",
    "clean_sheets_per_90": "Clean Sheets Per 90",
    "expected_assists": "Expected Assists",
    "expected_assists_per_90": "Expected Assists Per 90",
    "expected_goals": "Expected Goals",
    "expected_goals_per_90": "Expected Goals Per 90",
    "goals_scored": "Goals",
    "goals_conceded": "Goals Conceded",
    "goals_conceded_per_90": "Goal Conceded Per 90",
    "points_per_game": "Points Per Game",
    "total_points": "Total Points",
    "name".lower(): "Name",
    "element_type": "Position",
    "GW": "Game Week",
    "was_home": "Was Home",
    'opponent_team': "Opponent Team",
    "element": "Player ID"
}

s2425_gw = [col for col in s2425_dict_gw.keys() if col in s2425_gw_csv.columns]
s2425_gw_df = s2425_gw_csv[s2425_gw].rename(columns=s2425_dict_gw)

# gw for 23/24
# url https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/gws/merged_gw.csv
s2324_url_gw = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/gws/merged_gw.csv"
s2324_gw_csv = pd.read_csv(s2324_url_gw)
s2324_dict_gw ={
    "assists": "Assists",
    "clean_sheets": "Clean Sheets",
    "clean_sheets_per_90": "Clean Sheets Per 90",
    "expected_assists": "Expected Assists",
    "expected_assists_per_90": "Expected Assists Per 90",
    "expected_goals": "Expected Goals",
    "expected_goals_per_90": "Expected Goals Per 90",
    "goals_scored": "Goals",
    "goals_conceded": "Goals Conceded",
    "goals_conceded_per_90": "Goal Conceded Per 90",
    "points_per_game": "Points Per Game",
    "total_points": "Total Points",
    "name".lower(): "Name",
    "element_type": "Position",
    "GW": "Game Week",
    "was_home": "Was Home",
    'opponent_team': "Opponent Team",
    "element": "Player ID"
}
s2324_gw = [col for col in s2425_dict_gw.keys() if col in s2425_gw_csv.columns]
s2324_gw_df = s2324_gw_csv[s2324_gw].rename(columns=s2324_dict_gw)



# use flask
# use numpy

# use scikit
