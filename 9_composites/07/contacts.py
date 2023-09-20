"""
COMP.CS.100: Puhelinluettelo
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*

Creating a phonebook, training nested dictionaries
"""


def read_file(filename: str) -> dict:
    """Reads a CSV file for phonebook data and reaturns the data for queries.

    :param filename: str, CSV filename
    :return: dict, the phonebook data structure containing the CSV data
    """

    phonebook = {}

    try:
        data_file = open(filename, 'r')

        parent_keys = data_file.readline().rstrip().split(';')[1:]

        while True:

            line: str = data_file.readline().rstrip()
            if not line:
                break

            name, *info = line.split(';')

            if name not in phonebook:
                phonebook[name] = {}
            for i in range(len(info)):
                phonebook[name].update({parent_keys[i]:info[i]})

        data_file.close()

    except OSError as oserror:
        print('Virhe: ', oserror)

    return phonebook
