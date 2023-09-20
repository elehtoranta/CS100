"""
COMP.CS.100 Ohjelmointi 1
Tekija: Erkka Lehtoranta (*SECRET*)
Kuvaus: ROT13-salausohjelma
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
        uppercase = True
    else:
        uppercase = False
    text = text.lower()

    for i in range(len(regular_chars)):
        if text == regular_chars[i]:
            text = encrypted_chars[i]
            break

    if uppercase:
        text = text.upper()

    return text


def main():
    print(row_encryption(str(input('encrypt: '))))


if __name__ == "__main__":
    main()
