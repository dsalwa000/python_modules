import sys
import site


def simulate_construct():
    in_environment: bool = False
    if sys.prefix != sys.base_prefix:
        in_environment = True

    matrix_status = (
        "Welcome to the construct"
        if in_environment
        else "You're still plugged in"
    )

    print(f"MATRIX STATUS: {matrix_status}\n")

    print(f"Current Python: {sys.executable}")

    virtual_env = (
        sys.prefix
        if in_environment
        else "None detected"
    )
    print(f"Virtual Environment: {virtual_env}\n")

    if in_environment:
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        print(site.getsitepackages())
    else:
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("After that activate your environment using source")

        print("\nThen run this program again.")


if __name__ == "__main__":
    simulate_construct()
