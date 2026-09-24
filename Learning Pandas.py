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

# im going to print out the id and names of all the teams
print(teams_DF[['id', 'name', 'short_name', 'team_division']])

# printing out all the players
players = fplData['elements']
# print(players[0].keys())

for i, allPlayers in enumerate(players, start=1):
    if allPlayers.get('known_name'):
        print(f'{i} {allPlayers['known_name']}')


# below this is day 2

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

# testing the same thing with a different url
url_V2_Players = (
    "https://github.com/vaastav/Fantasy-Premier-League/blob/master/data/2025-26/cleaned_players.csv")
# fpl_Request = requests.get(url_V2_Players)
# v2_Players_Data = fpl_Request.json()
# print(v2_Players_Data.keys())

# v2_Players = v2_Players_Data['elements']
# print(v2_Players[0])

# this url does not work because it's github page not an api like the official FPL fantasty page, so you read it in a cvs

# Define data and columns
data = [[0.3, 2], [0.5, 4], [0.1, 1]]
columns = ["goals_per_90", "goals"]

df = pd.DataFrame(data, columns=columns)
print(df)
# Output:
#    goals_per_90  goals
# 0           0.3      2
# 1           0.5      4
# 2           0.1      1
