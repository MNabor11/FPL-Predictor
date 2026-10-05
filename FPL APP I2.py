import pandas as pd
import requests
from FPLLeagueDataI2 import GettingLeagueData, elementData, fplData


def main():

    user_league_id = int(input("Enter the league ID: "))
    league = GettingLeagueData(user_league_id)
    league_name, manager_data_df, league_id = league.get_league_data()
    print(f"League Name: {league_name} ID: {user_league_id}")
    print(manager_data_df)  # manager data frame

    element_player_data = elementData(user_league_id)
    player_element_df = element_player_data.get_element_data()
    print(player_element_df)

    fplData = fplData(user_league_id)
    fplData = fplData(user_league_id)
    fpl_player_data_df = fplData.get_fpl_data()  # fpl player data frame
    fpl_teams_data_df = fplData.get_fpl_teams()  # teams data frame
    print(fpl_teams_data_df)

    changing_player_postion = {1: "GKP",
                               2: "DEF",
                               3: "MID",
                               4: "FWD"}
    fpl_player_data_df['Position'] = fpl_player_data_df['Position'].map(
        changing_player_postion)
    print(fpl_player_data_df)


if __name__ == "__main__":
    main()
