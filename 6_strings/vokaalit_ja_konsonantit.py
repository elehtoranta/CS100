"""
COMP.CS.100: Vokaalit ja konsonantit
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Prints the number of vowels and consonants in a given word.
"""


def main():
    vowels = consonants = 0

    word = input("Enter a word: ")
    for char in word:
        if char in "aeiouy":
            vowels += 1
        else:
            consonants += 1

    print(f'The word "{word}" contains {vowels} vowels and {consonants}'
          f' consonants.')


if __name__ == "__main__":
    main()
