import tkinter as tk


def main():
    app = TestApp()
    app.mainloop()


class TestApp(tk.Tk):
    LANGUAGES = [
        "English",
        "Spanish",
        "French",
        "Chinese",
        "German"
    ]

    def __init__(self):
        super().__init__()
        self.title("RadioButton")
        self.geometry("200x200")

        tk.Label(
            self,
            text="Languages spoken: ",
        ).pack(anchor="w")

        self.languages = list()
        for cur_pos, language in enumerate(self.LANGUAGES):
            x = tk.IntVar()
            x.set(0)
            b = tk.Checkbutton(
                self,
                text=language,
                variable=x
            )
            b.pack(anchor="w")
            self.languages.append((x,b))
        tk.Button(
            self,
            text="submit",
            command=self.submit,
        ).pack(anchor="w")

        self.result = tk.Label(
            self,
            text="candidate speak:"
        )
        self.result.pack()

    def submit(self):
        speaks = list()
        for lang in self.languages:
            if lang[0].get() == 1:
                speaks.append(lang[1].cget("text"))
        self.result.config(text=f"candidate speaks: {' ,'.join(speaks)}")


if __name__ == '__main__':
    main()
