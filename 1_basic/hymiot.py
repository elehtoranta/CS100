"""
COMP.CS.100: Hymiot
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
"""

def main():
    mood: int = int(input('How do you feel? (1-10) '))
    if mood > 10 or mood < 1:  # Error check
        print('Bad input!')
        return
    print('A suitable smiley would be ', end='')
    if mood > 7:  # Good mood
        if mood == 10:  # Great
            print(':-D')
        else:  # OK
            print(':-)')
    elif mood < 4:  # Bad mood
        if mood == 1:  # Miserable
            print(":'(")
        else:  # Generalized depression
            print(':-(')
    else:  # Tonni's sedel
        print(':-|')

if __name__ == "__main__":
    main()