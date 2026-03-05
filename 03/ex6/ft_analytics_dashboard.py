#!/usr/bin/env python3
from typing import TypedDict


class Player(TypedDict):
    name: str
    score: int
    active: bool
    region: str
    achievements: set[str]


def main() -> None:
    players: list[Player] = [
        {
            "name": "alice",
            "score": 2100,
            "active": True,
            "region": "east",
            "achievements": {
                "first_kill",
                "level_10",
                "treasure_hunter",
                "speed_demon"
            }
        },
        {
            "name": "bob",
            "score": 1900,
            "active": False,
            "region": "north",
            "achievements": {
                "first_kill",
                "level_10",
                "boss_slayer",
                "collector"
            }
        },
        {
            "name": "charlie",
            "score": 2100,
            "active": True,
            "region": "north",
            "achievements": {
                "level_10",
                "treasure_hunter",
                "boss_slayer",
                "speed_demon",
                "perfectionist"
            }
        }
    ]

    print("=== List Comprehension Examples ===")

    high_scorers: list[str] = [
        player["name"]
        for player in players
        if player["score"] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    seen: set[int] = set()
    duplicates: set[int] = set()

    for player in players:
        score = player["score"]
        if score in seen:
            duplicates.add(score)
        else:
            seen.add(score)

    doubles: list[str] = [duplicate for duplicate in duplicates]
    print(f"Scores doubled: {doubles}")

    active_players = [
        player["name"]
        for player in players
        if player["active"] is True
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores: list[str] = {
        player["name"]: player["score"]
        for player in players
    }
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        "high": 0,
        "medium": 0,
        "low": 0
    }
    for player in players:
        score = player["score"]

        if 2000 <= score:
            score_categories["high"] += 1
        elif 1800 <= score < 2000:
            score_categories["medium"] += 1
        else:
            score_categories["low"] += 1

    print(f"Score categories: {score_categories}")

    achievements = {}
    for player in players:
        name = player["name"]
        count = 0

        for _ in player["achievements"]:
            count += 1

        achievements[name] = count

    print(f"Achievement counts: {achievements}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {
        player["name"]
        for player in players
    }
    print(f"Unique players: {unique_players}")

    unique_achievements: set[str] = set()
    for player in players:
        for achievement in player["achievements"]:
            unique_achievements.add(achievement)
    print(f"Unique achievements: {unique_achievements}")

    active_regions: set[str] = {
        player["region"]
        for player in players
        if player["active"] is True
    }
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    average_score: list[int] = sum([player["score"] for player in players])
    print(f"Average score: {(average_score / len(players)):.1f}")

    top_score: int = max([player["score"] for player in players])
    top_performer: Player = None

    for player in players:
        if top_score == player["score"]:
            top_performer = player
            break

    print(f"Top performer: {top_performer['name']} "
          f"({top_performer['score']} points, "
          f"{len(top_performer['achievements'])} achievements)\n")


if __name__ == "__main__":
    main()
