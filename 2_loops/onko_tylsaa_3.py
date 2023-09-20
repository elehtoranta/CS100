"""
COMP.CS.100: Onko tylsaa 3
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Asking if the user is bored but very, very weirdly.
"""


# Why is this an example of (good) usage of nested loops? The second while is so
# redundant that I have a hard time to understand how to do this.
def main():
    while input('Bored? (y/n) ').lower() != 'y':
        continue
    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()

# Below a clearer solution in my opinion.
# def main():
#     bored: str = ''
#     while bored != 'y':
#         bored = input('Bored? (y/n) ').lower()
#         if ('y' != bored) and ('n' != bored):
#             print('Incorrect entry.')
#     print("Well, let's stop this, then.")
