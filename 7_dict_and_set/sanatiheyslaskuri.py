"""
COMP.CS.100: Sanatiheyslaskuri
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Ohjelma kertoo sanojen esiintymistiheyden.
"""

def add_occurances(occurances: dict, sentence: str):
    """
    Adds the words in a given <sentence> to dict <occurances>, updating the
    times they appear.

    :param occurances: dict, contains the word occurances as word-times pairs
    :param sentence: str, to be split into words to be recorded
    :return: None
    """
    words = sentence.split()

    for word in words:
        word = word.lower()
        if word in occurances:
            occurances[word] += 1
        else:
            occurances.update({word:1})

def print_occurances(occurances: dict):
    """
    Outputs the word occurances.

    :param occurances: dict, contains the word occurances as word-times pairs
    :return: None
    """
    for item in sorted(occurances.items()):
        print(f'{item[0]} : {item[1]} times')

def main():

    occurances: dict = {}

    print('Enter rows of text for word counting. Empty row to quit.')
    while True:
        sentence = input()
        if not sentence:
            break

        add_occurances(occurances, sentence)

    print_occurances(occurances)


if __name__ == "__main__":
    main()
