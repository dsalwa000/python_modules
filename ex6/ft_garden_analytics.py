class GardenStats:


class GardenManager:
    def __init__(self, name, heigth, plant_age):
        self.name = name

class Plant:
    def __init__(self, name, heigth, plant_age):
        self.name = name
        self.heigth = heigth
        self.plant_age = plant_age
        print(f"Created: {self.name} ({self.heigth}cm, {self.plant_age} days)")
        Plant.plants += 1

class FloweringPlant(Plant):
    def __init__(self, name, heigth, plant_age):
        self.name = name
        self.heigth = heigth
        self.plant_age = plant_age
        print(f"Created: {self.name} ({self.heigth}cm, {self.plant_age} days)")
        Plant.plants += 1

class PrizeFlower(FloweringPlant):
    def __init__(self, name, heigth, plant_age):
        self.name = name
        self.heigth = heigth
        self.plant_age = plant_age
        print(f"Created: {self.name} ({self.heigth}cm, {self.plant_age} days)")
        Plant.plants += 1

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
