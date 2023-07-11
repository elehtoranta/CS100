"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: ***REMOVED***
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Description:
    A simplified car assignment implementation using a class.
"""



class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = 0.0
        self.__odometer = 0.0

    def print_information(self):
        print(f"The tank contains {self.__gas:.1f} liters of gas "
              f"and the odometer shows {self.__odometer:.1f} kilometers.")

    def fill(self, liters):
        if liters < 0.0:
            raise ValueError("You cannot remove gas from the tank")
        elif self.__gas + liters > self.__tank_volume:
            self.__gas = self.__tank_volume
        else:
            self.__gas += liters

    def drive(self, distance):
        if distance < 0.0:
            raise ValueError("You cannot travel a negative distance")

        would_consume = (self.__consumption / 100) * distance
        consumed = would_consume if would_consume <= self.__gas else self.__gas
        driven = consumed * self.__consumption
        self.__odometer += driven
        self.__gas -= consumed


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    car = Car(tank_size, gas_consumption)

    while True:
        try:
            car.print_information()

            choice = input("1) Fill 2) Drive 3) Quit\n-> ")

            if choice == "1":
                to_fill = read_number("How many liters of gas to fill up?")
                car.fill(to_fill)

            elif choice == "2":
                distance = read_number("How many kilometers to drive?")
                car.drive(distance)

            elif choice == "3":
                print("Thank you and bye!")
                break

        except ValueError as error_message:
            print(error_message)


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
