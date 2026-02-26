class PlantError(Exception):
    def __init__(self, message="Plant error"):
        super().__init__(message)


class GardenError():
    def __init__(self, message="Garden error:"):
        super().__init__(message)

    def lack_of_water(self):
        return "Not enough water in the tank!"


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
                raise GardenManager("Error adding plant: "
                                    "Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except GardenError as e:
            print(f"{e}")


class GardenManager:
    def __init__(self):
        self.plants: list[Garden] = []

    def add_garden(self, garden: Garden):
        try:
            if garden.name == "":
                raise PlantError("Error adding garden: "
                                 "Garden name cannot be empty!")
            self.plants.append(garden)
            print(f"Added garden {garden.name} successfully")
        except PlantError as e:
            print(f"{e}")

    def check_plant_health(self, name: str):
        for p in self.plants:
            if p.name == name:
                plant = p
        try:
            if not p:
                raise PlantError("Plant not found")
            if not 0 <= plant.water_level <= 10:
                raise PlantError("Water level must be between 0 and 10")
            if not 2 <= plant.sunlight_hours <= 12:
                raise PlantError("Sunligth hours must be reasonable (2 to 12)")
            print(f"Plant '{plant.name}' is healthy!")
        except PlantError as e:
            print(f"Health check: {e}")
        finally:
            print("Closed plant check")

    def water_plants(self):
        print("Opening watering system")
        try:
            for p in self.plants:
                if p is None:
                    raise PlantError("Invalid plant")
            for p in self.plants:
                print(f"Watering {p.name}")
                p.water_level += 1
        except PlantError as e:
            print(f"PlantError: {e}")
        finally:
            print("Closing watering system")


def test_garden_manager():
    print("=== Garden Management System ===")

    manager = GardenManager()
    tomato = Plant("tomato", 5, 5)
    lettuce = Plant("lettuce", 2, 8)

    print("Proper adding of plants")
    manager.add_plant(tomato)
    manager.add_plant(lettuce)
    manager.add_plant("")

    print()

    manager.water_plants()

    print()

    manager.check_plant_health("tomato")
    manager.check_plant_health("not_existing_tomato")

# Na jutro:
# Testing error recovery...
# Caught GardenError: Not enough water in tank
# System recovered and continuing...
