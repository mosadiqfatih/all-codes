import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Username entry
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password entry
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login button
        self.login_button = tk.Button(root, text="Login", command=self.check_credentials)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace with actual credentials validation logic
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main tkinter window
root = tk.Tk()

# Create an instance of LoginApp
app = LoginApp(root)

# Run the tkinter main loop
root.mainloop()
