"""
COMP.CS.100: Sanakirja matkalle 2
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Translating important words to Spanish.
"""

def print_contents(dictionary: dict):
    """Prints the current contents of the dictionary.

    :param dictionary: dict, contains the english-spanish word translations
    :return: None
    """

    print("Dictionary contents:")
    keys = sorted(dictionary.keys())
    print(*keys, sep=', ')

def main():
    """A translating program, from English, to Spanish."""
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    # Printing the current contents.
    print_contents(english_spanish)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f'{word} in Spanish is {english_spanish[word]}')
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            key = input("Give the word to be added in English: ")
            value = input("Give the word to be added in Spanish: ")
            if key and value:
                english_spanish.update({key: value})
            print_contents(english_spanish)

        elif command == "R":
            key = input("Give the word to be removed: ")
            if key in english_spanish:
                del english_spanish[key]
            else:
                print(f'The word {key} could not be found from the dictionary.')

        elif command == "P":
            values: list = sorted(english_spanish.items())
            for value in values:
                print(value[0], value[1])

        elif command == "T":
            sentence = input(f'Enter the text to be translated into Spanish: ')
            sentence_as_list: list = sentence.split()
            translated = ""

            for word in sentence_as_list:
                if word in english_spanish:
                    translated += english_spanish[word]
                else:
                    translated += word
                translated += " "

            print("The text, translated by the dictionary:")
            print(translated.rstrip())

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
