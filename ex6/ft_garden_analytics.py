class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth_tracker = 0
        self.type = "regular"

    def grow(self, cm) -> None:
        self.height = self.height + cm
        self.growth_tracker = cm
        print(f"{self.name} grew {cm}cm")

    def get_info(self) -> str:
        return (f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, colore: str, bloming: bool) -> None:
        super().__init__(name, height, age)
        self.color = colore
        self.bloming = bloming
        self.type = "flowering"

    def get_info(self) -> str:
        if self.bloming == True:
            return (super().get_info() + f", {self.color} flowers (blooming)")
        else:
            return (super().get_info() + f", {self.color} flowers (not blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, colore: str, bloming: bool, prize_points: int) -> None:
        super().__init__(name, height, age, colore, bloming)
        self.prize_points = prize_points
        self.type = "prize"

    def get_info(self) -> str:
        return (super().get_info() + f", prize_points :{self.prize_points}")


class GardenManager:
    garden_created = 0

    def __init__(self, owner: str) -> None:
        self.name = owner
        self.list_plants = []
        self.regular = 0
        self.flowering = 0
        self.prize = 0
        GardenManager.garden_created += 1

    class GardenStats:
        @staticmethod
        def plants_grow(garden) -> None:
            sume = 0
            j = 0
            for x in garden.list_plants:
                sume += x.growth_tracker
                j += 1
            print(f"Plants added: {j}, Total growth: {sume}cm")
            print(f"Plant types: {garden.regular} regular, {garden.flowering} flowering, {garden.prize} prize flowers")

    @classmethod
    def create_garden_network(cls, list_owners: list) -> list:
        garden_list = []
        for x in list_owners:
            garden_list = garden_list + [cls(x)]
        return garden_list

    def add_plant(self, plant: Plant) -> None:
        self.list_plants += [plant]
        if plant.type == "regular":
            self.regular += 1
        elif plant.type == "flowering":
            self.flowering += 1
        elif plant.type == "prize":
            self.prize += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def help_plants_grow(self, cm):
        print(f"\n{self.name} is helping all plants grow...")
        for p in self.list_plants:
            p.grow(cm)

    def garden_report(self):
        print(f"=== {self.name}'s Garden Report ===")
        for x in self.list_plants:
            print(x.get_info())

    def checke_height(self) -> bool:
        for x in self.list_plants:
            if x.height < 0:
                return False
        print(f"Height validation test: {True}")
        return True

    @classmethod
    def class_status(cls) -> None:
        print(f"Total gardens managed: {cls.garden_created}")


if __name__ == "__main__":
    alice = GardenManager("alice")
    Oak = Plant("Oak tree", 101, 30)
    rose = FloweringPlant("Rose", 25, 16, "red", True)
    Sunflower = PrizeFlower("Sunflower", 25, 16, "red", True, 10)
    print("=== Garden Management System Demo ===")
    print("\n")

    alice.add_plant(Oak)
    alice.add_plant(rose)
    alice.add_plant(Sunflower)
    print("\n\n")

    alice.help_plants_grow(9)
    print("\n")
    alice.garden_report()
    print("\n")

    alice.GardenStats.plants_grow(alice)
    alice.checke_height()
    GardenManager.class_status()
"""
./ft_garden_analytics.py:19:80: E501 line too long (93 > 79 characters)
./ft_garden_analytics.py:26:25: E712 comparison to True should be 'if cond is True:' or 'if cond:'
./ft_garden_analytics.py:29:80: E501 line too long (82 > 79 characters)
./ft_garden_analytics.py:33:80: E501 line too long (112 > 79 characters)
./ft_garden_analytics.py:62:80: E501 line too long (119 > 79 characters)
zid dok docstring o pushi Gn
 """