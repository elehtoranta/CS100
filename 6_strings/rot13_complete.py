"""
COMP.CS.100 Ohjelmointi 1
Tekija: Erkka Lehtoranta (***REMOVED***)
Kuvaus: ROT13-salausohjelma (complete)
"""

def row_encryption(text: str) -> str:
    """
    Encrypts a full string using ROT13 encryption.

    :param text: str, to be encrypted
    :return: str, encrypted string
    """

    encrypted_string: str = ""

    for char in text:
        encrypted_string += encrypt(char)

    return encrypted_string

def encrypt(text: str) -> str:
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if text.isupper():
        input_is_uppercase = True
    else:
        input_is_uppercase = False
    text = text.lower()

    for i in range(len(regular_chars)):
        if regular_chars[i] == text:
            text = encrypted_chars[i]
            break

    if input_is_uppercase:
        text = text.upper()

    return text

def read_message() -> str:
    """
    Reads input a row at a time, saving each to a list of strings,
    until an empty row (newline) is input.

    :return: list, containing every row of input.
    """

    msg: list = []
    while True:
        row = str(input())
        if not row:
            break
        msg.append(row)

    return msg


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for row in msg:
        print(row_encryption(row))

if __name__ == "__main__":
    main()

