"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: ***REMOVED***
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi

Description:
    A counter program with a GUI.
"""

from tkinter import *


class Counter:
    def __init__(self):
        """A simple counter program GUI."""
        self.__mainframe = Tk()

        self.__counter = IntVar()
        self.__counter.set(0)

        self.__current_value_label = Label(self.__mainframe, textvariable=self.__counter, borderwidth=5, relief='raised', )
        self.__current_value_label.grid(row=0, column=0, columnspan=5, sticky=NSEW)

        self.__reset_button = Button(self.__mainframe, text="Reset", command=self.reset)
        self.__reset_button.grid(row=1, column=1, sticky=W)

        self.__increase_button = Button(self.__mainframe, text="Increase", command=self.increment)
        self.__increase_button.grid(row=1, column=2)

        self.__decrease_button = Button(self.__mainframe, text="Decrease", command=self.decrement)
        self.__decrease_button.grid(row=1, column=3)

        self.__quit_button = Button(self.__mainframe, text="Quit", command=self.quit)
        self.__quit_button.grid(row=1, column=4, sticky=E)

        self.__mainframe.mainloop()


    def reset(self):
        self.__counter.set(0)

    def increment(self):
        self.__counter.set(self.__counter.get() + 1)

    def decrement(self):
        self.__counter.set(self.__counter.get() - 1)

    def quit(self):
        self.__mainframe.destroy()


def main():

    Counter()


if __name__ == "__main__":
    main()
