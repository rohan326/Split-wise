import tkinter as tk
from tkinter import messagebox

class SplitwiseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Splitwise Lite")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.user_entries = []

        # Welcome label
        tk.Label(root, text="Splitwise Lite", font=("Helvetica", 16, "bold"), bg="#7d4caf", fg="white", pady=10).pack(fill=tk.X)

        # Number of users input
        tk.Label(root, text="Enter number of users:", bg="#1871a4", font=("Helvetica", 10)).pack(pady=(10, 0))
        self.num_users_entry = tk.Entry(root)
        self.num_users_entry.pack(pady=5)

        tk.Button(root, text="Submit", command=self.create_user_fields, bg="#543558", fg="white").pack(pady=5)

        # Frame for user entries
        self.user_frame = tk.Frame(root, bg="#1a6bc8")
        self.user_frame.pack(pady=10)

        # Total expense input
        tk.Label(root, text="Enter total expense:", bg="#45dd2e", font=("Helvetica", 10)).pack()
        self.total_expense_entry = tk.Entry(root)
        self.total_expense_entry.pack(pady=5)

        tk.Button(root, text="Calculate Split", command=self.calculate_split, bg="#2196f3", fg="white").pack(pady=10)

        # Result display
        self.result_text = tk.Text(root, height=10, width=40, bg="white", fg="black", font=("Courier", 10))
        self.result_text.pack(pady=10)

    def create_user_fields(self):
        # Clear previous entries
        for widget in self.user_frame.winfo_children():
            widget.destroy()
        self.user_entries.clear()

        try:
            num_users = int(self.num_users_entry.get())
            for i in range(num_users):
                tk.Label(self.user_frame, text=f"User {i+1} name:", bg="#0beb1e").pack()
                entry = tk.Entry(self.user_frame)
                entry.pack(pady=2)
                self.user_entries.append(entry)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of users")

    def calculate_split(self):
        try:
            total_expense = float(self.total_expense_entry.get())
            names = [entry.get() for entry in self.user_entries if entry.get().strip() != ""]
            if not names:
                raise ValueError("No names provided")

            split_amount = total_expense / len(names)
            self.result_text.delete(1.0, tk.END)
            for name in names:
                self.result_text.insert(tk.END, f"{name} owes ${split_amount:.2f}\n")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid total expense and user names")

if __name__ == "__main__":
    root = tk.Tk()
    app = SplitwiseApp(root)
    root.mainloop()
