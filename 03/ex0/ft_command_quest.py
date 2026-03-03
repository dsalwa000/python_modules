#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")

    if sys.argv == 1:
        print("No arguments provided!")
    else:
        provided = sys.argv[1:]
        print(f"Amount of arguments: {len(provided)}")

        print("List of arguments: ")
        i = 0
        for arg in provided:
            print(f"Arg {i}: {arg}")
            i += 1


if __name__ == "__main__":
    main()
