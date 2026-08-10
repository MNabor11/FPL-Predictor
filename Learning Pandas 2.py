import requests
import pandas as pd

# THIS IS DATA FROM THE OFFICIAL FPL API


def fpl_Data():
    fpl_API_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
    fpl_API_Request = requests.get(fpl_API_URL)
    fpl_API_Data = fpl_API_Request.json()
    return fpl_API_Data


fpl_API_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
fpl_API_Request = requests.get(fpl_API_URL)
fpl_API_Data = fpl_API_Request.json()

print(fpl_API_Data.keys())
fpl_Phases = fpl_API_Data['phases']
fpl_Teams = fpl_API_Data['teams']
fpl_Total_Players = fpl_API_Data['element_stats']
fpl_Element_Types = fpl_API_Data['element_types']
fpl_elements = fpl_API_Data['elements']
# print(fpl_elements[0].keys())

# printing out the short team names
for shrtName in fpl_Teams:
    print(f'{shrtName['name']}'.upper())


# print(fpl_Teams[0])

# printing out teams id, name, strength at home and away
teams_Data_Table = pd.DataFrame(fpl_Teams)
print(teams_Data_Table[['id', 'name',
      'strength_overall_home', 'strength_overall_away']])

# printing out strength_overall_home and strength_overall_away
for overall_Strength in fpl_Teams:
    if overall_Strength['strength_overall_home'] & overall_Strength['strength_overall_away'] >= 3:
        print(
            f'{overall_Strength['name'].upper()}  Home: {overall_Strength['strength_overall_home']} Away: {overall_Strength['strength_overall_away']}')


class team:
    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name


class players:
    def __init__(self, known_name):
        self.known_name = known_name
