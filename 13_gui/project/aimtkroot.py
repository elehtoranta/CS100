from tkinter import *
from tkinter.ttk import Combobox

from atkcanvas import ATKCanvas

class AimTKRoot:
    """The root class for the AimTK program."""

    def __init__(self):
        """Constructor."""

        self.__root = Tk()
        self.__root.title('AimTK - The Blazingly Bad Aim Trainer')
        self.__hits = IntVar(value=0)

        # These are not all implemented as controllable options:
        # I ran out of time (and competence). The controllable options
        # are target_*.
        self.__settings = {
                'gamecanvas_bg': StringVar(value='#dd9900'),
                'gamecanvas_w': IntVar(value=1200),
                'gamecanvas_h': IntVar(value=800),
                'target_color': StringVar(value='red'),
                'target_size': IntVar(value=60),
                }

        self.__gamecanvas = ATKCanvas(
                master=self.__root,
                aimtkroot=self,
                bg=self.__settings['gamecanvas_bg'].get(),
                width=max(200, self.__settings['gamecanvas_w'].get()),
                height=max(200, self.__settings['gamecanvas_h'].get()))

        ### Menu
        self.__root.option_add("*tearOff", FALSE)
        menu = Menu(self.__root)
        self.__root['menu'] = menu

        menu.add_command(label="Play", command=self.play)
        menu.add_command(label="Options", command=self.show_options)
        menu.add_separator()
        menu.add_command(label="Add target",
                         command=self.__gamecanvas.add_target)
        menu.add_command(label="Remove target",
                         command=self.__gamecanvas.remove_target)
        menu.add_command(label="Quit", command=self.__root.destroy)

        ### Heading
        heading = Label(self.__root, text="AimTK - The slowest aim trainer")
        heading.config(font=("", 24))
        heading.grid(row=0, sticky="ew")

        ### Hit counter
        counter = Label(textvariable=self.__hits,
                        font=("", 20))
        counter.grid(row=1)

        ### Game alignment
        self.__root.rowconfigure(2, weight=2)
        self.__root.columnconfigure(0, weight=2)
        self.__gamecanvas.grid(row=2, column=0)

    def start(self):
        """Execute GUI."""
        self.__root.mainloop()

    def play(self):
        """Start the game."""
        self.__gamecanvas.add_target()

    def get_settings(self):
        """Return settings dictionary."""
        return self.__settings

    def get_hits(self):
        """Return the current hit counter value."""
        return self.__hits.get()

    def set_hits(self, n):
        """Set the hit counter."""
        self.__hits.set(n)

    def add_hit(self):
        """Increment hit counter.

        Convenience function for interfacing with the class.
        """
        self.set_hits(self.get_hits() + 1)

    def show_options(self):
        """Show options window.

        A monster function that builds and displays the entire
        options window. This should be separated to a class component,
        but alas, time is my enemy and incompetence my downfall.
        """
        self.__options_window = Toplevel(self.__root)
        self.__options_window.title('AimTK - Options')
        self.__options_window.attributes('-topmost', True)

        # Spinbox option pickers, corresponding to all user modifiable
        # settings.

        # Target color control
        target_color_label = Label(self.__options_window,
                                   text="Target color")
        target_color_label.grid(row=0, sticky='ew')
        select_target_color = Combobox(
                self.__options_window,
                textvariable = self.__settings['target_color'])
        select_target_color['values'] = (
                'red', 'black', 'white', 'blue', 'gray')
        select_target_color.state(['readonly'])
        select_target_color.config(background='white')
        select_target_color.grid(row=1, sticky='ew')

        # Target size control
        target_size_label = Label(self.__options_window,
                                  text="Target size (range 10-80)")
        target_size_label.grid(row=2, sticky='ew')

        # NOTE+TODO: User can force values outside the supplied range,
        # as no validation is done. This produces an error currently.
        select_target_size = Spinbox(
                self.__options_window,
                textvariable=self.__settings['target_size'],
                from_=10,
                to=80,
                increment=10,
                bg='white')
        select_target_size.grid(row=3, sticky='ew')

        # Close settings
        close = Button(master=self.__options_window,
                       text="Close",
                       command=self.__options_window.destroy)
        close.grid(row=4, sticky='ew')
