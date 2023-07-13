"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: ***REMOVED***
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Description:
    TODO
"""


LOW_STOCK_LIMIT = 30


class Product:
    """
    This class represent a product i.e. an item available for sale.
    """

    def __init__(self, code, name, category, price, stock):
        self.__code = code
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock

        # TODO (MAYBE): You might want to add more attributes here.

    def __str__(self):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests.
        """

        lines = [
            f"Code:     {self.__code}",
            f"Name:     {self.__name}",
            f"Category: {self.__category}",
            f"Price:    {self.__price:.2f}€",
            f"Stock:    {self.__stock} units",
        ]

        longest_line = len(max(lines, key=len))

        for i in range(len(lines)):
            lines[i] = f"| {lines[i]:{longest_line}} |"

        solid_line = "+" + "-" * (longest_line + 2) + "+"
        lines.insert(0, solid_line)
        lines.append(solid_line)

        return "\n".join(lines)

    def __eq__(self, other):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests since the read_database function will
        stop working correctly.
        """

        return self.__code == other.__code and \
               self.__name == other.__name and \
               self.__category == other.__category and \
               self.__price == other.__price

    # Comparisons for sorting by code
    def __lt__(self, other):
        """
        Less-than comparison.

        :return: True | False, True if the stock of <self> is
                 less than <other>'s, False otherwise.
        """

        return True if self.__code < other.__code else False

    def __gt__(self, other):
        """
        Greater-than comparison.

        :return: True | False, True if the stock of <self> is
                 greater than <other>'s, False otherwise.
        """

        return True if self.__code > other.__code else False

    def get_stock(self) -> int:
        """
        Get the current stock amount.

        :return: int, stock amount.
        """

        return self.__stock

    def modify_stock_size(self, amount):
        """
        YOU SHOULD NOT MODIFY THIS METHOD since read_database
        relies on its behavior and might stop working as a result.

        Allows the <amount> of items in stock to be modified.
        This is a very simple method: it does not check the
        value of <amount> which could possibly lead to
        a negative amount of items in stock. Caveat emptor.

        :param amount: int, how much to change the amount in stock.
                       Both positive and negative values are accepted:
                       positive value increases the stock and vice versa.
        """

        self.__stock += amount

    def print(self):
        """Prints the product information of <self>."""

        print(self)


def _read_lines_until(fd, last_line):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION since read_database
    relies on its behavior and might stop working as a result.

    Reads lines from <fd> until the <last_line> is found.
    Returns a list of all the lines before the <last_line>
    which is not included in the list. Return None if
    file ends bofore <last_line> is found.
    Skips empty lines and comments (i.e. characeter '#'
    and everything after it on a line).

    You don't need to understand this function works as it is
    only used as a helper function for the read_database function.

    :param fd: file, file descriptor the input is read from.
    :param last_line: str, reads lines until <last_line> is found.
    :return: list[str] | None
    """

    lines = []

    while True:
        line = fd.readline()

        if line == "":
            return None

        hashtag_position = line.find("#")
        if hashtag_position != -1:
            line = line[:hashtag_position]

        line = line.strip()

        if line == "":
            continue

        elif line == last_line:
            return lines

        else:
            lines.append(line)


def read_database(filename):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION as it is ready.

    This function reads an input file which must be in the format
    explained in the assignment. Returns a dict containing
    the product code as the key and the corresponding Product
    object as the payload. If an error happens, the return value will be None.

    You don't necessarily need to understand how this function
    works as long as you understand what the return value is.
    You can probably learn something new though, if you examine the
    implementation.

    :param filename: str, name of the file to be read.
    :return: dict[int, Product] | None
    """

    data = {}

    try:
        with open(filename, mode="r", encoding="utf-8") as fd:

            while True:
                lines = _read_lines_until(fd, "BEGIN PRODUCT")
                if lines is None:
                    return data

                lines = _read_lines_until(fd, "END PRODUCT")
                if lines is None:
                    print(f"Error: premature end of file while reading '{filename}'.")
                    return None

                # print(f"TEST: {lines=}")

                collected_product_info = {}

                for line in lines:
                    keyword, value = line.split(maxsplit=1)  # ValueError possible

                    # print(f"TEST: {keyword=} {value=}")

                    if keyword in ("CODE", "STOCK"):
                        value = int(value)  # ValueError possible

                    elif keyword in ("NAME", "CATEGORY"):
                        pass  # No conversion is required for string values.

                    elif keyword == "PRICE":
                        value = float(value)  # ValueError possible

                    else:
                        print(f"Error: an unknown data identifier '{keyword}'.")
                        return None

                    collected_product_info[keyword] = value

                if len(collected_product_info) < 5:
                    print(f"Error: a product block is missing one or more data lines.")
                    return None

                product_code = collected_product_info["CODE"]
                product_name = collected_product_info["NAME"]
                product_category = collected_product_info["CATEGORY"]
                product_price = collected_product_info["PRICE"]
                product_stock = collected_product_info["STOCK"]

                product = Product(code=product_code,
                                  name=product_name,
                                  category=product_category,
                                  price=product_price,
                                  stock=product_stock)

                # print(product)

                if product_code in data:
                    if product == data[product_code]:
                        data[product_code].modify_stock_size(product_stock)

                    else:
                        print(f"Error: product code '{product_code}' conflicting data.")
                        return None

                else:
                    data[product_code] = product

    except OSError:
        print(f"Error: opening the file '{filename}' failed.")
        return None

    except ValueError:
        print(f"Error: something wrong on line '{line}'.")
        return None


def example_function_for_example_purposes(warehouse, parameters):
    """
    This function is an example of how to deal with the extra
    text user entered on the command line after the actual
    command word.

    :param warehouse: dict[int, Product], dict of all known products.
    :param parameters: str, all the text that the user entered after the command word.
    """

    try:
        # Let's try splitting the <parameters> string into two parts.
        # Raises ValueError if there are more or less than exactly two
        # values (in this case there should be one int and one float) in
        # the <parameters> string.
        code, number = parameters.split()

        # First parameter was supposed to be a products code i.e. an integer
        # and the second should be a float. If either of these assumptions fail
        # ValueError will be raised.
        code = int(code)
        number = float(number)

    except ValueError:
        print(f"Error: bad parameters '{parameters}' for example command.")
        return

    # <code> should be an existing product code in the <warehouse>.
    if code not in warehouse:
        print(f"Error: unknown product code '{code}'.")
        return

    # All the errors were checked above, so everything should be
    # smooth sailing from this point onward. Of course, the other
    # commands might require more or less error/sanity checks, this
    # is just a simple example.

    print("Seems like everything is good.")
    print(f"Parameters are: {code=} and {number=}.")


def print_products(warehouse):
    """
    Prints out all products in a format specified by '__str__'.
    The products are sorted in ascending order by the product code (id).

    :param warehouse: dict[int, Product], products currently in stock.
    """

    for product in sorted(warehouse.values()):
        print(product)


def print_product_by_code(warehouse, code):
    """
    Prints out a product from <products> specified by identifier <code>, in
    a format specified in Product.

    :param warehouse: dict[int, Product], product entries.
    :param code: int, product code of the product to be printed.
    """

    try:
        code = int(code)
    except:
        print(f"Error: product '{code}' can not be printed as it does not exist.")
        return

    if not isinstance(code, int) or code not in warehouse:
        print(f"Error: product '{code}' can not be printed as it does not exist.")
    else:
        print(warehouse[code])


def delete_product_entry(warehouse, params):
    """
    Deletes a warehouse product entry, if a matching entry is found,
    and if there's no such products held at the warehouse.

    :param warehouse: dict[int, Product], product entries.
    :param code: int, product code of the entry to be deleted.
    """

    try:
        code = int(params)
    except ValueError:
        print(f"Error: product '{params}' can not be deleted as it does not exist.")
        return

    if code not in warehouse:
        print(f"Error: product '{code}' can not be deleted as it does not exist.")
    elif warehouse[code].get_stock() > 0:
        print(f"Error: product '207457' can not be deleted as stock remains.")
    else:
        del warehouse[code]


def change_stock(warehouse, params):
    """
    Changes the stock of a product entry specified by <code>.
    Performs input validation that 'modify_stock_size()' does not.

    :param warehouse: dict[int, Product], product entries.
    :param code: int, product code of the entry to be changed.
    """

    try:
        code, amount = params.strip().split()

        code = int(code)
        amount = int(amount)

    except ValueError:
        print(f"Error: bad parameters {params} for change command")
        return

    if code not in warehouse:
        print(f"Error: stock for '{code}' can not be changed as it does not exist.")
    else:
        warehouse[code].modify_stock_size(amount)

def display_low_stocks(warehouse):
    """
    Prints out the products that have less than LOW_STOCK_LIMIT (30)
    stock available.

    :param warehouse: dict[int, Product], product entries.
    """

    lows = dict(filter(lambda x:x[1].get_stock() < LOW_STOCK_LIMIT, warehouse.items()))
    print_products(lows)


def main():
    filename = input("Enter database name: ")
    # filename = "products.txt"

    warehouse = read_database(filename)
    if warehouse is None:
        return

    while True:
        command_line = input("Enter command: ").strip()

        if command_line == "":
            return

        command, *parameters = command_line.split(maxsplit=1)

        command = command.lower()

        if len(parameters) == 0:
            parameters = ""
        else:
            parameters = parameters[0]

        # If you have trouble undestanding what the values
        # in the variables <command> and <parameters> are,
        # remove the '#' comment character from the next line.
        # print(f"TEST: {command=} {parameters=}")

        if "example".startswith(command) and parameters != "":
            """
            'Example' is not an actual command in the program. It is
            implemented only to allow you to get ideas how to handle
            the contents of the variable <parameters>.

            Example command expects user to enter two values after the
            command name: an integer and a float:

                Enter command: example 123456 1.23

            In this case the variable <parameters> would refer to
            the value "123456 1.23". In other words, everything that
            was entered after the actual command name as a single string.
            """

            example_function_for_example_purposes(warehouse, parameters)

        elif "print".startswith(command) and parameters == "":
            print_products(warehouse)

        elif "print".startswith(command) and parameters != "":
            print_product_by_code(warehouse, parameters)

        elif "delete".startswith(command) and parameters != "":
            delete_product_entry(warehouse, parameters)

        elif "change".startswith(command) and parameters != "":
            change_stock(warehouse, parameters)

        elif "low".startswith(command) and parameters == "":
            display_low_stocks(warehouse)

        elif "combine".startswith(command) and parameters != "":
            # TODO: Implement combine command which allows
            #       the combining of two products into one.
            ...

        elif "sale".startswith(command) and parameters != "":
            # TODO: Implement sale command which allows the user to set
            #       a sale price for all the products in a specific category.
            ...

        else:
            print(f"Error: bad command line '{command_line}'.")


if __name__ == "__main__":
    main()
