#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r", encoding="utf-8") as file:
            contains: str = file.read()

            print(contains)

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")

    print("STATUS: Crisis handled, system stable\n")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "w", encoding="utf-8") as file:
            contains: str = file.read()

            print(contains)

    except PermissionError:
        print("RESPONSE: Security protocols deny access")

    print("STATUS: Crisis handled, system stable\n")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r", encoding="utf-8") as file:
            contains: str = file.read()

            print(f"SUCCESS: Archive recovered - ``{contains}``")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")

    print("STATUS: Crisis handled, system stable\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
