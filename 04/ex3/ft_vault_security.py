#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    try:
        with open("classified_vault.txt", "r", encoding="utf-8") as file:
            contains = file.read()
            print(contains)

    except IOError as e:
        print(f"The file doesn't exists: {e}")

    print("\nSECURE PRESERVATION:")
    try:
        with open("classified_vault.txt", "w", encoding="utf-8") as file:
            classified: str = "[CLASSIFIED] New security protocols archived"

            file.write(classified)
            print(classified)

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
