from tkinter import Tk, OptionMenu, StringVar


class OptionLenException(Exception):
    def __init__(self, sub_modes: tuple):
        self.length = len(sub_modes)
        self.message = f"sub mode length is {self.length}, should be 3"
        super().__init__(self.message)


class Mode(tuple):
    def __init__(self, program, sub_modes: tuple, default: Option):
        if len(sub_modes) != 3:
            raise OptionLenException(sub_modes)
        super().__init__(sub_modes)
        self.program = program
        self.default = default
        self.current = default

    def choose(self):
        window = Tk().wm_withdraw()
        var = StringVar(window)
        var.set(self.current)
        menu = OptionMenu(window, var, self[0], self[1], self[2])


class Draw(Mode):
    def __init__(self, program):
        super().__init__(program, [])

    def calculate(self):
        pass


class Option(str):
    def __init__(self, do, name: str):
        super().__init__(name)
        self.id = id(self)
        self.do = do
