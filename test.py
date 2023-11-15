import unittest
from reader import read_csv
from statistics import calculate_statistics, calculate_average_statistic


class Test(unittest.TestCase):
    def test_read_csv_does_not_exit_on_existing_file(self):
        try:
            read_csv("test.csv")
        except SystemExit:
            self.fail("File doesn't exist")

    def test_read_csv_exits_on_nonexistent_file(self):
        with self.assertRaises(SystemExit):
            read_csv("a791jaSgnhgAfqaoiAGA.csv")

    def test_read_csv_exits_on_bad_header(self):
        with self.assertRaises(SystemExit):
            read_csv("badHeader.csv")

    def test_read_csv_exits_on_bad_row_length(self):
        with self.assertRaises(SystemExit):
            read_csv("badRowLength.csv")

    def test_read_csv_exits_on_bad_data(self):
        with self.assertRaises(SystemExit):
            read_csv("badData.csv")

    def test_calculate_statistics_is_valid(self):
        player_stats = {
            "FTM": 5,
            "FTA": 7,
            "2PM": 10,
            "2PA": 15,
            "3PM": 3,
            "3PA": 5,
            "REB": 8,
            "BLK": 2,
            "AST": 4,
            "STL": 2,
            "TOV": 1,
            "games_played": 5,
        }

        result = calculate_statistics(player_stats, "Test Name")

        expected_result = {
            "playerName": "Test Name",
            "gamesPlayed": 5,
            "traditional": {
                "freeThrows": {"attempts": 7.0, "made": 5.0, "shootingPercentage": 71.4},
                "twoPoints": {"attempts": 15.0, "made": 10.0, "shootingPercentage": 66.7},
                "threePoints": {"attempts": 5.0, "made": 3.0, "shootingPercentage": 60.0},
                "points": 34.0,
                "rebounds": 8.0,
                "blocks": 2.0,
                "assists": 4.0,
                "steals": 2.0,
                "turnovers": 1.0
            },
            "advanced": {
                "valorization": 40.0,
                "effectiveFieldGoalPercentage": 72.5,
                "trueShootingPercentage": 72.9,
                "hollingerAssistRatio": 14.1
            }
        }
        self.assertEqual(result, expected_result)

    def test_calculate_average_statistic_is_valid(self):
        data = [
            {"PLAYER": "Player Test", "POSITION": "PG", "FTM": "2", "FTA": "3", "2PM": "5", "2PA": "10",
             "3PM": "2", "3PA": "4", "REB": "5", "BLK": "4", "AST": "3", "STL": "2", "TOV": "0"},
            {"PLAYER": "Player Test", "POSITION": "PG", "FTM": "1", "FTA": "2", "2PM": "3", "2PA": " 5",
             "3PM": "2", "3PA": "3", "REB": "2", "BLK": "0", "AST": "8", "STL": "0", "TOV": "2"},
            {"PLAYER": "Player Test", "POSITION": "SG", "FTM": "3", "FTA": "4", "2PM": "8", "2PA": "15",
             "3PM": "0", "3PA": "1", "REB": "3", "BLK": "1", "AST": "3", "STL": "1", "TOV": "1"},
            {"PLAYER": "Player Test", "POSITION": "SG", "FTM": "4", "FTA": "5", "2PM": "7", "2PA": "12",
             "3PM": "3", "3PA": "4", "REB": "6", "BLK": "3", "AST": "6", "STL": "1", "TOV": "1"},
        ]
        result = calculate_average_statistic(data)

        expected_result = {'Player Test': {'FTM': 2.5, 'FTA': 3.5, '2PM': 5.75, '2PA': 10.5, '3PM': 1.75, '3PA': 3.0,
                                           'REB': 4.0, 'BLK': 2.0, 'AST': 5.0, 'STL': 1.0, 'TOV': 1.0,
                                           'games_played': 4}}

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
