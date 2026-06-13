# Day 13 - File Handling + OOP
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"{self.owner} deposited {amount}. Balance: {self.balance}")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def save_to_file(self):
        filename = f"{self.owner}_transactions.txt"
        with open(filename, "w") as f:
            f.write(f"Owner: {self.owner}\nBalance: {self.balance}\n")
            f.write("Transactions:\n")
            for t in self.transactions:
                f.write(f"- {t}\n")
        print(f"Transactions saved to {filename}")


class SavingsAccount(Account):
    def withdraw(self, amount):
        if self.balance - amount >= 100:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"{self.owner} withdrew {amount}. Balance: {self.balance}")
        else:
            self.transactions.append("Failed withdrawal (minimum balance rule)")
            print(f"{self.owner} - Cannot withdraw, must keep minimum balance of 100")


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount} (overdraft allowed)")
            print(f"{self.owner} withdrew {amount}. Balance: {self.balance}")
        else:
            self.transactions.append("Failed withdrawal (overdraft exceeded)")
            print(f"{self.owner} - Overdraft limit exceeded!")


# --- Main Program ---
sneha_acc = SavingsAccount("Sneha", 150)
amit_acc = CurrentAccount("Amit", 200)

sneha_acc.deposit(100)
sneha_acc.withdraw(200)
sneha_acc.save_to_file()

amit_acc.deposit(100)
amit_acc.withdraw(200)
amit_acc.save_to_file()
