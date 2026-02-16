class Plant:
    def __init__(self, name: str, height: int, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age

class Flower(Plant):
    def __init__(self, name: str, height: int, plant_age: int, color: str):
        super().__init__(name, height, plant_age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, {self.plant_age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name: str, height: int, plant_age: int, trunk_diameter: int):
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
        self.shadow_area = 3.14 * ((trunk_diameter / 2) ** 2)
        print(f"{self.name} (Tree): {self.height}cm, {self.plant_age} days, {self.trunk_diameter}cm diameter")
    
    def produce_shade(self):
        print(f"Oak provides {self.shadow_area} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, plant_age: int, harvest: str, nutritional_value: str):
        super().__init__(name, height, plant_age)
        self.harvest = harvest
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Tree): {self.height}cm, {self.plant_age} days, {self.harvest} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")

if __name__ == "__main__":
    rose = Flower("Rose", 15, 30, "Red")
    tulip = Flower("Tulip", 10, 20, "Yellow")
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50) 
    pine = Tree("Pine", 300, 1000, 30)
    oak.produce_shade()

    carrot = Vegetable("Carrot", 20, 60, "Autumn", "Vitamin A")
    tomato = Vegetable("Tomato", 120, 90, "Summer", "Lycopene")
