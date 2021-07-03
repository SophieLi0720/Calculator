from tkinter import *
from tkinter.ttk import *
from calculator_gui_creator import *


def main():
    """A calculator"""
    window = Tk()
    window.title("Calculator")
    window.geometry("300x400+600+200")
    window.minsize(300, 400)
    window.columnconfigure(0, weight=2)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=5)
    Calculator(window)

    window.mainloop()


main()
