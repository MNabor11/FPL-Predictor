

from API import fpl
from Teams import team
from Players import players_Name
# data from the official api
fpl_data = fpl()
fpl_Teams = fpl_data['teams']
fpl_Players = fpl_data['elements']
print(fpl_data.keys())
print(fpl_Teams[0])

teams_List = []
for teams_Info in fpl_Teams:
    team_Name = team(name=teams_Info['name'],
                     short_name=teams_Info['short_name'])
    teams_List.append(team_Name)
print("\n")
for t in teams_List:
    print(f'{t.name} - {t.short_name}')
print("\n")
for club_Names in fpl_Teams:
    print(
        f'{club_Names['id']} {club_Names['name']} - {club_Names['short_name']}'.upper())
print("\n")
players_List = []
for players_Info in fpl_Players:
    player_Name = players_Name(name=players_Info['known_name'])
    players_List.append(player_Name)

# printing out the players
print("\n")
i = 0
for i, p_players in enumerate(players_List, start=1):
    if p_players.known_name:
        print(f'{i} {p_players.known_name}')

variants = {
    'name': ['loki', 'mobius', 'time keepers'],
    'age': [33, 54, 0],
    'role': ['variant', 'worker', 'boss']
}
print(variants.keys())
