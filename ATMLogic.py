import tkinter as tk
from tkinter import messagebox


# ATM Class (Handles ATM Logic)
class ATM:
    def __init__(self):
        self.balance = 5000   # Initial balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True


# GUI Controller Class
class ATMApp:
    def __init__(self, root):
        self.atm = ATM()
        self.root = root

        root.title("ATM Simulation")
        root.geometry("500x450")
        root.configure(bg="#191933")

        # Title
        self.title = tk.Label(
            root,
            text="🏧 ATM Simulation",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#191933"
        )
        self.title.pack(pady=20)

        # Input Box
        self.entry = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry.pack(pady=20)

        # Deposit Button
        self.deposit_btn = tk.Button(
            root,
            text="Deposit",
            bg="green",
            fg="white",
            width=15,
            font=("Arial", 12, "bold"),
            command=self.deposit_money
        )
        self.deposit_btn.pack(pady=10)

        # Withdraw Button
        self.withdraw_btn = tk.Button(
            root,
            text="Withdraw",
            bg="red",
            fg="white",
            width=15,
            font=("Arial", 12, "bold"),
            command=self.withdraw_money
        )
        self.withdraw_btn.pack(pady=10)

        # Check Balance Button
        self.balance_btn = tk.Button(
            root,
            text="Check Balance",
            bg="blue",
            fg="white",
            width=15,
            font=("Arial", 12, "bold"),
            command=self.show_balance
        )
        self.balance_btn.pack(pady=10)

        # Result Label
        self.result = tk.Label(
            root,
            text="Welcome!",
            font=("Arial", 16, "bold"),
            fg="cyan",
            bg="#191933"
        )
        self.result.pack(pady=30)

    def deposit_money(self):
        amount = self.entry.get()

        if amount == "":
            self.result.config(text="Enter amount!")
            return

        amount = int(amount)
        balance = self.atm.deposit(amount)
        self.result.config(text=f"Deposited: {amount}\nBalance: {balance}")

    def withdraw_money(self):
        amount = self.entry.get()

        if amount == "":
            self.result.config(text="Enter amount!")
            return

        amount = int(amount)

        success = self.atm.withdraw(amount)

        if success:
            self.result.config(
                text=f"Withdrawn: {amount}\nBalance: {self.atm.check_balance()}"
            )
        else:
            self.result.config(text="Insufficient Balance!")

    def show_balance(self):
        balance = self.atm.check_balance()
        self.result.config(text=f"Current Balance: {balance}")


# Run Program
root = tk.Tk()
app = ATMApp(root)
root.mainloop()