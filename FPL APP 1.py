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
# print(fpl_api_details.keys())
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

manage_player_dr = pd.DataFrame(managed_players_list)

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

fpl_m_df = pd.DataFrame(fpl_manger_list).head(-20)
print(fpl_m_df)


# read in the old seasons

# url for the 25/26 season https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/players_raw.csv
season2526_cvs = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/players_raw.csv"
season2526 = pd.read_csv(season2526_cvs)
for s2526 in season2526.keys():
    pass
    # print(s2526)
# url for the 25/24 season
# url https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/players_raw.csv
season2425_cvs = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/players_raw.csv"
season2425 = pd.read_csv(season2425_cvs)
for s2425 in season2425.keys():
    pass
    # print(s2425)

# url for the 23/24 season
# https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/players_raw.csv
season2324_cvs = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/players_raw.csv"
season2324 = pd.read_csv(season2324_cvs)
for s2324 in season2324.keys():
    pass
    # print(s2324)
# use numpy

# use scikit
