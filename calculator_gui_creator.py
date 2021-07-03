from tkinter import *
from tkinter.ttk import *

B_ROWS = 5
B_COLUMN = 4
KEYS = [['AC', '+/-', '%', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '.', '=', None]
        ]


class Calculator:
    """This class created the calculator window, display section and all the buttons"""

    def __init__(self, window):
        """this is the upper frame which contains the result and equation window"""
        self.equation = StringVar()
        self.result = DoubleVar()
        self.state = False  # If the "=" key is pressed

        frame_appearance = Style()
        frame_appearance.configure('TFrame', background='white')
        self.frame_display = Frame(window, borderwidth=8, relief=GROOVE, style="TFrame")
        self.frame_display.pack_propagate(0)
        self.frame_display.grid(row=0, column=0, sticky="EWNS")
        self.frame_display.columnconfigure(0, weight=1)

        # This is an equation label which will be updated every time a key is pressed.
        self.display_equation = Label(self.frame_display, background='white',
                                      textvariable=self.equation, font=('Helvetica', 12, 'bold', 'italic'))
        self.display_equation.grid(row=0, column=0, padx=10, pady=10, sticky="ENS")

        # This is a result label, which will show the result.
        self.result_label = Label(self.frame_display, background='white',
                                  textvariable=self.result, font=('Helvetica', 20, 'bold'))
        self.result_label.grid(row=1, column=0, padx=10, sticky="ENS")

        # This is the bottom frame contains all the keys.
        self.frame_buttons = Frame(window, borderwidth=8, relief=GROOVE)
        self.frame_buttons.pack_propagate(0)
        self.frame_buttons.grid(row=1, column=0, sticky="EWNS")
        self.button_appearance = Style()
        self.button_appearance.configure('TButton', font=('Helvetica', 18, 'bold'))

        # Creating individual frame for every button and add button
        # into that from and label it by getting the values from list - keys
        for i in range(B_ROWS):  # the number of rows of buttons
            self.frame_buttons.rowconfigure(i, weight=1)  # setting the weight of rows to 1

            for j in range(B_COLUMN):  # number of cols of buttons
                self.frame_buttons.columnconfigure(j, weight=1)  # setting the weight of cols to 1

                if KEYS[i][j] is not None:
                    self.frame_per_button = Frame(self.frame_buttons, height=50, width=100)
                    self.frame_per_button.pack_propagate(0)
                    self.frame_per_button.grid(row=i, column=j, sticky="EWNS")

                    self.buttons = Button(self.frame_per_button, text=KEYS[i][j],
                                          style='TButton', command=lambda x=KEYS[i][j]: self.append_num(x))
                    self.buttons.pack(fill=BOTH, expand=1)

                if i == 4 and j == 2:
                    # Merge last 2 columns and show equal sign it it.
                    self.frame_per_button.grid(columnspan=2)

    @staticmethod
    def check_float(potential_float):
        try:
            float(potential_float)
            return True
        except ValueError:
            return False

    def append_num(self, char):
        """this method will get the values from the buttons and show on the equation label,
           once "=" is pressed it will call the function to process the equation."""
        if self.equation.get() == "Error":
            self.equation.set(char)
        else:
            if char == '=':
                self.state = False
                if self.equation.get() == '':
                    pass
                else:
                    try:
                        result = eval(self.equation.get())
                    except Exception:
                        self.equation.set('Error')
                        self.result.set(0)
                    else:
                        self.result.set(result)

            elif char == 'AC':
                self.equation.set('')
                self.result.set(0)
            else:
                if not self.state:
                    self.state = True
                    if char.isdigit():
                        self.equation.set(char)
                    else:
                        self.equation.set(str(self.result.get()) + char)

                else:
                    self.equation.set(self.equation.get() + char)
