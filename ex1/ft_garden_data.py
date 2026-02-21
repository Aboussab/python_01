class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = str(height) + "cm"
        self.age = str(age) + " days old"


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    fleur = Plant("Sunflower", 80, 45)
    sunflower = Plant("Cactus", 15, 120)
    palnt_list = [rose, fleur, sunflower]
    for i in range(3):
        print(palnt_list[i].name, ": ", sep="", end="")
        print(palnt_list[i].height, ", ", ", ", palnt_list[i].age, sep="")
