# this gives me the tool so that I can talk to the internet
import requests

import random

# a variable FantasyURL that is set equal to the offical FPL api
FantasyUrl = "https://fantasy.premierleague.com/api/bootstrap-static/"

# a variable response that set equal gather all the raw data
response = requests.get(FantasyUrl)

# take the raw data and turns it into readable python data
data = response.json()

print(data.keys())

# trying to print out BRUNO
players = data["elements"]

print("\n---------------------------------------")
for player in players:
    if player["web_name"] == "B.Fernandes":
        print(
            f"First Name: {player['first_name']} \nLast Name: {player['second_name']}")
        print(f"Form: {player['form']}")
        break
print("\n---------------------------------------")

# trying to print out Manchester United
United = data['teams']
for team in United:
    if team["name"] == "Man Utd":
        print(
            "--------------------\nThe BEST club in the Premier League is MANCHESTER UNITED\n--------------------")

print("\n---------------------------------------")
# reads out all the keys so that i know what to use
print(United[0].keys())
print("\n---------------------------------------")

teams = []
print("\n---------------------------------------")
for i, allTeams in enumerate(United, start=1):
    print(f"Team {i} : {allTeams['name']}")
    teams.append(allTeams['name'])
print("\n---------------------------------------")
# this will print the list teams
# print(teams)

print("\n---------------------------------------")
randomTeam = random.randint(1, 20)
print(f"Man Utd will play {teams[randomTeam]} this Sunday @ 12:30pm")
print("\n---------------------------------------")

# prints out all the keys of elements
print(players[0].keys())
# key is 'known_name'
print("\n---------------------------------------")
for player in players:
    if player.get('known_name'):
        print(f"Player - {player['known_name']}")
print("\n---------------------------------------")

# attempting to print out the Man Utd roster and the 'squad_number'
Man_U_ID = None

for id in United:
    if id['name'] == 'Man Utd':
        Man_U_ID = id['id']
        print(Man_U_ID)
i = 1
print("The roster for MANCHESTER UNITED")
for player in players:
    if player['team'] == Man_U_ID:
        if player.get('known_name'):
            print(
                f' \n {i} Player name: {player['known_name']} Number {player['squad_number']}')
            i += 1

# printing out the keys of 'total_players'

total_Player = data['total_players']
print(total_Player)
print("Hello FPL")
