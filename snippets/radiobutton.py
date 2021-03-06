import tkinter as tk


def main():
    app = TestApp()
    app.mainloop()


class TestApp(tk.Tk):
    MODES = [
        ("Rock", "R"),
        ("Paper", "P"),
        ("Scissor", "S"),
    ]

    def __init__(self):
        super().__init__()
        self.title("RadioButton")
        self.geometry("200x200")

        """A group of RadioButtons share a common variable.
        Its possibile to select exactly one Choice out of the group of Buttons.
        """
        self.choice = tk.StringVar()
        self.choice.set(-1) # optional: those the default setting here
        for text, mode in self.MODES:
            b = tk.Radiobutton(
                self,
                indicatoron = 0,# turns the radiobutton into clickable rectangle
                width=20, padx = 5, pady=5,
                text=text,
                variable=self.choice,#variable, that stores the current selection of the Radiobutton - group
                value=text,#mode,#keyword for the variable, coud either use the same as text, or whatever is more useful
                command=self.ShowChoice #Optional command, that runs, once a Radiobutton is selected
            )
            b.pack(anchor="w")

        self.show = tk.Label(
            self,
            text=f"currently selected: -",
            width = 20, padx = 5, pady = 5,
            relief=tk.GROOVE
        )
        self.show.pack()

    def ShowChoice(self):
        """Updates the text of the show-Label, with the current value of the
        shared Radiobutton variable."""
        self.show.config(text=f"currently selected: {self.choice.get()}")


if __name__ == '__main__':
    main()
