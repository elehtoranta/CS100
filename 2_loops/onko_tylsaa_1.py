"""
COMP.CS.100: Onko tylsää 1
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
A small function that loops while the caller is not bored.
"""

def main():
    while input("Bored? (y/n) ") == 'n':
        continue
    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()