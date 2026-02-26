class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_cur = age

    def grow(self) -> None:
        self.height = self.height + 1

    def age(self) -> None:
        self.age_cur = self.age_cur + 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_cur} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    borned_highte = rose.height
    for i in range(1, 7):
        rose.age()
        rose.grow()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: + {rose.height - borned_highte}cm")
