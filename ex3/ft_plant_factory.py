class Plant:
    def __init__(self, name : str, height : int, age : int) -> None :
        self.name = name
        self.height = height
        self.age_cur = age

if __name__ == "__main__":
    plants = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]]
    for x in plants:
        