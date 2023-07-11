
"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: ***REMOVED***
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Description:
    TODO
"""

WINNING_POINTS  = 50
PENALTY_POINTS  = 25

class Player():
    """
    Represents a player of a game of Mölkky.

    :param name: str, name of the player.
    """
    def __init__(self, name):
        """
        Constructor.

        :param name: str, name of the player.
        """
        self.__name = name
        self.__points = 0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def add_points(self, pts):
        if pts < 0:
            raise ValueError("Points must be 0 or more.")
        elif pts + self.__points > WINNING_POINTS:
            print(f"{self.__name} gets penalty points!")
            self.__points = PENALTY_POINTS
        else:
            self.__points += pts

        if self.__points in range(40, WINNING_POINTS):
            print(f"{self.__name} needs only {WINNING_POINTS - self.__points} points. "
                   "It's better to avoid knocking down the pins with higher points.")

    def has_won(self):
        return True if self.__points == WINNING_POINTS else False


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:
        try:

            # if throw is an even number
            if throw % 2 == 0:
                in_turn = player1

            # else throw is an odd number
            else:
                in_turn = player2

            pts = int(input("Enter the score of player " + in_turn.get_name() +
                            " of throw " + str(throw) + ": "))

            in_turn.add_points(pts)

            # TODO:
            # c) Add a supporting feedback printout "Cheers NAME!" here.

            if in_turn.has_won():
                print("Game over! The winner is " + in_turn.get_name() + "!")
                return

            print("")
            print("Scoreboard after throw " + str(throw) + ":")
            print(player1.get_name() + ":", player1.get_points(), "p")  # TODO: d)
            print(player2.get_name() + ":", player2.get_points(), "p")  # TODO: d)
            print("")

            throw += 1

        except ValueError as errmsg:
            print(errmsg)

        except TypeError as errmsg:
            print(errmsg)


if __name__ == "__main__":
    main()
