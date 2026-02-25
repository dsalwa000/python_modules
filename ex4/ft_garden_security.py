class SecurePlant:
    def __init__(self, name: str, heigth: int, plant_age: int):
        self.name = name
        self.heigth = heigth
        self.plant_age = plant_age

        print(f"Plant created: : {self.name}")

    def _validate(self, value: int, type: str, unit: str) -> bool:
        if value <= 0:
            print(
                f"Invalid operation attempted: "
                f"{type} {value}{unit} [REJECTED]"
            )
            print(f"Security: Negative {type} rejected")
            return False
        return True

    def set_height(self, heigth: int) -> None:
        if self._validate(heigth, "heigth", "cm"):
            self.heigth = heigth
            print(f"Height updated: {self.heigth}cm [OK]")

    def set_age(self, age: int):
        if self._validate(age, "age", " days"):
            self.plant_age = age
            print(f"Age updated: {self.plant_age} days [OK]")

    def get_height(self):
        return self.heigth

    def get_age(self):
        return self.plant_age

    def get_info(self):
        print(
            f"Current plant: {self.name} ({self.heigth}cm, "
            f"{self.plant_age} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 2)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.set_age(-5)
    print()
    rose.get_info()
