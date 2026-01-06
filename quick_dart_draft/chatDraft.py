import tkinter as tk

class DartsApp:
    def __init__(self, root):
        self.root = root
        root.title("Darts Pistelasku")

        # Pelin tila
        self.multiplier = 1
        self.dart_count = 0
        self.turn_darts = 0
        self.turn_score = 0
        self.turns = []
        self.best_turn = 0

        # Ylätiedot
        self.info = tk.Label(root, text="", font=("Arial", 12))
        self.info.pack(pady=5)

        # Kertoimen valinta
        mult_frame = tk.Frame(root)
        mult_frame.pack()

        tk.Button(mult_frame, text="Single", width=8,
                  command=lambda: self.set_multiplier(1)).pack(side=tk.LEFT)
        tk.Button(mult_frame, text="Tupla", width=8,
                  command=lambda: self.set_multiplier(2)).pack(side=tk.LEFT)
        tk.Button(mult_frame, text="Tripla", width=8,
                  command=lambda: self.set_multiplier(3)).pack(side=tk.LEFT)

        # Numeropainikkeet
        num_frame = tk.Frame(root)
        num_frame.pack(pady=10)

        numbers = list(range(1, 21)) + [25, 50]
        for i, n in enumerate(numbers):
            tk.Button(
                num_frame,
                text=str(n),
                width=5,
                command=lambda x=n: self.throw(x)
            ).grid(row=i // 7, column=i % 7, padx=2, pady=2)

        self.update_info()

    def set_multiplier(self, m):
        self.multiplier = m

    def throw(self, value):
        score = value * self.multiplier
        self.dart_count += 1
        self.turn_darts += 1
        self.turn_score += score

        if self.turn_darts == 3:
            self.turns.append(self.turn_score)
            if self.turn_score > self.best_turn:
                self.best_turn = self.turn_score
            self.turn_darts = 0
            self.turn_score = 0

        self.update_info()

    def update_info(self):
        avg = sum(self.turns) / len(self.turns) if self.turns else 0
        text = (
            f"Heitetyt tikat: {self.dart_count}\n"
            f"Vuoroja: {len(self.turns)}\n"
            f"Keskiarvo / vuoro: {avg:.2f}\n"
            f"Paras vuoro: {self.best_turn}\n"
            f"Nykyinen vuoro: {self.turn_score} ({self.turn_darts}/3)\n"
            f"Valittu: {'Single' if self.multiplier==1 else 'Tupla' if self.multiplier==2 else 'Tripla'}"
        )
        self.info.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    app = DartsApp(root)
    root.mainloop()
