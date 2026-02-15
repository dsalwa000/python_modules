class SecurePlant:
    def __init__(self, name, heigth, plant_age):
        self.__name = name
        self.__heigth = heigth
        self.__plant_age = plant_age
        print(f"Plant created: : {self.__name}")
    
    def __alert(self, type, value, unit):
        print(f"Invalid operation attempted: {type} {value}{unit} [REJECTED]")
        print(f"Security: Negative {type} rejected")
    
    def set_height(self, heigth):
        if (heigth <= 0):
            self.__alert("heigth", heigth, "cm")
            return
        self.__heigth = heigth
        print(f"Height updated: {self.__heigth}cm [OK]")

    def set_age(self, age):
        if (age <= 0):
            self.__alert("age", age, " days")
            return
        self.__plant_age = age
        print(f"Age updated: {self.__plant_age} days [OK]")

    def get_height(self):
        return self.__heigth

    def get_age(self):
        return self.__plant_age
    
    def get_info(self):
        print(f"Current plant: {self.__name} ({self.__heigth}cm, {self.__plant_age} days)")


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