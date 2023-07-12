
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
        self.__throws = []
        self.__points = 0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def get_hit_percentage(self):
        if not self.__throws:
            return 0.0

        return float(len(list(filter(lambda x:x > 0, self.__throws))) / len(self.__throws) * 100)

    def set_points(self, pts):
        if type(pts) is not int:
            raise ValueError("Points must be an integer value")
        else:
            self.__points = pts

    def add_points(self, pts):
        if pts < 0:
            raise ValueError("Points must be 0 or more.")

        self.__throws.append(pts)

        if pts + self.__points > WINNING_POINTS:
            print(f"{self.__name} gets penalty points!")
            self.set_points(PENALTY_POINTS)
        else:
            self.set_points(self.__points + pts) # TODO this check gives too many points if there's penalty points given

        if self.__points in range(40, WINNING_POINTS):
            print(f"{self.__name} needs only {WINNING_POINTS - self.get_points()} points. "
                   "It's better to avoid knocking down the pins with higher points.")


    def better_than_average(self):
        if self.__throws[-1] != PENALTY_POINTS and self.__points == PENALTY_POINTS:
            return False

        return True if self.__throws[-1] > self.__points / len(self.__throws) else False

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

            if in_turn.better_than_average():
                print(f"Cheers {in_turn.get_name()}!")

            if in_turn.has_won():
                print("Game over! The winner is " + in_turn.get_name() + "!")
                return

            print("")
            print("Scoreboard after throw " + str(throw) + ":")
            print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.get_hit_percentage():.1f}")
            print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.get_hit_percentage():.1f}")
            print("")

            throw += 1

        except ValueError as errmsg:
            print(errmsg)

        except TypeError as errmsg:
            print(errmsg)


if __name__ == "__main__":
    main()
