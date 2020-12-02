import tkinter as tk


def main():
    app = App()
    app.mainloop()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("500x500")
        EntryForm(self).pack()


class EntryForm(tk.Frame):
    HEADER = [
        'KEY',
        'VALUE'
    ]


    def __init__(self, master):
        super().__init__(master)

        for i, label in enumerate(self.HEADER):
            tk.Label(self,text=label).grid(column=i, row=0)

        tk.Button(
            self,
            text="Add Field",
            command=self.add_field
        ).grid(column=0, row=1)

        tk.Button(
            self,
            text="Save",
            command=self.save
        ).grid(column=1, row=1)

        self.entries = [

        ]

    def add_field(self):
        row_pos = len(self.entries) +2
        id = tk.Entry(self)
        id.grid(column=0, row=row_pos)
        val = tk.Entry(self)
        val.grid(column=1, row=row_pos)
        self.entries.append({'ID':id, 'VAL':val})

    def save(self):
        data = dict()
        print(len(self.entries))
        for entry in self.entries:
            data[entry.get('ID').get()] = entry.get('VAL').get()

        print(data)



if __name__ == '__main__':
    main()
