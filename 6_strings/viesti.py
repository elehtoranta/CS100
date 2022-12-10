"""
COMP.CS.100 Programming 1
Tekijä: Erkka Lehtoranta
Kuvaus: Tekstin tallentamista ja kapitalisaatiota.
"""


def read_message() -> list:
    """
    Reads a paragraph from the user and returns it as a list of strings.
    :return: list, list of strings received from the user.
    """
    result: list = []

    while True:
        input_string = str(input())
        if not input_string:
            break
        result.append(input_string)

    return result


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")

    msg: list = read_message()

    print("The same, shouting:")
    for sentence in msg:
        print(sentence.upper())


if __name__ == "__main__":
    main()
