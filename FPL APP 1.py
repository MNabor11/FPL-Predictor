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
