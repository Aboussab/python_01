class GardenManager:
    def __init__(self, owner : str, plants : list) -> None:
        self.name = owner
        self.list_plants = plants
    
    @classmethod
    def create_garden_network(cls, list_owners : list)-> list:
        garden_list = []
        for x in list_owners:
            garden_list = garden_list + [cls(x)]
        return garden_list
    @staticmethod
    def  
    class GardenStats:
        pass


class Plant:
    def __init__(self, name : str, height : int, age : int) -> None :
        self.name = name
        self.height = height
        self.age = age

class FloweringPlant(Plant):
    def __init__(self, name : str, height : int, age : int , colore : str) -> None :
        super().__init__(name, height, age)
        self.color = colore


class PrizeFlower(FloweringPlant):
    def __init__(self, name : str, height : int, age : int , colore : str) -> None :
        super().__init__(name, height, age, colore)

