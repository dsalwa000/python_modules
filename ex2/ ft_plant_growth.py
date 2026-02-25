class Plant:
    def __init__(self, name: str, heigth: int, plant_age: int):
        self.name = name
        self.heigth = heigth
        self.plant_age = plant_age

    def grow(self) -> None:
        self.heigth += 1

    def age(self) -> None:
        self.plant_age += 1
        self.grow()

    def get_info(self) -> None:
        print(f"{self.name}: {self.heigth}cm, {self.plant_age} days old")

    def week_simulation(self) -> None:
        difference = self.heigth
        print("=== Day 1 ===")
        self.get_info()
        for _ in range(0, 6):
            self.age()
        print("=== Day 7 ===")
        self.get_info()
        print(f"Growth this week: +{self.heigth - difference}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)

    rose.week_simulation()
    print()
    sunflower.week_simulation()
