class Plant:
    def __init__(self, name, heigth, age):
        self.name = name
        self.heigth = heigth
        self.age = age

if (__name__ == "__main__"):
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]

    for i in range(0, 3):
        print(f"{plants[i].name}: {plants[i].heigth}cm, {plants[i].age} days old")