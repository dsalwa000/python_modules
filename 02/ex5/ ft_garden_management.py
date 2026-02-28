class PlantError(Exception):
    def __init__(self, message="Plant error"):
        super().__init__(message)


class GardenError(Exception):
    def __init__(self, message="Garden error:"):
        super().__init__(message)


class GardenManagerError(Exception):
    def __init__(self, message="Garden Manager error:"):
        super().__init__(message)


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class Garden:
    def __init__(self, name: str):
        self.name: str = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant):
        try:
            if plant.name == "":
                raise GardenError("Error adding plant: "
                                  "Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except GardenError as e:
            print(f"{e}")


class GardenManager:
    def __init__(self):
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden):
        try:
            if garden.name == "":
                raise GardenManagerError("Error adding garden: "
                                         "Garden name cannot be empty!")
            self.gardens.append(garden)
            print(f"Added garden {garden.name} successfully")
        except GardenManagerError as e:
            print(f"GardenManagerError: {e}")

    def add_plant(self, garden: Garden, plant: Plant):
        try:
            if not self.find_garden(garden):
                raise GardenManagerError("Garden not found")
            garden.add_plant(plant)
        except GardenManagerError as e:
            print(f"GardenManagerError: {e}")

    def check_plant_health(self, garden: Garden, plant: Plant):
        try:
            if not self.find_garden(garden):
                raise GardenManagerError("Garden not found")
            if not self.find_plant(garden, plant):
                raise GardenManagerError("Plant not found")

            if not 0 <= plant.water_level <= 10:
                raise PlantError("Water level must be between 0 and 10")
            if not 2 <= plant.sunlight_hours <= 12:
                raise PlantError("Sunligth hours must be reasonable (2 to 12)")

            print(f"Plant '{plant.name}' is healthy!")
        except GardenManagerError as e:
            print(f"GardenManagerError: {e}")
        except PlantError as e:
            print(f"PlantError: {e}")
        finally:
            print("Closed plant check")

    def water_plants(self, garden: Garden):
        try:
            if not self.find_garden(garden):
                raise GardenManagerError("Garden not found")

            print("Opening watering system")
            for plant in garden.plants:
                if plant is None:
                    raise PlantError("Invalid plant")
            for plant in garden.plants:
                print(f"Watering {plant.name}")
                plant.water_level += 1
        except GardenManagerError as e:
            print(f"GardenManagerError: {e}")
        except PlantError as e:
            print(f"PlantError: {e}")
        finally:
            print("Closing watering system")

    def find_garden(self, garden_to_find: Garden) -> bool:
        for garden in self.gardens:
            if garden == garden_to_find:
                return True
        return False

    def find_plant(self, garden: Garden, plant_to_find: Plant) -> bool:
        for plant in garden.plants:
            if plant == plant_to_find:
                return True
        return False


def test_garden_manager():
    print("=== Garden Management System ===")

    manager = GardenManager()
    our_garden = Garden("Our garden")
    mock_garden = Garden("Mock garden")
    tomato = Plant("tomato", 5, 5)
    lettuce = Plant("lettuce", 2, 8)
    mock_plant = Plant("", -1, -1)

    print("Adding plants to garden...")
    our_garden.add_plant(tomato)
    our_garden.add_plant(lettuce)
    our_garden.add_plant(mock_plant)

    print()

    manager.add_garden(our_garden)

    print()

    print("Watering plants...")
    manager.water_plants(our_garden)
    print()
    manager.water_plants(mock_garden)

    print()

    print("Checking plant health...")
    manager.check_plant_health(our_garden, tomato)

    print()

    print("Testing error recovery...")
    manager.check_plant_health(our_garden, mock_plant)

    print()
    print("Garden management system test complete!")


if __name__ == '__main__':
    test_garden_manager()
