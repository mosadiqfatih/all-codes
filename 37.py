import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")

        # List to store tasks
        self.tasks = []

        # Entry for task input
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Button to add task
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, height=15, width=50)
        self.task_listbox.pack(pady=10)

        # Button to remove task
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.pack()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main tkinter window
root = tk.Tk()

# Create an instance of ToDoApp
app = ToDoApp(root)

# Run the tkinter main loop
root.mainloop()
