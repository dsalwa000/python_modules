#!/usr/bin/env python3
import sys


class InputError(Exception):
    def __init__(self, message="Input error") -> None:
        super().__init__(message)


def main() -> None:
    try:
        if len(sys.argv) == 1:
            raise InputError("No arguments")

        strScoreBoard: list[str] = sys.argv[1:]
        scoreBoard: list[int] = []

        for score in strScoreBoard:
            scoreBoard.append(int(score))

        totalScore: int = 0
        for score in scoreBoard:
            totalScore += score

        print(f"Scores processed: {scoreBoard}")
        print(f"Total players {len(scoreBoard)}")
        print(f"Total score {totalScore}")
        print(f"Average score {totalScore / 5}")
        print(f"High score {max(scoreBoard)}")
        print(f"Low score {min(scoreBoard)}")
        print(f"Score range {max(scoreBoard) - min(scoreBoard)}")

    except ValueError as e:
        print(f"ValueError: {e}")
    except InputError as e:
        print(f"InputError: {e}")


if __name__ == "__main__":
    main()
