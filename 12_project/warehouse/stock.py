"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: ***REMOVED***
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Description:
    A warehouse stock management program.

    Reads a simple database file, which is turned into product entries
    to be displayed and manipulated by provided commands (see:
    Commands).

Usage:
    Reading the database: <filename>
        Read product information from <filename>.

        The file format consists of following input blocks
        delimited by blank lines:
            BEGIN PRODUCT
            CODE <id>
            NAME <name>
            CATEGORY <category>
            PRICE <price>
            STOCK <stock>
            END PRODUCT

    Commands: print | change | remove | low | combine | sale
        `print [<id>]`: With no arguments, displays all products in
            stock. With optional <id>, displays a product with that ID.

        `change <id> <quantity>`: Changes (adds or removes) stock of the
            product with ID <id>. Both arguments should be integers.

        `remove <id>`: Removes the database entry for product with ID
            <id>. An entry can only be removed if there's no current
            stock available.

        `low`: Display products that have stock less than
            LOW_STOCK_LIMIT (see below).

        `combine <stays> <leaves>:` Combine product with ID <leaves> to
            <stays>. This is useful especially when handling duplicate
            entries. The stock of <leaves> is added to (or if negative
            stock, substracted from) the stock of <stays>, after which
            <leaves> product entry is deleted.

        `sale <category> <sale>`: Places the items in <category> to a
            sale of <sale> percents. Note: A sale can be reverted by
            placing a category to a 'sale' of 0 percents.
"""


LOW_STOCK_LIMIT = 30
USAGE = """Usage: <command> [<args>]
Commands:
    print [<id>]
    change <id> <quantity>
    remove <id>
    low
    combine <id> <id>
    sale <category> <sale>
Argument format:
    id, quantity: int
    category: str
    sale: float
"""

class Product:
    """This class represents a product entry in a warehouse."""

    def __init__(self, code, name, category, price, stock):
        self.__code = code
        self.__name = name
        self.__category = category
        self.__price = price
        self.__original_price = price
        self.__stock = stock

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

    # Comparisons for sorting by product code
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

    def get_price(self) -> float:
        """
        Get the current price of <self>.

        :return: float, price.
        """

        return self.__price

    def get_category(self) -> str:
        """
        Get the category of the product <self>.

        :return: str, category of the product.
        """

        return self.__category

    def set_on_sale(self, sale):
        """Set the sale price according to a sale percentage."""
        self.__price = self.__original_price * ((100 - sale) / 100)

    def transfer_stock_to(self, other, amount):
        """Transfer <amount> of Product <self> to <other>."""
        transferable = amount if self.__stock >= amount else self.__stock

        other.modify_stock_size(transferable)
        self.modify_stock_size(-1 * transferable)

    def can_combine_with(self, other):
        """
        Return whether <other> can be combined with <self>.

        :param other: Product to check combination with.
        :return: True | None, True if can be combined, None if 
        """

        if self.__price != other.__price:
            print(f"Error: combining items with different prices "
                  f"{self.__price}€ and {other.__price}€.")
            return False
        elif self.__category != other.__category:
            print(f"Error: combining items of different categories "
                  f"'{self.__category}' and '{other.__category}'.")
            return False
        else:
            return True

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
                       positive value increases the stock and vice
                       versa.
        """

        self.__stock += amount

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
    object as the payload. If an error happens, the return value will
    be None.

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
    :param parameters: str, all the text that the user entered after
                       the command word.
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
    Print out all products in a format specified by '__str__'.
    The products are sorted in ascending order by the product code (id).

    :param warehouse: dict[int, Product], product entries.
    """

    for product in sorted(warehouse.values()):
        print(product)


def print_product_by_code(warehouse, args):
    """
    Print out product information about a Product in <warehouse>.
    Format specified in class <Product>.

    :param warehouse: dict[int, Product], product entries.
    :param args: str, argument string containing the code of the Product
                 to be printed.
    """

    E_NO_EXIST = (f"Error: product '{args}' can not be printed as it does not "
                "exist.")

    try:
        code = int(args)
    except ValueError:
        raise ValueError(E_NO_EXIST)

    if code not in warehouse:
        print(E_NO_EXIST)
        return
    else:
        print(warehouse[code])


def delete_product_entry(warehouse, args):
    """
    Delete a <warehouse> product entry, if:
        - a matching entry is found, and
        - there's no products at stock.

    :param warehouse: dict[int, Product], product entries.
    :param args: str, argument string containing the product code of the
                 entry to be deleted.
    """

    E_NO_EXIST = (f"Error: product '{args}' can not be deleted as it does not "
                  "exist.")

    try:
        code = int(args)
    except ValueError:
        raise ValueError(E_NO_EXIST)

    E_STOCK_REMAINS = (f"Error: product '{code}' can not be deleted as stock "
                       "remains.")

    if code not in warehouse:
        print(E_NO_EXIST)
        return
    elif warehouse[code].get_stock() > 0:
        print(E_STOCK_REMAINS)
        return
    else:
        del warehouse[code]


def change_stock(warehouse, args):
    """
    Changes the stock of a product entry specified by <args>.
    Performs input validation that 'modify_stock_size()' does not.

    :param warehouse: dict[int, Product], product entries.
    :param args: str, argument string containing the product code and
                 quantity to change.
    """

    E_BAD_PARAMS = f"Error: bad parameters '{args}' for change command."

    try:
        code, quantity = args.strip().split()

        code = int(code)
        quantity = int(quantity)

    except ValueError:
        raise ValueError(E_BAD_PARAMS)

    E_NO_EXIST = (f"Error: stock for '{code}' can not be changed as it does "
                  "not exist.")

    if code not in warehouse:
        print(E_NO_EXIST)
        return
    else:
        warehouse[code].modify_stock_size(quantity)


def display_low_stocks(warehouse):
    """
    Prints out the products that have less than LOW_STOCK_LIMIT (now 30)
    stock available.

    :param warehouse: dict[int, Product], product entries.
    """

    # For more readable lambda: we're filtering the values of the
    # key:value tuples the 'warehouse.items()' produces.
    PRODUCT = 1

    lows = dict(filter(lambda x:x[PRODUCT].get_stock() < LOW_STOCK_LIMIT,
                       warehouse.items()))
    print_products(lows)


def combine_products(warehouse, args):
    """
    Combines products with two separate product codes under the code
    of the first product, if their categories and prices match. The
    latter product is deleted from the product entries.

    :param warehouse: dict[int, Product], product entries.
    :param args: str, argument string of the two product codes.
    """

    E_BAD_PARAMS = f"Error: bad parameters '{args}' for combine command."

    try:
        stays, goes = args.strip().split()

        stays = int(stays)
        goes = int(goes)

    # All errors display the same error, E_BAD_PARAMS.
    except ValueError:
        raise ValueError(E_BAD_PARAMS)

    # Indentation, see https://peps.python.org/pep-0008/#indentation
    if (stays == goes
            or stays not in warehouse
            or goes not in warehouse):
        print(E_BAD_PARAMS)
        return

    if warehouse[stays].can_combine_with(warehouse[goes]):
        # Negative stock is considered valid here, so combining can
        # result in lowering the total stock.
        warehouse[goes].transfer_stock_to(warehouse[stays],
                                          warehouse[goes].get_stock())
        delete_product_entry(warehouse, goes)


def set_sale(warehouse, args):
    """
    Place all Products of <category> to <sale> percents.

    :param warehouse: dict[int, Product], product entries.
    :param args: str, argument string containing category and sale
                 percentage.
    """

    E_BAD_PARAMS = f"Error: bad parameters '{args}' for sale command."

    try:
        category, sale = args.strip().split()

        sale = float(sale)

    except ValueError:
        raise ValueError(E_BAD_PARAMS)

    set_items = 0
    for product in warehouse.values():
        if product.get_category() == category:
            product.set_on_sale(sale)
            set_items += 1

    print(f"Sale price set for {set_items} items.")


def main():
    filename = input("Enter database name: ")

    warehouse = read_database(filename)
    if warehouse is None:
        return

    while True:
        command_line = input("Enter command: ")

        if command_line == "":
            return

        try:
            command, *args = command_line.split(maxsplit=1)

            # Flatten to single argument string
            args = ''.join(args)

            if command == "usage" or command == "help":
                print(USAGE)

            elif command == "print" and not args:
                print_products(warehouse)

            elif command == "print" and args:
                print_product_by_code(warehouse, args)

            elif command == "delete" and args:
                delete_product_entry(warehouse, args)

            elif command == "change" and args:
                change_stock(warehouse, args)

            elif command == "low" and not args:
                display_low_stocks(warehouse)

            elif command == "combine" and args:
                combine_products(warehouse, args)

            elif command == "sale" and args:
                set_sale(warehouse, args)

            else:
                print(f"Error: bad command line '{command_line}'.")

        # Catches validation errors (re)-raised from command handlers. The
        # handlers raise ValueErrors in justifiable cases (mainly typecasts),
        # while errors related to restrictions set by the program etc. are
        # handled with traditional print/returns, as they can be considered a
        # part of normal control flow.
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
