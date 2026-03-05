class GardenError(Exception):
    def __init__(self, message="Caught GardenError!"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Caught PlantError:"):
        super().__init__(message)

    def wilting_plant(self):
        return "The tomato plant is wilting!"


class WaterError(PlantError):
    def __init__(self, message="Caught WaterError:"):
        super().__init__(message)

    def lack_of_water(self):
        return "Not enough water in the tank!"


class Garden:
    def garden_problem(self):
        print("Testing GardenError...")
        try:
            raise GardenError()
        except GardenError as e:
            print(f"{e}")

    def wilting_plant_error(self):
        print("Testing PlantError...")
        try:
            raise PlantError()
        except PlantError as e:
            print(f"{e} {e.wilting_plant()}")

    def lack_of_water_error(self):
        print("Testing WaterError...")
        try:
            raise WaterError()
        except WaterError as e:
            print(f"{e} {e.lack_of_water()}")


def test_errors():
    print("=== Custom Garden Errors Demo ===")
    garden = Garden()
    garden.garden_problem()
    garden.wilting_plant_error()
    garden.lack_of_water_error()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
