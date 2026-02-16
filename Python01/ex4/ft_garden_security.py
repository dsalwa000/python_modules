class SecurePlant:
    def __init__(self, name: str, height: int, plant_age: int):
        self.__name = name
        self.__height = height
        self.__plant_age = plant_age
        print(f"Plant created: : {self.__name}")
    
    def __alert(self, type, value, unit):
        print(f"Invalid operation attempted: {type} {value}{unit} [REJECTED]")
        print(f"Security: Negative {type} rejected")
    
    def set_height(self, height):
        if (height <= 0):
            self.__alert("height", height, "cm")
            return
        self.__height = height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age):
        if age <= 0:
            self.__alert("age", age, " days")
            return
        self.__plant_age = age
        print(f"Age updated: {self.__plant_age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__plant_age
    
    def get_info(self):
        print(f"Current plant: {self.__name} ({self.__height}cm, {self.__plant_age} days)")


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