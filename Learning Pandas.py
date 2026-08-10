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
print(teams_DF.keys())

# im going to print out id and name of all the teams
print(teams_DF[['id', 'name', 'short_name', 'team_division']])

# printing out all the players
players = fplData['elements']
# print(players[0].keys())

for i, allPlayers in enumerate(players, start=1):
    if allPlayers.get('known_name'):
        print(f'{i} {allPlayers['known_name']}')

# using the 25/26 season data
url_Players = (
    "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/cleaned_players.csv")
fpl_Season_26 = pd.read_csv(url_Players)

# this prints out the first 20 players in this cvs
print(fpl_Season_26.head(20))

# trying to print out the highest points from the 25/26 season - above 180 points
highest_FPL_Points = fpl_Season_26['total_points'] >= 160
print(
    fpl_Season_26[highest_FPL_Points][[
        'first_name', 'second_name', 'total_points', 'element_type']]
    .sort_values('total_points', ascending=False)
)
