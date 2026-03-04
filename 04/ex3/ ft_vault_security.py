#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    try:
        with open("ancient_fragment.txt", "r", encoding="utf-8") as file:
            contains = file.read()
            print(contains)

    except IOError as e:
        print(f"The file doesn't exists: {e}")

    print("\nData recovery complete. Storage unit disconnected")


if __name__ == "__main__":
    main()Znacz
