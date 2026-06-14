# Day 14 - Exception Handling + OOP
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
            print(f"{self.owner} deposited {amount}. Balance: {self.balance}")
        except ValueError as e:
            print(f"Error: {e}")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def save_to_file(self):
        try:
            filename = f"{self.owner}_transactions.txt"
            with open(filename, "w") as f:
                f.write(f"Owner: {self.owner}\nBalance: {self.balance}\n")
                f.write("Transactions:\n")
                for t in self.transactions:
                    f.write(f"- {t}\n")
            print(f"Transactions saved to {filename}")
        except Exception as e:
            print(f"File error: {e}")


class SavingsAccount(Account):
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if self.balance - amount >= 100:
                self.balance -= amount
                self.transactions.append(f"Withdrew {amount}")
                print(f"{self.owner} withdrew {amount}. Balance: {self.balance}")
            else:
                raise ValueError("Minimum balance of 100 must be maintained")
        except ValueError as e:
            self.transactions.append(f"Failed withdrawal: {e}")
            print(f"Error: {e}")


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                self.transactions.append(f"Withdrew {amount} (overdraft allowed)")
                print(f"{self.owner} withdrew {amount}. Balance: {self.balance}")
            else:
                raise ValueError("Overdraft limit exceeded")
        except ValueError as e:
            self.transactions.append(f"Failed withdrawal: {e}")
            print(f"Error: {e}")


# --- Main Program ---
sneha_acc = SavingsAccount("Sneha", 150)
amit_acc = CurrentAccount("Amit", 200)

# Valid operations
sneha_acc.deposit(100)
sneha_acc.withdraw(200)
sneha_acc.save_to_file()

# Invalid operations to test exception handling
sneha_acc.deposit(-50)       # ❌ negative deposit
amit_acc.withdraw(-100)      # ❌ negative withdrawal
amit_acc.withdraw(1000)      # ❌ overdraft exceeded
amit_acc.save_to_file()
