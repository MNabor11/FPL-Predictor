import requests


def fpl():
    api_Url = ("https://fantasy.premierleague.com/api/bootstrap-static/")
    url_Request = requests.get(api_Url)
    api_Data = url_Request.json()
    return api_Data
