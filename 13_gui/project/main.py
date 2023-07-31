"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: ***REMOVED***
Name:       Erkka Lehtoranta
Email:      erkka.lehtoranta@tuni.fi
Exercise:   GUI project

Description:
    AimTK is a simple "aim trainer" program, where the user clicks on
    targets spawning on a screen as fast as they can, to potentially
    improve their mouse clicking accuracy.

Installation:
    Requires python3 with tkinter library installed.

    Most operating systems ship tkinter with tkinter installed, but
    some, like Ubuntu, may require installing tkinter separately. In
    case of Ubuntu, you can run `sudo apt install python3-tk`. On
    Windows, python3 should ship with tkinter library.

Usage:
    This usage information is based on running the program on Ubuntu.
    I simply and rudely assume that you know how to run the program on
    your platform.

    Starting the program (main.py):
        Command line: `cd ./aimtk && python3 main.py`

    Menu options:
        Play: Adds clickable targets.
        Options: Opens an options window, just for target controls in
                 this iteration.
        Add target: Same as 'Play', adds targets to click on.
        Remove target: Removes added targets.
        Quit: Quits the program.

    To start clicking your heart out, add targets to the window
    by clicking either 'Play' or 'Add target' (in the current version
    these options are equivalent).

    Clicking the targets increments the counter above the game view.
    For now, while not too entertaining, this is the only statistic
    available.
"""


from aimtkroot import AimTKRoot

def main():
    AimTKRoot().start()

if __name__ == "__main__":
    main()
