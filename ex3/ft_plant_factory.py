class Plant:
    def __init__(self, name : str, height : int, age : int) -> None :
        self.name = name
        self.height = height
        self.age = age


plants = [
    ["Rose", 25, 30],
    ["Oak", 200, 365],
    ["Cactus", 5, 90],
    ["Sunflower", 80, 45],
    ["Fern", 15, 120]]
j = 0
for x in plants :
        plants[j] = Plant(x[0],x[1],x[2])
        j = j + 1
if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    for x in plants:
        print(f"Created : {x.name} ({x.height}cm, {x.age} days)")
    print(f"\nTotal plants created:",j)