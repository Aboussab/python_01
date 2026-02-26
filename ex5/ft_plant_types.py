class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, colore: str) -> None:
        super().__init__(name, height, age)
        self.color = colore

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days, ", end="")
        print(f"{self.color} color")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        n = (self.trunk_diameter/2) * 3.14
        print(f"{self.name} provides {n} square meters of shade")

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days,", end="")
        print(f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days, ", end="")
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


rose = Flower("Rose", 25, 15, "red")
rose.get_info()
rose.bloom()

print("\n")
oke = Tree("Oak", 500, 1825, 50)
oke.get_info()
oke.produce_shade()
print("\n")
tomate = Vegetable("Tomato", 80, 90, "summer", "vitamine C")
tomate.get_info()
