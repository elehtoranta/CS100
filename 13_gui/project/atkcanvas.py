from tkinter import Canvas, IntVar, Label, Frame
from target import Target

class ATKCanvas(Canvas):
    """Extended Canvas for displaying the aim game.

    ATKCanvas contains the <Target> objects and manages their
    addition/removal from the Canvas.

    Note: The targets are attached to the canvas in <Target> object
    initialization.
    """

    def __init__(self, aimtkroot, **kwargs):
        """Constructor.

        :param aimtkroot: AimTKRoot, root object of the GUI.
        """

        super().__init__(**kwargs)

        self.__targets = {}
        self.__aimtkroot = aimtkroot
        self['cursor'] = 'cross'

    def add_target(self):
        """Add an aim target on the canvas.

        Note: the <Target> gets bound to <self> in Target
        initialization, see Target class definition.
        """

        target = Target(aimtkroot=self.__aimtkroot, canvas=self)
        target_id = target.get_id()

        if target_id in self.__targets.keys():
            print(f"Error: Target with id {target_id} already in targets"
                  f"dictionary.")
            self.delete(target_id)

        self.__targets[target_id] = target

    def remove_target(self):
        """Remove an aim target from the canvas.

        Removes the most recently added Target object, both from the
        dictionary containing all Target references and from the Canvas
        containing a binding to the Target.
        """

        if not self.__targets:
            return

        # Last in, first out
        id = list(self.__targets)[-1]
        self.__targets.pop(id)
        self.delete(id)
