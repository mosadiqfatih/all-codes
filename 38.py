import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry for displaying calculations
        self.entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 18))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Calculator buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create and place buttons
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=10, font=("Arial", 18),
                               command=lambda t=text: self.handle_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def handle_click(self, text):
        current = self.entry.get()
        if text == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, text)

# Create the main tkinter window
root = tk.Tk()

# Create an instance of CalculatorApp
app = CalculatorApp(root)

# Run the tkinter main loop
root.mainloop()
