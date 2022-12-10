"""
COMP.CS.100: Points
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***

Calculating and displaying total score for contestants saved in a file.
"""


def main():
    contestants: dict = {}

    try:
        score_file = open(input('Enter the name of the score file: '))
    except:
        print('There was an error in reading the file.')
        return

    while True:
        line = score_file.readline()

        # Stop at EOF (readline() returns empty string at EOF)
        if not line:
            break

        # Skip empty lines
        if line == '\n':
            continue

        try:
            name, score = line.split()
        except:
            print(f'There was an erroneous line in the file:\n{line.rstrip()}')
            return

        try:
            score = int(score)
        except:
            print(f'There was an erroneous score in the file:\n{score}')
            return

        if name not in contestants:
            contestants.update({name:score})
        else:
            contestants[name] += score

    print(f'Contestant score:')
    for name, score in sorted(contestants.items()):
        print(f'{name} {score}')


if __name__ == "__main__":
    main()
