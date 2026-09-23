import pandas as pd
import requests
import numpy as py

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

# connect managers and players

# read in the old seasons

# use numpy

# use scikit
