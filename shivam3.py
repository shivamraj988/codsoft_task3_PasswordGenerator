import tkinter as tk
from tkinter import ttk
import random
import string

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Attractive Login Page")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TLabel", background="#f0f0f0", foreground="black")
        self.style.configure("TButton", background="blue", foreground="white", padding=5)
        self.style.configure("TEntry", padding=5)

        self.root.geometry("300x330")

        self.title_label = ttk.Label(root, text="PASSWORD GENERATOR", font=("Helvetica", 14))
        self.title_label.pack(pady=10)

        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.username_label = ttk.Label(self.frame, text="Username:")
        self.username_label.grid(column=0, row=0, sticky=tk.W)

        self.username_entry = ttk.Entry(self.frame, width=30)  
        self.username_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

        self.password_label = ttk.Label(self.frame, text="Password:")
        self.password_label.grid(column=0, row=1, sticky=tk.W)

        self.password_entry = ttk.Entry(self.frame, show="*", width=30)  
        self.password_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        self.password_visibility = tk.BooleanVar()
        self.password_visibility.set(False)

        self.password_visibility_button = ttk.Checkbutton(self.frame, text="Show Password", variable=self.password_visibility, command=self.toggle_password_visibility)
        self.password_visibility_button.grid(column=1, row=2, sticky=tk.W)

        self.generate_password_button = ttk.Button(self.frame, text="Generate Password", command=self.generate_password, width=25)  
        self.generate_password_button.grid(column=0, row=3, columnspan=2, pady=10)

        self.accept_button = ttk.Button(self.frame, text="Accept", command=self.accept_login, width=25)  
        self.accept_button.grid(column=0, row=4, columnspan=2)

        self.reset_button = ttk.Button(self.frame, text="Reset", command=self.reset_fields, width=25) 
        self.reset_button.grid(column=0, row=5, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.grid(column=0, row=6, columnspan=2, pady=10)

    def toggle_password_visibility(self):
        if self.password_visibility.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(12)) 
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, generated_password)

    def accept_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.result_label.config(text=f"Logged in as: {username}\nPassword: {password}")

    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
