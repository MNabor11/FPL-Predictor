import pandas as pd

# getting gw 1 -38 from previous seasons

# url for GW 1-38 https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/gws/merged_gw.csv


class S2526Weekly():
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2025-26/gws/merged_gw.csv"

    def get_s2526_weekly_data(self):
        season2526_weekly = pd.read_csv(self.url)
        pos_map = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
        if "element_type" in season2526_weekly.columns:
            season2526_weekly["element_type"] = season2526_weekly["element_type"].map(
                pos_map)
        s2526_dict_gw = {
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
            "name".lower(): "Name",
            "element_type": "Pos",
            "GW": "Game Week",
            "was_home": "Was Home",
            'opponent_team': "O Team",
            "element": "Player ID"
        }
        s2526_gw = [col for col in s2526_dict_gw.keys(
        ) if col in season2526_weekly.columns]
        s2526_weekly_df = season2526_weekly[s2526_gw].rename(
            columns=s2526_dict_gw)
        return s2526_weekly_df


"""S2526_season_weekly = S2526Weekly()
s2526_weekly_df = S2526_season_weekly.get_s2526_weekly_data()  # weekly data for 25/26
print(s2526_weekly_df.sort_values(
    by=["Game Week", "Total Points"], ascending=False))"""

# gw for 24/25
# url https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/gws/merged_gw.csv


class S2425Weekly():
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/gws/merged_gw.csv"

    def get_s2425_weekly_data(self):
        season2425_weekly = pd.read_csv(self.url)
        pos_map = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
        if "element_type" in season2425_weekly.columns:
            season2425_weekly["element_type"] = season2425_weekly["element_type"].map(
                pos_map)
        s2425_dict_gw = {
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
            'name'.lower(): 'Name',
            'element_type': 'Pos',
            'GW': 'Game Week',
            'was_home': 'Was Home',
            'opponent_team': 'O Team',
            'element': 'Player ID'
        }
        s2425_gw = [col for col in s2425_dict_gw.keys(
        ) if col in season2425_weekly.columns]
        s2425_weekly_df = season2425_weekly[s2425_gw].rename(
            columns=s2425_dict_gw)
        return s2425_weekly_df


"""S2425Weekly_season_weekly = S2425Weekly()  # weekly data for 24/25
s2425_weekly_df = S2425Weekly_season_weekly.get_s2425_weekly_data()
print(s2425_weekly_df.sort_values(
    by=["Game Week", "Total Points"], ascending=False))"""

# gw for 23/24
# url https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/gws/merged_gw.csv


class S2324Weekly():
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2023-24/gws/merged_gw.csv"

    def get_s2324_weekly_data(self):
        season2324_weekly = pd.read_csv(self.url)
        pos_map = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}
        if "element_type" in season2324_weekly.columns:
            season2324_weekly["element_type"] = season2324_weekly["element_type"].map(
                pos_map)
        s2324_dict_gw = {
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
            'name'.lower(): 'Name',
            'element_type': 'Pos',
            'GW': 'Game Week',
            'was_home': 'Was Home',
            'opponent_team': 'O Team',
            'element': 'Player ID'
        }
        s2324_gw = [col for col in s2324_dict_gw.keys(
        ) if col in season2324_weekly.columns]
        s2324_weekly_df = season2324_weekly[s2324_gw].rename(
            columns=s2324_dict_gw)
        return s2324_weekly_df


"""S2324Weekly_season_weekly = S2324Weekly()
# weekly data for 23/24
S2324_weekly_df = S2324Weekly_season_weekly.get_s2324_weekly_data()
print(S2324_weekly_df.sort_values(
    by=["Game Week", "Total Points"], ascending=False))"""
