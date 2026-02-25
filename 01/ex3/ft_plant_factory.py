class Plant:
    plants = 0

    def __init__(self, name: str, heigth: int, plant_age: int):
        self.name = name
        self.heigth = heigth
        self.plant_age = plant_age

        print(f"Created: {self.name} ({self.heigth}cm, {self.plant_age} days)")
        Plant.plants += 1

    def total_plants(self) -> None:
        print(f"Total plants created: {self.plants}")


if __name__ == "__main__":
    rose = Plant("Rose", 15, 2)
    sunflower = Plant("Sunflower", 30, 5)
    cactus = Plant("Cactus", 5, 50)
    oak = Plant("Oak", 50, 10)
    lavender = Plant("Lavender", 10, 3)
    print()
    rose.total_plants()
