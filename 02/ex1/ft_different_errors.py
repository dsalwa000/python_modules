def garden_operations():
    print("Testing ValueError...")
    try:
        int("convert")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("Testing ZeroDivisionError...")
    try:
        print(f"{10 / 0}")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    object = {"key": 1}
    try:
        object["big_key"]
    except KeyError as exc:
        print(f"Caught KeyError: {exc}\n")

    print("Testing multiple errors together...")
    try:
        int("10 / 0")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")
