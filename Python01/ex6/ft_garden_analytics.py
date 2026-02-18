class GardenManager:
    def __init__(self, name):
        self.name = name
        self.plants = []
        self.stats = self.GardenStatus

    def add_plant(self, plant):
        self.plants.append()
        print(f"Added {plant} Tree to {self.name}'s garden")

    def help_grow(self, grow):
        for i in range(len(self.plants)):
            self.plants[i].height += grow
            self.stats.total_growth += grow
            print(f"{self.plants[i].name} grew {grow}cm")

    class GardenStatus:
        def __init__(self, garden_manager):
            self.garden_manager = garden_manager
            self.total_growth = 0

        def report(self):
            plants_amount = len(self.garden_manager.plants)
            print(f"Plants added: {plants_amount},"
                  f"Total growth: {self.total_growth}cm")

        def plants_type_info(self):
            plants = self.garden_manager.plants
            print(f"=== {self.garden_manager.name}'s Garden Report ===")
            print("Plants in garden:")
            for i in range(len(self.plants)):
                

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, blooming: str):
        super().__init__(name, height)
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, blooming: str, prize_points: int):
        super().__init__(name, height, blooming)
        self.prize_points = prize_points
