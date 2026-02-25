class Plant:
    def __init__(self, name : str, height : int, age : int) -> None :
        self.name = name
        self.height = height
        self.age = age
    def grow(self) -> None:
        self.height = self.height + 1
        print(f"{self.name} grew 1cm")

class FloweringPlant(Plant):
    def __init__(self, name : str, height : int, age : int , colore : str, bloming : bool) -> None :
        super().__init__(name, height, age)
        self.color = colore
        self.bloming = bloming
    def get_info(self) -> None:
        if self.bloming == True:
            print(f"{self.name}: {self.height}cm, {self.color} (blooming)")
        else:
            print(f"{self.name}: {self.height}cm, {self.color} (not blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name : str, height : int, age : int , colore : str, prize_points : int) -> None :
        super().__init__(name, height, age, colore)
        self.prize_points = prize_points
    def get_info(self) -> None:
        super().get_info()

class GardenManager:
    def __init__(self, owner : str) -> None:
        self.name = owner
        self.list_plants = []
    
    @classmethod
    def create_garden_network(cls, list_owners : list)-> list:
        garden_list = []
        for x in list_owners:
            garden_list = garden_list + [cls(x)]
        return garden_list
    @staticmethod
    def  loo():
        pass
    def add_plant(self, plant : Plant) -> None:
        self.list_plants += [plant]
        print(f"Added {plant.name} to {self.name}'s garden")

    class GardenStats:
        pass

alice = GardenManager("alice")
rose = FloweringPlant("rose", 25, 16,"red")
alice.add_plant(rose)