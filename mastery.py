import tkinter as tk

class Mastery:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastery")

        # Configure the main grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create main frame to hold everything
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(sticky="nsew")

        # Configure the main frame grid layout
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_rowconfigure(2, weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Create frame for the grid
        self.grid_frame = tk.Frame(self.main_frame)
        self.grid_frame.grid(row=0, column=0, padx=200, pady=100, sticky="nsew")

        # Create frame for the buttons
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.grid(row=1, column=0, pady=(0, 10))

        # Create frame for the counter
        self.counter_frame = tk.Frame(self.main_frame)
        self.counter_frame.grid(row=2, column=0, pady=(0, 10))

        # Buttons to add symbols
        self.x_button = tk.Button(self.button_frame, text="X", fg="red")
        self.x_button.pack(side=tk.LEFT, padx=5)
        self.x_button.bind("<ButtonPress-1>", lambda event: self.start_adding_symbol("X"))
        self.x_button.bind("<ButtonRelease-1>", self.stop_adding_symbol)

        self.v_button = tk.Button(self.button_frame, text="V", fg="green")
        self.v_button.pack(side=tk.LEFT, padx=5)
        self.v_button.bind("<ButtonPress-1>", lambda event: self.start_adding_symbol("V"))
        self.v_button.bind("<ButtonRelease-1>", self.stop_adding_symbol)

        # Counter label
        self.v_counter_label = tk.Label(self.counter_frame, text="Win: 0", font=('Arial', 14))
        self.v_counter_label.pack()

        self.symbols = []
        self.grid_size = 10

        self.adding_symbol = False
        self.add_symbol_delay = 100  # milliseconds

        self.update_grid()

    def add_symbol(self, symbol):
        if len(self.symbols) >= 100:
            self.symbols = self.symbols[1:]
        self.symbols.append(symbol)
        self.update_grid()

    def update_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        for i, symbol in enumerate(self.symbols):
            color = "red" if symbol == "X" else "green"
            label = tk.Label(self.grid_frame, text=symbol, width=3, height=1, borderwidth=1, relief="solid", fg=color)
            row, col = divmod(i, self.grid_size)
            label.grid(row=row, column=col)

        # Update the counter for 'V' symbols
        v_count = self.symbols.count('V')
        self.v_counter_label.config(text=f"Win: {v_count}")

    def start_adding_symbol(self, symbol):
        self.adding_symbol = True
        self._add_symbol_repeatedly(symbol)

    def stop_adding_symbol(self, event):
        self.adding_symbol = False

    def _add_symbol_repeatedly(self, symbol):
        if self.adding_symbol:
            self.add_symbol(symbol)
            self.root.after(self.add_symbol_delay, self._add_symbol_repeatedly, symbol)

if __name__ == "__main__":
    root = tk.Tk()
    app = Mastery(root)
    root.mainloop()
