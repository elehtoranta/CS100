"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: *SECRET*
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Description:
    This program models a character adventuring in a video game.
"""


class Character:
    """This class defines what a character is in the game and what he or she can do."""

    def __init__(self, name, hp) -> None:
        """
        Constructor.

        :param name: Character name.
        """

        if not isinstance(name, str):
            raise ValueError(f"{name} is not a valid value for a name")

        self.__name         = name
        self.__hitpoints    = hp
        self.__inventory    = {}


    def __str__(self) -> str:
        """Returns a formatted string representation of the character."""

        return ((f"Name: {self.__name}\nHitpoints: {self.__hitpoints}\n  " + "\n  "
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

    def get_hp(self) -> int:
        """Gets the hitpoints of the character."""

        return self.__hitpoints


    def has_item(self, item) -> bool:
        """Checks if the character has a specified <item>"""

        return True if item in self.__inventory else False


    def how_many(self, item) -> int:
        """Returns the amount of given <item> in the inventory."""

        return self.__inventory[item] if item in self.__inventory else 0


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


    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        if self.has_item(item):
            self.remove_item(item)
            target.give_item(item)
            return True
        else:
            return False


    def receive_damage(self, damage):
        """Damages the hitpoints of <self> with <damage> amount."""
        self.__hitpoints -= damage


    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        # Didn't feel like long try/excepts, didn't feel like repeating return False
        error = ""
        if weapon not in WEAPONS:
            error = f'Attack fails: unknown weapon "{weapon}".'
        elif not self.has_item(weapon):
            error = f'Attack fails: {self.__name} doesn\'t have "{weapon}".'
        elif self is target:
            error = f'Attack fails: {self.__name} can\'t attack him/herself.'
        if error:
            print(error)
            return False

        damage = WEAPONS[weapon]
        print(f'{self.__name} attacks {target.get_name()} delivering {damage} damage.')
        target.receive_damage(damage)

        if target.get_hp() < DEAD:
            print(f'{self.__name} successfully defeats {target.get_name()}.')

DEAD = 0

WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
