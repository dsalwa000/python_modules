#!/usr/bin/env python3


def main() -> None:
    print("=== List Comprehension Examples ===")

    players = {
        {
            "name": "alice",
            "score": 4000,
            "active": True,
            "achievements": {
                "first_kill",
                "level_10",
                "treasure_hunter",
                "speed_demon"
            }
        },
        {
            "name": "bob",
            "score": 2100,
            "active": False,
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
            "achievements": {
                "level_10",
                "treasure_hunter",
                "boss_slayer",
                "speed_demon",
                "perfectionist"
            }
        }
    }

    high_scorers = [player.score for player in players if player.score > 2000]
    print(high_scorers)


if __name__ == "__main__":
    main()
