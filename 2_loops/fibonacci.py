"""
COMP.CS.100: Fibonacci
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Description: A program printing the Fibonacci sequence to a user specified end.
"""


def main():
    end: int = int(input('How many Fibonacci numbers do you want? '))
    first = 0
    second = fib = 1

    i = 1
    while i <= end:
        print(f'{i}. {fib}')
        fib = first + second
        first = second
        second = fib
        i += 1

if __name__ == "__main__":
    main()
