import requests
import pandas as pd


# pulling league name and manager data
# https://draft.premierleague.com/api/league/14352/details the api to pull the data

class GettingLeagueData:
    league_details_api = "https://draft.premierleague.com/api/league/14352/details"
    league_details_request = requests.get(league_details_api)
    league_details = league_details_request.json()