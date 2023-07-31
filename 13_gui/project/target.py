from random import randrange

class Target:
    """Aim target class."""

    def __init__(self, aimtkroot, canvas):
        """Constructor."""

        self.__canvas = canvas
        self.__aimtkroot = aimtkroot
        self.__color = aimtkroot.get_settings()['target_color'].get()
        self.__size = aimtkroot.get_settings()['target_size'].get()
        self.__x = 0
        self.__y = 0

        self.set_random_position(self.__canvas.winfo_reqwidth(),
                                 self.__canvas.winfo_reqheight(),
                                 self.__size)

        # Canvas.create_* -functions return the <int> type id bound to the
        # object.
        self.__id = canvas.create_oval(self.__x,
                                       self.__y,
                                       self.__x + self.__size,
                                       self.__y + self.__size,
                                       fill=self.__color)

        # Bind mouse1 to register a target hit
        canvas.tag_bind(self.__id, '<1>', self.hit)

    def __str__(self) -> str:
        """Return a string representation of Target id.

        This is apparently required for some compitability reason, since the
        canvas binding pipeline assumes a string representation of the given
        id/tag.

        :return: str, target id in string format.
        """
        return f"{self.__id}"

    def get_id(self):
        """Return the Target id.

        :return: int, target id.
        """
        return self.__id

    def hit(self, event):
        """Move Target to a random position on the canvas.

        :param event: Event, TBH, I have no clue why this needs to be passed
                             in. Without <event> we receive error for too
                             many/few positional arguments.
        """

        # print(type(event)) # For your amusement =)

        # Reposition
        self.set_random_position(self.__canvas.winfo_reqwidth(),
                                 self.__canvas.winfo_reqheight(),
                                 self.__size)
        self.__canvas.moveto(self.__id, self.__x, self.__y)

        # Record a hit to the root statistics
        self.__aimtkroot.add_hit()

    def set_random_position(self, max_x, max_y, diameter):
        """Moves the Target to a random position on the visible canvas.

        The Target object <self> is set to be fully visible on the
        canvas (i.e. not clipping).

        :param max_x: int, the max x coordinate Target can be placed at.
        :param max_y: int, the max y coordinate Target can be placed at.
        :param diameter: int, the diameter of the (round) target.
        """

        try:
            self.__x = randrange(max_x - diameter)
            self.__y = randrange(max_y - diameter)

        except ValueError:
            print(f"Error: supplied target diameter ({diameter}) over maximum "
                  f"canvas dimensions ({max_x}:{max_y}).\nSet a valid value "
                  f"(i.e. value inside the valid range) in options.")
