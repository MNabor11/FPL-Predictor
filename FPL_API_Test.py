# this gives me the tool so that I can talk to the internet
import requests

# a variable FantasyURL that is set equal to the offical FPL api
FantasyUrl = "https://fantasy.premierleague.com/api/bootstrap-static/"

# a variable response that set equal gather all the raw data
response = requests.get(FantasyUrl)

# take the raw data and turns it into readable python data
data = response.json()

print(data.keys())

# trying to print out BRUNO
players = data["elements"]

for player in players:
    if player["web_name"] == "B.Fernandes":
        print(
            f"First Name: {player['first_name']} \nLast Name: {player['second_name']}")
        print(f"Form: {player['form']}")
        break


print("Hello FPL")
