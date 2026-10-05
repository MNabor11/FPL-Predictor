import requests
import pandas as pd


# pulling league name and manager data
# https://draft.premierleague.com/api/league/14352/details the api to pull the data


class GettingLeagueData:
    def __init__(self, league_id):
        self.league_id = league_id

    def get_league_data(self):
        url = f"https://draft.premierleague.com/api/league/{self.league_id}/details"
        response = requests.get(url)
        league_data = response.json()

        league_name = league_data['league']['name']
        managers = league_data['league_entries']

        manager_data = []
        for manager in managers:
            manager_info = {
                'ID': manager['entry_id'],
                'Name': manager['player_first_name'] + " " + manager['player_last_name'],
                'Team Name': manager['entry_name'],
                'Short Name': manager['short_name']
            }
            manager_data.append(manager_info)
        return league_name, pd.DataFrame(manager_data), self.league_id


# getting manager players and player id's
# https://draft.premierleague.com/api/league/14352/element-status


class elementData:
    def __init__(self, user_league_id):
        self.user_league_id = user_league_id

    def get_element_data(self):
        element_url = f"https://draft.premierleague.com/api/league/{self.user_league_id}/element-status"
        element_response = requests.get(element_url)
        element_data = element_response.json()
        element_status = element_data['element_status']
        player_element_list = []
        for getting_players in element_status:
            if getting_players['owner'] is not None:
                player_id_dict = {
                    "Owner": getting_players['owner'],
                    "Player ID": getting_players['element']
                }
                player_element_list.append(player_id_dict)
        return pd.DataFrame(player_element_list)


"""element_player_data = elementData(user_league_id)
player_element_df = element_player_data.get_element_data()
print(player_element_df)  # player data frame"""

# getting the players data
# connecting player id to players names and connecting them to managers
# https://fantasy.premierleague.com/api/bootstrap-static/ the official fpl api


class fplData:
    def __init__(self, user_league_id):
        self.user_league_id = user_league_id

    def get_fpl_data(self):
        fpl_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
        fpl_response = requests.get(fpl_url)
        fpl_data = fpl_response.json()
        players = fpl_data['elements']
        player_data_list = []
        for player in players:
            player_info = {
                "ID": player['id'],
                "Name": player['first_name']+" "+player['second_name'],
                "Total Points": player['total_points'],
                # add mapping? for player position?
                "Position": player['element_type'],
                'Minutes': player['minutes'],
                "Goals": player['goals_scored'],
                "Assists": player['assists'],
                'Clean Sheet': player['clean_sheets'],
                # can add way more
            }
            player_data_list.append(player_info)
        return pd.DataFrame(player_data_list)

    def get_fpl_teams(self):
        fpl_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
        fpl_response = requests.get(fpl_url)
        fpl_data = fpl_response.json()
        fpl_api_teams = fpl_data['teams']
        fpl_teams_list = []
        for team in fpl_api_teams:
            fpl_teams_dict = {
                "ID": team['id'],
                "Team Name": team['name'],
                "Home Str": team['strength_overall_home'],
                "Away Str": team['strength_overall_away'],
            }
            fpl_teams_list.append(fpl_teams_dict)
        return pd.DataFrame(fpl_teams_list)


"""fplData = fplData(user_league_id)
fpl_player_data_df = fplData.get_fpl_data()  # fpl player data frame
fpl_teams_data_df = fplData.get_fpl_teams()  # teams data frame
print(fpl_teams_data_df)"""

"""changing_player_postion = {1: "GKP",
                           2: "DEF",
                           3: "MID",
                           4: "FWD"}
fpl_player_data_df['Position'] = fpl_player_data_df['Position'].map(
    changing_player_postion)
print(fpl_player_data_df)"""

if __name__ == "__main__":
    some_league_id = int(input("Enter the league ID: "))
    league = GettingLeagueData(some_league_id)
    name, df, _ = league.get_league_data()
    print(df)
