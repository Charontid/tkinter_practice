import tkinter as tk

def main():
    app = App()
    app.mainloop()


class App(tk.Tk):
    OPTIONLIST = [
        "Choice 1",
        "Choice 2",
        "Choice 3",
        "Choice 4"
    ]

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("200x100")
        self.title("OptionMenu")

        self.variable = tk.StringVar(self)
        self.variable.set(self.OPTIONLIST[0])
        #tracking changes: 
        self.variable.trace("w", self.option_changed)

        self.option = tk.OptionMenu(
            self,
            self.variable,
            *self.OPTIONLIST
        )
        self.option.grid(row=0, column=0)

        self.label = tk.Label(
            self,
            text="Placeholder"
        )
        self.label.grid(row=0, column=1)


    def option_changed(self, *args):
        self.label.config(text=self.variable.get())

if __name__ == '__main__':
    main()
