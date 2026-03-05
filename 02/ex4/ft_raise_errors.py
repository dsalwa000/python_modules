class PlantError(Exception):
    def __init__(self, message="Plant error"):
        super().__init__(message)


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    try:
        if (plant_name == ""):
            raise PlantError("Invalid plant name")
        if not 0 <= water_level <= 10:
            raise PlantError("Water level must be between 0 and 10")
        if not 2 <= sunlight_hours <= 12:
            raise PlantError("Sunligth hours must be reasonable (2 to 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except PlantError as e:
        print(f"{e}")


def test_plant_checks():
    print("Testing good values...")
    check_plant_health("tomato", 10, 4)

    print()

    print("Testing empty plant name...")
    check_plant_health("", 10, 4)

    print()

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 4)

    print()

    print("Testing bad water level...")
    check_plant_health("tomato", 5, 0)

    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
