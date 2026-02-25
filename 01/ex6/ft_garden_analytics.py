from __future__ import annotations


class Garden:
    def __init__(self, name: str):
        self.name: str = name
        self.plants: list[Plant] = []
        self.count = 0
        self.grow = 0
        self.types: dict[type[Plant], int] = {
            Plant: 0,
            FloweringPlant: 0,
            PrizeFlower: 0
        }
        self.points = 0

    def add_plant(self, plant: Plant) -> None:
        print(f"Added {plant.name} to the {self.name} garden")
        self.plants.append(plant)
        self.count += 1
        self.types[type(plant)] += 1
        if (isinstance(plant, PrizeFlower)):
            self.points += plant.points


class GardenManager:
    def __init__(self):
        self.gardens: list[Garden] = []
        self.gardens_count = 0
        self.stats = self.GardenStats(self)

    class GardenStats:
        def __init__(self, manager: GardenManager):
            self.manager = manager

        def create_report(self, garden_name: str) -> None:
            garden = self.manager.find_garden(garden_name)

            if not garden:
                print("Garden not found")
                return

            print(f"=== {garden.name} Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                print(plant.report_line())

            print()
            print(f"Plants added: {garden.count}, "
                  f"Total growth: {garden.grow}cm")

            print(
                f"Plant types: {garden.types[Plant]} regular, "
                f"{garden.types[FloweringPlant]} flowering, "
                f"{garden.types[PrizeFlower]} prize flowers"
            )

            print()
            score_list = ", ".join(
                f"{garden.name}: {garden.points}"
                for garden in self.manager.gardens
            )
            print(f"Garden scores - {score_list}")

            print(f"Total gardens managed: {self.manager.gardens_count}")

    def add_garden(self, garden: Garden) -> None:
        print(f"Garden {garden.name} added to the manager")
        self.gardens.append(garden)
        self.gardens_count += 1

    def grow_plants(self, garden_name: str, grow: int) -> None:
        garden = self.find_garden(garden_name)

        if not garden:
            print("Garden not found")
            return

        print(f"In {garden.name} plants grow")

        for plant in garden.plants:
            print(f"{plant.name} grew {grow}cm")
            plant.size += grow
            garden.grow += grow

    def find_garden(self, name: str) -> Garden | None:
        for garden in self.gardens:
            if garden.name == name:
                return garden
        return None


class Plant:
    _total_plants = 0

    def __init__(self, name: str, size: int):
        self.name = name

        if not Plant.is_valid_size(size):
            self.size = 1
        else:
            self.size = size
        Plant._total_plants += 1

    def report_line(self) -> str:
        return f"- {self.name}: {self.size}cm"

    @classmethod
    def get_total_plants(cls) -> int:
        return cls._total_plants

    @staticmethod
    def is_valid_size(size: int) -> bool:
        return size >= 0


class FloweringPlant(Plant):
    def __init__(self, name: str, size: int, color: str, blooming: bool):
        super().__init__(name, size)
        self.blooming = blooming
        self.color = color

    def report_line(self) -> str:
        base = f"{super().report_line()}"
        blooming = "blooming" if self.blooming else "not blooming"

        return f"{base} {self.color} flowers ({blooming})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        size: int,
        color: str,
        blooming: bool,
        points: int,
    ):
        super().__init__(name, size, color, blooming)
        self.points = points

    def report_line(self) -> str:
        base = f"{super().report_line()}"

        return f"{base}, Prize points: {self.points}"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    nice_garden = Garden("Nice")
    not_nice_garden = Garden("Not Nice")

    rose = FloweringPlant("Rose", 10, "red", True)
    sunflower = PrizeFlower("Sunflower", 10, "yellow", False, 10)
    big_rose = PrizeFlower("Big Rose", 40, "red", True, 32)

    garden_manager = GardenManager()
    garden_manager.add_garden(nice_garden)
    garden_manager.add_garden(not_nice_garden)

    print()

    nice_garden.add_plant(rose)
    nice_garden.add_plant(sunflower)
    not_nice_garden.add_plant(big_rose)

    print()

    garden_manager.grow_plants("Nice", 4)

    print()

    garden_manager.stats.create_report("Nice")

    print()

    garden_manager.stats.create_report("Not Nice")

    print()
    print(f"Total plants: {Plant.get_total_plants()}")
