"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: ***REMOVED***
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Description:
    11.4: Fraction calculations
"""


NUMERATOR = 0
DENOMINATOR = 1


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator


    def __gt__(self, other):
        comp = self.deduct(other)
        return True if comp.get_numerator() * comp.get_denominator() > 0 else False


    def __lt__(self, other):
        comp = self.deduct(other)
        return True if comp.get_numerator() * comp.get_denominator() < 0 else False


    def __str__(self):
        return self.return_string()


    def get_numerator(self):
        """Getter for numerator."""
        return self.__numerator


    def get_denominator(self):
        """Getter for denominator."""
        return self.__denominator


    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


    def simplify(self):
        """Simplifies the fraction by dividing the sides with the greatest common divisor."""

        divisor = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator //= divisor
        self.__denominator //= divisor


    def complement(self):
        """Returns the complement of <self>."""
        return Fraction(-1 * self.__numerator, self.__denominator)


    def reciprocal(self):
        """Returns the reciprocal of <self>."""
        return Fraction(self.__denominator, self.__numerator)


    def multiply(self, other):
        """Returns the multiplication of two fractional numbers."""
        return Fraction(self.get_numerator() * other.get_numerator(),
                        self.get_denominator() * other.get_denominator())


    def divide(self, other):
        """Returns the division of two fractional numbers."""
        return self.multiply(other.reciprocal())


    def expand(self, other):
        """Returns a tuple containing two cross-expanded fractions."""
        return (Fraction(self.get_numerator() * other.get_denominator(),
                         self.get_denominator() * other.get_denominator()),
                Fraction(other.get_numerator() * self.get_denominator(),
                         other.get_denominator() * self.get_denominator()))


    def add(self, other):
        """Returns the sum of two fractional numbers."""
        self_expanded, other_expanded = self.expand(other)

        return Fraction(self_expanded.get_numerator() + other_expanded.get_numerator(),
                        self_expanded.get_denominator())


    def deduct(self, other):
        """Returns the deduction of two fractional numbers."""
        self_expanded, other_expanded = self.expand(other)

        return Fraction(self_expanded.get_numerator() - other_expanded.get_numerator(),
                        self_expanded.get_denominator())


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def add(fractions):
    """
    Reads and adds a Fraction object to a dictionary <fractions>.

    :param fractions: dict, contains Fraction objects as 'name:Fraction'.
    """

    f = input("Enter a fraction in the form integer/integer: ")

    if f == "":
        return

    f = f.strip().split('/')

    name = input("Enter a name: ")
    fractions[name] = Fraction(int(f[NUMERATOR]), int(f[DENOMINATOR]))


def print_frac(fractions):
    """Prints out a single fraction object."""

    name = input("Enter a name: ")

    if name not in fractions:
        print(f"Name {name} was not found")
    else:
        print(f"{name} = {fractions[name]}")


def list_frac(fractions):
    """Prints out a list of saved fractions."""

    for f in sorted(fractions):
        print(f"{f} = {fractions[f]}")


def multiply_frac(fractions):
    """Command to multiply 2 fractions."""

    first = input("1st operand: ")
    if first not in fractions:
        print(f"Name {first} was not found")
        return

    second = input("2nd operand: ")
    if second not in fractions:
        print(f"Name {second} was not found")
        return

    multiplied = fractions[first].multiply(fractions[second])

    print(f"{fractions[first]} * {fractions[second]} = {multiplied}")
    multiplied.simplify()
    print(f"simplified {multiplied}")


def read_fraction_file(fractions):
    """
    Reads a file of fractions with names into the <fractions> dict.

    :param fractions: dict, contains Fraction objects.
    """
    fname = input("Enter the name of the file: ")

    try:
        f = open(fname)

        for line in f:
            line = line.strip()

            name, values = line.split('=')
            operands = values.split('/')

            fractions[name] = Fraction(int(operands[NUMERATOR]), int(operands[DENOMINATOR]))

    except:
        print("Error: the file cannot be read.")
        return


def main():
    fractions = {}

    while True:
        try:
            command = input("> ")

            if "quit" == (command):
                print("Bye bye!")
                return

            elif "add" == (command):
                add(fractions)

            elif "print" == (command):
                print_frac(fractions)

            elif "list" == (command):
                list_frac(fractions)

            elif "*" == (command):
                multiply_frac(fractions)

            elif "file" == (command):
                read_fraction_file(fractions)

            else:
                print("Unknown command!")


        except IOError as emsg:
            print(emsg)


if __name__ == "__main__":
    main()
