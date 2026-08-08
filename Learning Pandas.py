# this loads the libraries needed
import pandas as pd

import requests

# getting the data from the api
FantasyUrl = "https://fantasy.premierleague.com/api/bootstrap-static/"
fplRequest = requests.get(FantasyUrl)
fplData = fplRequest.json()

# printing out the keys so that i know what im looking for
print(fplData.keys())

# going to use 'teams'
teams_DF = pd.DataFrame(fplData['teams'])

# shows all the 'keys' in teams
# print(teams_DF.keys())

# im going to print out id and name of all the teams
print(teams_DF[['id', 'name']])

# printing out all the players
players = fplData['elements']
# print(players[0].keys())

for i, allPlayers in enumerate(players, start=1):
    if allPlayers.get('known_name'):
        print(f'{i} {allPlayers['known_name']}')
