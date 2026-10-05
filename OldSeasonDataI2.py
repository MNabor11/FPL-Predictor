import pandas as pd

# url for the 25/26 season
# url 25/26 season https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/players_raw.csv


class S2526Total():
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/players_raw.csv"

    def get_s2526_data(self):
        season2526 = pd.read_csv(self.url)
        pos_map = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
        season2526["element_type"] = season2526["element_type"].map(pos_map)
        s2526_dict = {
            "assists": "Assists",
            "clean_sheets": "Clean Sheets",
            "clean_sheets_per_90": "Clean Sheets Per 90",
            "defensive_contribution": "Defensive Contribution",
            "defensive_contribution_per_90": "Defensive Contribution Per 90",
            "expected_assists": "Expected Assists",
            "expected_assists_per_90": "Expected Assists Per 90",
            "expected_goals": "Expected Goals",
            "expected_goals_per_90": "Expected Goals Per 90",
            "goals_scored": "Goals",
            "goals_conceded": "Goals Conceded",
            "goals_conceded_per_90": "Goal Conceded Per 90",
            "points_per_game": "Points Per Game",
            "total_points": "Total Points",
            "web_name": "Web Name",
            "element_type": "Pos"}
        s2526_col = [col for col in s2526_dict.keys()
                     if col in season2526.columns]
        s2526_total_df = season2526[s2526_col].rename(columns=s2526_dict)
        return s2526_total_df


s2526_season_total = S2526Total()
s2526_total_df = s2526_season_total.get_s2526_data()  # total season data for 25/26
print(s2526_total_df.sort_values(by="Total Points", ascending=False))


# url for the 25/24 season
# url https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/players_raw.csv


class S2425Total():
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/players_raw.csv"

    def get_s2425_data(self):
        season2425 = pd.read_csv(self.url)
        pos_map = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
        season2425["element_type"] = season2425["element_type"].map(pos_map)
        s2425_dict = {
            "assists": "Assists",
            "clean_sheets": "Clean Sheets",
            "clean_sheets_per_90": "Clean Sheets Per 90",
            "expected_assists": "Expected Assists",
            "expected_assists_per_90": "Expected Assists Per 90",
            "expected_goals": "Expected Goals",
            "expected_goals_per_90": "Expected Goals Per 90",
            "goals_scored": "Goals",
            "goals_conceded": "Goals Conceded",
            "goals_conceded_per_90": "Goal Conceded Per 90",
            "points_per_game": "Points Per Game",
            "total_points": "Total Points",
            "web_name": "Web Name",
            "element_type": "Pos"}
        s2425_col = [col for col in s2425_dict.keys()
                     if col in season2425.columns]
        s2425_total_df = season2425[s2425_col].rename(columns=s2425_dict)
        return s2425_total_df


s2425_season_total = S2425Total()
s2425_total_df = s2425_season_total.get_s2425_data()  # total season data for 24/25
print(s2425_total_df.sort_values(by="Total Points", ascending=False))


# url for the 23/24 season
# https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/players_raw.csv

class S2324Total():
    def __init__(self):
        self.url = " https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/players_raw.csv"

    def get_s2324_data(self):
        season2324 = pd.read_csv(self.url)
        pos_map = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
        season2324["element_type"] = season2324["element_type"].map(pos_map)
        s2324_dict = {
            "assists": "Assists",
            "clean_sheets": "Clean Sheets",
            "clean_sheets_per_90": "Clean Sheets Per 90",
            "expected_assists": "Expected Assists",
            "expected_assists_per_90": "Expected Assists Per 90",
            "expected_goals": "Expected Goals",
            "expected_goals_per_90": "Expected Goals Per 90",
            "goals_scored": "Goals",
            "goals_conceded": "Goals Conceded",
            "goals_conceded_per_90": "Goal Conceded Per 90",
            "points_per_game": "Points Per Game",
            "total_points": "Total Points",
            "web_name": "Web Name",
            "element_type": "Pos"}
        s2324_col = [col for col in s2324_dict.keys()
                     if col in season2324.columns]
        s2324_total_df = season2324[s2324_col].rename(columns=s2324_dict)
        return s2324_total_df


s2324_season_total = S2324Total()
s2324_total_df = s2324_season_total.get_s2324_data()  # total season data for 23/24
print(s2324_total_df.sort_values(by="Total Points", ascending=False))
