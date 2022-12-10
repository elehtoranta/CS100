"""
COMP.CS.100 Programming 1
ROT13 program code template
"""


def row_encryption(text: str) -> str:
    """
    Encrypts a string 'text' with ROT13 "encryption".
    :param text: the string to be encrypted.
    :return: str, encrypted string.
    """
    result: str = ""
    for i in range(len(text)):
        result += encrypt(text[i])

    return result


def encrypt(text: str) -> str:
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
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
