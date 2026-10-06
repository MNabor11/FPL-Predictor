import pandas as pd
import requests
from FPLLeagueDataI2 import GettingLeagueData, elementData, fplData
from OldSeasonDataI2 import S2526Total, S2425Total, S2324Total
from OldWeeklyDataI2 import S2526Weekly, S2425Weekly, S2324Weekly

getting_seasonT = True


def main():

    user_league_id = int(input("Enter the league ID: "))

    # pulling league name and manager data
    league = GettingLeagueData(user_league_id)
    league_name, manager_data_df, league_id = league.get_league_data()
    print(f"League Name: {league_name} ID: {league_id}")
    print(manager_data_df)  # manager data frame

    # getting manager players and player id's
    element_player_data = elementData(user_league_id)
    player_element_df = element_player_data.get_element_data()
    print(player_element_df)

    # getting the players data
    fpl_Data = fplData(user_league_id)
    fpl_player_data_df = fpl_Data.get_fpl_data()  # fpl player data frame
    fpl_teams_data_df = fpl_Data.get_fpl_teams()  # teams data frame
    print(fpl_teams_data_df)

    changing_player_postion = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
    fpl_player_data_df['Position'] = fpl_player_data_df['Position'].map(
        changing_player_postion)
    print(fpl_player_data_df)

    # old total season data s23 - s2526
    get_old_season_data = input(
        "Do you want to get old season data? (y/n): ").lower()
    if get_old_season_data == "y":
        # total season data for 25/26
        s2526_season_total = S2526Total()
        s2526_total_df = s2526_season_total.get_s2526_data()
        print(s2526_total_df.sort_values(by="Total Points", ascending=False))

        # total season data for 24/25
        s2425_season_total = S2425Total()
        s2425_total_df = s2425_season_total.get_s2425_data()  # total season data for 24/25
        print(s2425_total_df.sort_values(by="Total Points", ascending=False))

        # total season data for 23/24
        s2324_season_total = S2324Total()
        s2324_total_df = s2324_season_total.get_s2324_data()  # total season data for 23/24
        print(s2324_total_df.sort_values(by="Total Points", ascending=False))

    elif get_old_season_data == "n":
        print("Skipping old season data.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
