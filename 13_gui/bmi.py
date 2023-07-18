"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__entry_frame = Frame(self.__mainwindow, width=300, height=500)
        self.__weight_labelframe = Frame(self.__entry_frame, width=300, height=250)
        self.__height_labelframe = Frame(self.__entry_frame, width=300, height=250)

        self.__weight_value_label = Label(self.__weight_labelframe,
                                          text="Enter your weight (kg):")
        self.__weight_value = Entry(self.__weight_labelframe, borderwidth=5)

        self.__height_value_label = Label(self.__height_labelframe,
                                          text="Enter your height (cm):")
        self.__height_value = Entry(self.__height_labelframe, borderwidth=5)

        self.__calculate_button = Button(self.__entry_frame,
                                         text="Calculate BMI",
                                         command=self.calculate_BMI,
                                         bg='green')

        self.__result_text = Label(self.__mainwindow, text="")
        self.__explanation_text = Label(self.__mainwindow, text="")

        self.__stop_button = Button(self.__mainwindow,
                                    text="Quit",
                                    command=self.stop)

        self.__entry_frame.grid(row=0, column=0) # Parent
        self.__weight_labelframe.grid(row=0, column=0)
        self.__height_labelframe.grid(row=0, column=1)

        self.__weight_value_label.grid(row=0, column=0, columnspan=2)
        self.__weight_value.grid(row=1, column=0, columnspan=2)

        self.__height_value_label.grid(row=0, column=3, columnspan=2)
        self.__height_value.grid(row=1, column=3, columnspan=2)

        self.__calculate_button.grid(row=2, column=0)

        self.__stop_button.grid(row=4, column=0, sticky="E", padx=10, pady=10)
        self.__result_text.grid(row=2, column=0)
        self.__explanation_text.grid(row=3, column=0, columnspan=3)

    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        try:
            (weight, height) = (float(self.__weight_value.get()),
                                float(self.__height_value.get()))
            print(f'weight {weight}, height {height}')
            bmi = weight / ((height / 100) ** 2)
            print(f"bmi {bmi}")

        except ValueError as e:
            print(e)
            self.__explanation_text['text'] = (
                    f"Error: height and weight must be numbers.")
            self.reset_fields()
            return

        if weight <= 0.0 or height <= 0.0:
            self.__explanation_text['text'] = (
                    f"Error: height and weight must be positive.")
            self.reset_fields()
            return

        self.reset_fields()

        if bmi < 18.5:
            desc = "You are underweight."
        elif bmi > 25.0:
            desc = "You are overweight."
        else:
            desc = "Your weight is normal."

        self.__result_text['text'] = f'{bmi:.2f}'
        self.__explanation_text['text'] = desc

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__result_text['text'] = ""
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
