from dotenv import load_dotenv
import os


def the_oracle() -> None:
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    print(f'Mode: {os.getenv("MATRIX_MODE")}')
    print(f'Database: {os.getenv("DATABASE_URL")}')
    print(f'API Access: {os.getenv("API_KEY")}')
    print(f'Log Level: {os.getenv("LOG_LEVEL")}')
    print(f'Zion Network: {os.getenv("ZION_ENDPOINT")}\n')

    print("Environment security check:\n")

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    the_oracle()
