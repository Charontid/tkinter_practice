import tkinter as tk
from itertools import chain
"""
special thanks to __blackjack__ for contiuous code reviews
"""

def main():
    game = Kniffel()
    game.mainloop()


class Kniffel(tk.Tk):
    DARK = "#093E62"
    #LIGHT = "#468DAE"
    #DARK2 = "#0F668E" # momentan nicht benutzt
    ENTRIES_BLOCK1 = {
        "1:": set(range(1, 6)),
        "2:": set(range(2, 11, 2)),
        "3:": set(range(3, 16, 3)),
        "4:": set(range(4, 21, 4)),
        "5:": set(range(5,26,5)),
        "6:": set(range(6,31,6))
    }
    ENTRIES_BLOCK2 = {
        "Full House:": {0, 25},
        "kleine Straße:": {0, 30},
        "große Straße:": {0, 40},
        "3er Pasch:": set(range(5,31)),
        "4er Pasch:": set(range(5,31)),
        "Chance:": set(range(5,31)),
        "Kniffel:": {0, 50}
    }
    LABELS = ["Summe:", "Bonus:", "Summe2:", "Total:"]

    NAMES = [
        "Name:",
        *ENTRIES_BLOCK1,
        "Bonus:",
        "Summe:",
        *ENTRIES_BLOCK2,
        "Summe2:",
        "Total:"
    ]

    def __init__(self):
        super().__init__()
        self.geometry("500x680")
        self.config(bg=self.DARK)
        self.title("Kniffel")

        # -- Spielerverwaltung --
        self.new_player = tk.Entry(
            self,
            relief=tk.RIDGE,
            width=len("neuer Spieler")
        )
        self.new_player.grid(row=0, column=0, padx=5, pady=5)
        self.new_player.insert(tk.END, 'neuer Spieler')
        tk.Button(
            self,
            command=self.add_player,
            relief=tk.RIDGE,
            text="hinzufügen"
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            self,
            command=self.remove_player,
            relief=tk.RIDGE,
            text="lösche Spieler",
        ).grid(row=0, column=2, padx=5, pady=5)

        # -- Tabelle --
        for i, name in enumerate(self.NAMES):
            tk.Label(
                self,
                bg=self.DARK,
                fg="white",
                relief = tk.GROOVE,
                text=name,
                width=11
            ).grid(column=0, row=i+1, sticky="e", padx=15, pady=5)

        self.players = list()

        # -- Punkteauswertung --
        tk.Button(
            self,
            text="Ergebnis",
            relief=tk.RIDGE,
            command=self.sum_up
        ).grid(row=20, column=0, padx=5, pady=5)

        tk.Button(
            self,
            command=self.reset_points,
            relief=tk.RIDGE,
            text="zurücksetzen"
        ).grid(row=20, column=1, padx=5, pady=5)

    def add_player(self):
        if self.new_player.get() in {"neuer Spieler", ""}:
            self.new_player.config(fg="red")
        else:
            name = self.new_player.get()
            player = {}
            player['Name:'] = tk.Label(
                self,
                bg=Kniffel.DARK,
                fg="white",
                relief=tk.GROOVE,
                text=name
            )

            length = len(name)
            for name in chain(self.ENTRIES_BLOCK1, self.ENTRIES_BLOCK2):
                player[name] = tk.Entry(
                    self,
                    bg=Kniffel.DARK,
                    fg="white",
                    width=max(8, length)
                )

            for name in self.LABELS:
                player[name] = tk.Label(
                    self,
                    bg=Kniffel.DARK,
                    fg ="white",
                    relief=tk.GROOVE,
                    text="-",
                    width=max(8, length)
                )

            column = len(self.players) + 1
            for row, key in enumerate(self.NAMES, 1):
                player[key].grid(column=column, row=row)
            self.players.append(player)

            self.new_player.config(fg="black")
        self.new_player.delete(0, tk.END)
        self.new_player.insert(0, "neuer Spieler")

    def remove_player(self):
        if self.players:
            player = self.players.pop()
            for widget in player:
                player.get(widget).destroy()

    def sum_up(self):
        for player in self.players:
            summe1 = sum(
                self.evaluate(player[key], numbers)
                for key, numbers in self.ENTRIES_BLOCK1.items()
            )
            bonus = 0 if summe1 < 63 else 25
            summe1 += bonus
            player["Bonus:"].config(text=bonus)
            player["Summe:"].config(text=summe1)

            summe2 = sum(
                self.evaluate(player[key], numbers)
                for key, numbers in self.ENTRIES_BLOCK2.items()
            )
            player["Summe2:"].config(text=summe2)
            player["Total:"].config(text=summe1+summe2)

    def evaluate(self, entry, numbers):
        value = entry.get()
        if value.isdigit() and int(value) in numbers:
            entry.config(bg=Kniffel.DARK)
            return int(value)
        else:
            entry.config(bg="red")
            return 0

    def reset_points(self):
        for player in self.players:
            for name in chain(self.ENTRIES_BLOCK1, self.ENTRIES_BLOCK2):
                player[name].delete(0, tk.END)
                player[name].config(bg=Kniffel.DARK)
            for name in self.LABELS:
                player[name].config(text="-")


if __name__ == '__main__':
    main()
