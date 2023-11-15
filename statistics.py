from collections import defaultdict


def calculate_statistics(player_stats, name):
    if player_stats is None:
        return None

    ftm = float(player_stats["FTM"])
    fta = float(player_stats["FTA"])
    two_pm = float(player_stats["2PM"])
    two_pa = float(player_stats["2PA"])
    three_pm = float(player_stats["3PM"])
    three_pa = float(player_stats["3PA"])
    reb = float(player_stats["REB"])
    blk = float(player_stats["BLK"])
    ast = float(player_stats["AST"])
    stl = float(player_stats["STL"])
    tov = float(player_stats["TOV"])
    games_played = int(player_stats["games_played"])

    ftp = ftm / fta * 100 if fta > 0 else 0
    two_pp = two_pm / two_pa * 100 if two_pa > 0 else 0
    three_pp = three_pm / three_pa * 100 if three_pa > 0 else 0
    pts = ftm + 2 * two_pm + 3 * three_pm
    val = (pts + reb + blk + ast + stl) - (fta - ftm + two_pa - two_pm + three_pa - three_pm + tov)
    efgp = (two_pm + 1.5 * three_pm) / (two_pa + three_pa) * 100 if (two_pa + three_pa) > 0 else 0
    attempts_ratio = two_pa + three_pa + 0.475 * fta
    tsp = pts / (2 * attempts_ratio) * 100 if (2 * attempts_ratio) > 0 else 0
    hastp = ast / (attempts_ratio + ast + tov) * 100 if (attempts_ratio + ast + tov) > 0 else 0

    return {
        "playerName": name,
        "gamesPlayed": games_played,
        "traditional": {
            "freeThrows": {
                "attempts": round(fta, 1),
                "made": round(ftm, 1),
                "shootingPercentage": round(ftp, 1)
            },
            "twoPoints": {
                "attempts": round(two_pa, 1),
                "made": round(two_pm, 1),
                "shootingPercentage": round(two_pp, 1)
            },
            "threePoints": {
                "attempts": round(three_pa, 1),
                "made": round(three_pm, 1),
                "shootingPercentage": round(three_pp, 1)
            },
            "points": round(pts, 1),
            "rebounds": round(reb, 1),
            "blocks": round(blk, 1),
            "assists": round(ast, 1),
            "steals": round(stl, 1),
            "turnovers": round(tov, 1)
        },
        "advanced": {
            "valorization": round(val, 1),
            "effectiveFieldGoalPercentage": round(efgp, 1),
            "trueShootingPercentage": round(tsp, 1),
            "hollingerAssistRatio": round(hastp, 1)
        }
    }


def calculate_average_statistic(data):
    player_stats = defaultdict(list)

    for row in data:
        player = row["PLAYER"]
        player_stats[player].append(row)

    average_stats = {}

    for player, player_rows in player_stats.items():
        games_played = len(player_rows)
        total_stats = {
            key: sum(int(row[key]) for row in player_rows)
            for key in player_rows[0].keys() if key != 'PLAYER' and key != 'POSITION'
        }
        average_stats[player] = {key: total_stats[key] / games_played for key in total_stats.keys()}
        average_stats[player]["games_played"] = games_played

    return average_stats
