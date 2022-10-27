"""
COMP.CS.100: Rubikinkuutio
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Solving the Rubik's cube competition score by filtering list input.
"""

# Constant to denote the competition attempt total
ATTEMPTS = 5

def main():
    results: list = []
    # Fill the initial 5 results from query
    for i in range(ATTEMPTS):
        results.append(float(input(f'Enter the time for performance {i + 1}: ')))

    # Sort to align extreme cases as first and last elements
    results.sort()
    # Remove the extreme cases by slicing the ends off
    results = results[1:-1]
    average_result: float = sum(results) / len(results)
    print(f'The official competition score is {average_result:.2f} seconds.')


if __name__ == "__main__":
    main()
