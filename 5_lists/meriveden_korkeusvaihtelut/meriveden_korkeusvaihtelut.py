"""
COMP.CS.100: Meriveden korkeusvaihtelut
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Analyzing the development of sea level through some markers.
"""


def get_median(sea_levels: list) -> float:
    """
    Finds the median of a given list 'sea_levels'.
    :param sea_levels: list, of which the median is searched.
    :return: float, the median value of 'sea_levels'.
    """
    sea_levels.sort()
    # Get the reference point for the middle value of the sorted input list
    midpoint: int = len(sea_levels) // 2

    # For an UNEVEN number of elements, the middle point is the median value.
    # For EVEN number of elements, the median is the mean of the two
    # middle-most values of the list.
    if midpoint % 2 != 0:
        return sea_levels[midpoint]
    else:
        return (sea_levels[midpoint - 1] + sea_levels[midpoint]) / 2


def get_mean(sea_levels: list) -> float:
    """
    Calculates the mean value of given list (of floats), 'sea_levels'.
    :param sea_levels: list, values to average together
    :return: float, the mean value of a given list of floats 'sea_levels'
    """
    return sum(sea_levels) / len(sea_levels)


def get_variance(sea_levels: list, mean: float) -> float:
    """
    Calculates the variance of a given set of values.
    :param sea_levels: list, containing (sorted) sea level data as floats.
    :param mean: float, the mean value of the sea_levels list.
    :return: float, the variance of the sea level data.
    """
    adjusted: list = []

    for value in sea_levels:
        adjusted.append((value - mean) ** 2)
    return sum(adjusted) / (len(adjusted) - 1)


def get_deviation(variance: float) -> float:
    """
    Calculates the standard deviation for a given set of values.
    :param variance: float, precalculated variance of the set.
    :return: float, standard deviation of a given set.
    """
    return variance ** 0.5


def get_levels() -> list:
    """
    Reads and saves the user input of sea level data.
    :return: list, contains the raw sea level data.
    """
    sea_levels: list = []

    while True:
        value = input()
        if value:
            sea_levels.append(float(value))
        else:
            return sea_levels


def main():
    """
    A program to calculate data markers from a queried set of sea levels.
    Of a given data set, the sea level minimum, maximum, median, mean and
    standard deviation, respectively.
    Usage information is printed at the beginning of the program.
    NOTE: Erroneous input (i.e. non-numerical or overflowing) is not guarded
    in any way, and the former will cause the program to crash. I considered
    extensive error handling to be out of the scope of this project (and out
    of scope of my Python skills).
    :return: None
    """
    print("Enter seawater levels in centimeters one per line.\n"
          "End by entering an empty line.")
    sea_levels: list = get_levels()
    if len(sea_levels) < 2:
        print('Error: At least two measurements must be entered!')
        return

    mean = get_mean(sea_levels)
    median = get_median(sea_levels)
    variance = get_variance(sea_levels, mean)
    deviation = get_deviation(variance)

    print(f'Minimum:   {min(sea_levels):.2f} cm')
    print(f'Maximum:   {max(sea_levels):.2f} cm')
    print(f'Median:    {median:.2f} cm')
    print(f'Mean:      {mean:.2f} cm')
    print(f'Deviation: {deviation:.2f} cm')


if __name__ == "__main__":
    main()
