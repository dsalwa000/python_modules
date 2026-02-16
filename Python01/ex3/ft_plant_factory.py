class Plant:
    plants = 0

    def __init__(self, name: str, height: int, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age
        print(f"Created: {self.name} ({self.height}cm, {self.plant_age} days)")
        Plant.plants += 1
    
    def total_plants(self):
        print(f"Total plants created: {self.plants}")

if __name__ == "__main__":
    rose = Plant("Rose", 15, 2)
    sunflower = Plant("Sunflower", 30, 5)
    cactus = Plant("Cactus", 5, 50)
    oak = Plant("Oak", 50, 10)
    lavender = Plant("Lavender", 10, 3)
    rose.total_plants()