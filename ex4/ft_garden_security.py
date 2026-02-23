class SecurePlant:
    def __init__(self, name : str, height : int, age : int) -> None :
        self.name = name
        self.__height = height
        self.__age = age
    def set_age(self, new_age : int) -> None:
        if (new_age >= 0):
            self.__age = new_age
        else:
            print("Invalid operation attempted: age", new_age,"days [REJECTED]")
            print("Security: Negative age rejected")
    def set_height(self, new_height : int) -> None:
        if (new_height >= 0):
            self.__height = new_height
        else:
            print("Invalid operation attempted: height", new_height,"days [REJECTED]")
            print("Security: Negative height rejected")
    def get_height(self) -> int:
        return (self.__height)
    def get_age(self) -> int:
        return (self.__age)
if __name__ == "__main__":
    rose = SecurePlant("Rose",15,20)
    print(rose.name)
    rose.set_height(-0)
    print(rose.get_height())