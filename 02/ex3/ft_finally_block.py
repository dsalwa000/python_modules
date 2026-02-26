class Plant:
    def __init__(self, name: str):
        self.name = name


class PlantError(Exception):
    def __init__(self, message="Error: Cannot water None - invalid plant!"):
        super().__init__(message)


def water_plants(plant_list: list[Plant]):
    print("Opening watering system")
    try:
        for p in plant_list:
            if p is None:
                raise PlantError()
        for p in plant_list:
            print(f"Watering {p.name}")
    except PlantError as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print()
    print("Testing normal watering...")
    plant_list = [Plant("Rose"), Plant("BigRose"), Plant("Tree")]
    water_plants(plant_list)
    print("Watering completed successfully!")

    print()
    print("Testing with error...")
    incorrect_plant_list = [Plant("Rose"), None, Plant("Tree")]
    water_plants(incorrect_plant_list)

    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
