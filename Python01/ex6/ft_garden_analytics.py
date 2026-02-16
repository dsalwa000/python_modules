class GardenManager:
    class GardenStats:
        def __init__(self):
            self.total_plants = 0
            self.total_height = 0
            self.total_points = 0

        def calculate(self, plants_list):
            self.total_plants = 0
            self.total_height = 0
            self.total_points = 0
            
            for p in plants_list:
                self.total_plants += 1
                self.total_height += p.height
                self.total_points += p.get_prize_points()

    def __init__(self, garden_name: str):
        self.garden_name = garden_name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.garden_name}'s garden")

    def grow(self):
        print(f"\n{self.garden_name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew to {plant.height}cm")

    def show_analytics(self):
        stats = self.GardenStats()
        stats.calculate(self.plants)
        print(f"\n--- Analytics for {self.garden_name} ---")
        print(f"Total plants: {stats.total_plants}")
        print(f"Total height: {stats.total_height}cm")
        print(f"Total prize points: {stats.total_points}")

    @classmethod
    def create_garden_network(cls, names):
        print("\nCreating garden network...")
        network = []
        for name in names:
            network.append(cls(name))
        return network

    @staticmethod
    def print_garden_utility():
        print("Utility Tip: Remember to water plants based on their blooming season!")

class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def get_prize_points(self):
        return 0

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, blooming: str):
        super().__init__(name, height)
        self.blooming = blooming

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, blooming: str, prize_points: int):
        super().__init__(name, height, blooming)
        self.prize_points = prize_points

    def get_prize_points(self):
        return self.prize_points

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    GardenManager.print_garden_utility()

    garden_names = ["Royal Park", "Community Patch"]
    network = GardenManager.create_garden_network(garden_names)
    
    main_garden = network[0]

    main_garden.add_plant(Plant("Basic Fern", 15))
    main_garden.add_plant(FloweringPlant("Red Rose", 20, "Spring"))
    main_garden.add_plant(PrizeFlower("Golden Tulip", 25, "Summer", 100))

    for i in range(2):
        print(f"\n--- Day {i + 1} ---")
        main_garden.grow()

    main_garden.show_analytics()