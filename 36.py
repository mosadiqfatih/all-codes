import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.counter_value = 0
        
        # Create and pack the counter label
        self.label = tk.Label(root, text=f"Counter: {self.counter_value}", font=("Helvetica", 18))
        self.label.pack(pady=20)
        
        # Create and pack the increment button
        self.increment_button = tk.Button(root, text="Increment", command=self.increment_counter)
        self.increment_button.pack()

        # Create and pack the decrement button
        self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement_counter)
        self.decrement_button.pack()

    def increment_counter(self):
        self.counter_value += 1
        self.label.config(text=f"Counter: {self.counter_value}")

    def decrement_counter(self):
        self.counter_value -= 1
        self.label.config(text=f"Counter: {self.counter_value}")

# Create the main tkinter window
root = tk.Tk()
root.title("Counter App")
root.geometry('600x400')

# Create an instance of CounterApp
app = CounterApp(root)

# Run the tkinter main loop
root.mainloop()
