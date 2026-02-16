class GardenStats:


class GardenManager:
    def __init__(self, garden_name: str):
        self.garden_name = garden_name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.garden_name}'s garden")

    def grow(self):
        print(f"{self.garden_name} is helping all plants grow...")
        for plant in self.plants:
            print(f"{plant.name} grew 1cm")
            plant.height += 1

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, blooming: str):
        super().__init__(name, height)
        self.blooming = blooming

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, blooming: str, prizePoints: int):
        super().__init__(name, height, blooming)
        self.prizePoints = prizePoints

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
