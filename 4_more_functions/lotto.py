"""
COMP.CS.100: Lotto
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Calculating the chances of hitting the jackpot based on number of total and
drawn balls.
"""

def is_error(total: int, drawn: int) -> bool:
    """Check for errors in lotto inputs.

    :param total: int, total number of balls.
    :param drawn: int, number of drawn balls.

    :return: bool, True upon error, False otherwise.
    """
    if total < 0 or drawn < 0:
        print('The number of balls must be a positive number.')
        return True
    if drawn > total:
        print('At most the total number of balls can be drawn.')
        return True
    return False

def factorial(n: int) -> int:
    """Returns the factorial of integer n.

    :param n: int, base for factorial operation.
    :return: int, result of factorial operation.
    """
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

def combinatoric(total: int, drawn: int) -> int:
    """Gives the total number of ways the lottery balls
    can align given the total and drawn balls as parameters.

    :param total: int, total number of balls.
    :param drawn: int, drawn balls.
    :return: int, number of possible combinations of sets total and drawn.
    """
    return int(factorial(total) / (factorial(total - drawn) * factorial(drawn)))

def main():
    total: int = int(input('Enter the total number of lottery balls: '))
    drawn: int = int(input('Enter the number of the drawn balls: '))
    if is_error(total, drawn):
        return
    print(f'The probability of guessing all {drawn} balls correctly is '
          f'1/{combinatoric(total, drawn)}')

if __name__ == "__main__":
    main()
