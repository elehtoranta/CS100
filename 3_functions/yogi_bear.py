"""
COMP.CS.100: Yogi Bear
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Making the greatest sitsilaulu faster to sing virtually.
"""

def repeat_name(name, times):
    """Repeats the name of a certain bear n times.

    :param name: str, name of a bear.
    :param times: int, times the name is repeated.
    """
    for _ in range(times):
        print(f'{name}, {name} Bear')

def verse(sentence, name):
    """Compiles a verse of Yogi Bear.

    :param sentence: str, the main sentence of a verse.
    :param name: str, name of a bear appearing in the verse.
    """
    print(f'{sentence}')
    print(f'{name}, {name}')
    print(f'{sentence}')
    repeat_name(name, 3)
    print(f'{sentence}')
    repeat_name(name, 1)

def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
