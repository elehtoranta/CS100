"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: *SECRET*
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Description:
    This program models a character adventuring in a video game,
    or more like, the stuff that the character carries around.
"""


NOT_FOUND = 0


class Character:

    def __init__(self, name) -> None:
        """
        Constructor.

        :param name: Character name.
        """

        if not isinstance(name, str):
            raise ValueError(f"{name} is not a valid value for a name")

        self.__name         = name
        self.__inventory    = {}


    def __str__(self) -> str:
        """Returns a formatted string representation of the character."""

        return ((f"Name: {self.__name}\n  " + "\n  "
                 .join([f"{self.__inventory[item]} {item}"
                        for item in sorted(self.__inventory)
                        if self.how_many(item) > 0] ))
                if len(self.__inventory) > 0
                else f"Name: {self.__name}\n  --nothing--")


    def printout(self) -> None:
        """Prints a formatted representation of the character."""

        print(self)


    def get_name(self) -> str:
        """Gets the name of the character."""

        return self.__name


    def has_item(self, item) -> bool:
        """Checks if the character has a specified <item>"""

        return True if item in self.__inventory else False


    def how_many(self, item) -> int:
        """Returns the amount of given <item> in the inventory."""

        return self.__inventory[item] if item in self.__inventory else NOT_FOUND


    def give_item(self, item) -> None:
        """Adds a given <item> to the character inventory."""

        if not isinstance(item, str):
            raise ValueError("Item name must be a string")

        if self.has_item(item):
            self.__inventory[item] += 1
        else:
            self.__inventory[item] = 1


    def remove_item(self, item) -> None:
        """Removes an <item> from inventory."""

        if self.has_item(item):
            self.__inventory[item] -= 1

        if self.how_many(item) == 0:
            del self.__inventory[item]


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
