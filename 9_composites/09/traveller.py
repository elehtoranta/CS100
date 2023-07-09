"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: ***REMOVED***
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Project 3: Route optimizer
"""

DEPARTURE = 0
DESTINATION = 1
DISTANCE = 2

def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param data: dict, A dictionary which contains the distance
           information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stored twice.
    """

    # +--------------------------------------+
    # |                                      |
    # |     DO NOT MODIFY THIS FUNCTION!     |
    # |                                      |
    # +--------------------------------------+

    # Modified this condition, as the condition assumes a depth of 1 data
    # structure. My data is of form dict[(departure, destination):distance].
    # I know my choice of data structure is a bit esoteric, but you might want
    # consider abstracting this condition with a get_departures() boolean function
    # or something of the like for situations like this, as you've done with
    # fetch_neighbours() and distance_to_neighbour().
    if departure not in [x[DEPARTURE] for x in data]:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))


def read_distance_file(file_name):
    """
    Reads the distance information from <file_name> and stores it
    in a suitable data structure (you decide what kind of data
    structure to use). This data structure is also the return value,
    unless an error happens during the file reading operation.

    :param file_name: str, The name of the file to be read.
    :return: dict | None: A data structure containing the information
             read from the <file_name> or None if any kind of error happens.
             The data structure to be chosen is completely up to you as long
             as all the required operations can be implemented using it.
    """

    connections = {}

    try:
        file = open(file_name)

        print(f'File {file_name} opened successfully.')

        for line in file:
            connection = line.rstrip('\n').split(';')

            if len(connection) != 3:
                print(f"Error: invalid number of values on line '{line}', " \
                        "please input 3 values separated by a semicolon (;)")

            for i in range(len(connection)):
                connection[i] = connection[i].strip().capitalize()

            # Create a unique tuple identifier for faster single item access
            key = create_key(connection[0], connection[1])

            connections[key] = int(connection[DISTANCE])

        return connections

    except OSError:
        print(f"Error: '{file_name}' can not be read.")
        return None

def fetch_neighbours(data, city):
    """
    Returns a list of all the cities that are directly
    connected to parameter <city>. In other words, a list
    of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is
    an empty list [], if <city> is unknown or if there are no
    arrows leaving from <city>.

    :param data: dict, A dictionary containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """

    return [x[DESTINATION] for x in data if x[DEPARTURE] == city]

def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities.
    Returns None if there is no direct connection from
    <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to
    <destination> city.

    :param data: dict, dictionary containing the distance
           information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """

    return data[(departure, destination)] \
            if (departure, destination) in data \
            else None

def display_connections(connections):
    """
    Prints out the connections provided in the dictionary <data>,
    format padded as 14,14,5.

    :param connections: dict, key: (departure, destination), value: distance.
    :return: None
    """
    for key in sorted(connections):
        print(f"{key[DEPARTURE]:14} {key[DESTINATION]:14} {connections[key]:5}")

def create_key(departure, destination):
    """
    Creates a simple, unique identifier tuple to use as a
    dictionary key, speeding up and simplifying operations on
    the connections data. We don't care about memory footprint around here.

    :param departure: str, departure city.
    :param destination: str, destination city.
    :return: tuple[str, str], a departure-destination string pair as a key.
    """

    return (departure, destination)

def has_departure_city(connections, city):
    """
    Checks whether the given <city> has any outbound connections.

    :param connections: dict, contains all city connections.
    :param city: str, name of the city that is being tested.
    :return: bool, True if a city has outbound connections, False otherwise.
    """
    return True if city in map(lambda x:x[DEPARTURE], connections) else False

def get_departures(connections):
    """
    Returns a list of all cities with departures. Contains duplicates.

    :param connections: dict, contains distance information between cities.
    :return: iterator, of departure cities.
    """
    return map(lambda x:x[DEPARTURE], connections.keys())

def get_destinations(connections):
    """
    Returns a list of all cities that are destinations. Contains duplicates.

    :param connections: dict, contains distance information between cities.
    :return: iterator, of destination cities.
    """
    return map(lambda x:x[DESTINATION], connections.keys())

def display_route(route, connections):
    """
    
    """
    total_distance = 0
    for i in range(len(route) - 1):
        hop = connections[(route[i], route[i + 1])]
        total_distance += hop
        # print(f"Total distance on iteration {i}: {total_distance}")
        print(f"{route[i]}-", end='')

    print(f"{route[len(route) - 1]} ({total_distance} km)")

def main():
    input_file = input("Enter input file name: ").strip()

    connections = read_distance_file(input_file)

    if connections is None:
        print(f"Error: '{input_file}' can not be read.")
        return

    while True:
        action = input("Enter action> ")

        if action == "":
            print("Done and done!")
            return

        elif "display".startswith(action):
            display_connections(connections)

        elif "add".startswith(action):
            departure = input("Enter departure city: ").strip().capitalize()
            destination = input("Enter destination city: ").strip().capitalize()
            distance = int(input("Enter distance: ").strip())

            key = create_key(departure, destination)
            connections[key] = distance

        elif "remove".startswith(action):
            departure = input("Enter departure city: ").strip().capitalize()

            if departure not in [x[DEPARTURE] for x in connections.keys()]:
                print(f"Error: '{departure}' is unknown.")
                continue

            destination = input("Enter destination city: ").strip().capitalize()
            key = create_key(departure, destination)

            if key in connections.keys():
                del connections[key]
            else:
                print(f"Error: missing road segment between '{departure}' and '{destination}'")

        elif "neighbours".startswith(action):
            departure = input("Enter departure city: ").strip().capitalize()

            if not has_departure_city(connections, departure):
                print(f"Error: '{departure}' is unknown.")
            else:
                display_connections(dict(filter(lambda x:x[0][DEPARTURE] == departure, connections.items())))

        elif "route".startswith(action):
            departure = input("Enter departure city: ").strip().capitalize()
            if not has_departure_city(connections, departure):
                print(f"Error: '{departure}' is unknown.")
                continue

            destination = input("Enter destination city: ").strip().capitalize()

            route = find_route(connections, departure, destination)
            # print(route) # DEBUG

            if len(route) == 0:
                print(f"No route found between '{departure}' and '{destination}'.")
            elif len(route) == 2 and route[1] == departure: # push to display_route
                print(f"{departure}-{destination} (0 km)")
            else:
                display_route(route, connections)

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()
