class Plant:
    def __init__(self, name : str, height : int, age : int) -> None :
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    fleur = Plant("Sunflower", 80, 45)
    sunflower = Plant("Cactus", 15, 120)
    palnt_list = [rose, fleur, sunflower]
    for i in range(3):
        print(palnt_list[i].name, ": ", sep="", end="")
        print(palnt_list[i].height,"cm,", palnt_list[i].age,"days old")