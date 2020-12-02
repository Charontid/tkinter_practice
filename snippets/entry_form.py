import tkinter as tk


def main():
    entryfields = [
        'This',
        'is',
        'a',
        'list',
        'of',
        'placeholders'
    ]
    app = App(entryfields)
    app.mainloop()


class App(tk.Tk):
    def __init__(self, entryfields):
        super().__init__()
        self.title("App")
        EntryForm(self, entryfields=entryfields).pack()


class EntryForm(tk.Frame):
    def __init__(self, master, entryfields):
        super().__init__(master)
        self.entryfields = entryfields
        self.entries = {
            entry : {
                'Label' : tk.Label(self, text=entry),
                'Entry' : tk.Entry(self)
            }
            for entry in entryfields
        }

        for _,entry in self.entries.items():
            entry.get('Label').pack(fill = tk.X)
            entry.get('Entry').pack(fill = tk.X)

        self.save = tk.Button(self, fg="GREEN", text="Save", command=self.save)
        self.save.pack(fill = tk.X)

    def save(self):
        cur = {key: self.entries.get(key).get('Entry').get()

            for key in self.entryfields
        }
        print(cur)


if __name__ == '__main__':
    main()
