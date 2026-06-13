# Day 12 - Mini Project: Banking System with OOP pillars
from abc import ABC, abstractmethod

# --- Abstraction ---
class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []  # Encapsulation: each account keeps its own history

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"{self.owner} deposited {amount}. Balance: {self.balance}")

    @abstractmethod
    def withdraw(self, amount):
        pass  # Must be implemented by child classes

    def print_transactions(self):
        print(f"Transaction history for {self.owner}:")
        for t in self.transactions:
            print("-", t)


# --- Inheritance + Polymorphism ---
class SavingsAccount(Account):
    def withdraw(self, amount):
        if self.balance - amount >= 100:  # Minimum balance rule
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
        if amount <= self.balance + self.overdraft_limit:  # Overdraft allowed
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount} (overdraft allowed)")
            print(f"{self.owner} withdrew {amount}. Balance: {self.balance}")
        else:
            self.transactions.append("Failed withdrawal (overdraft exceeded)")
            print(f"{self.owner} - Overdraft limit exceeded!")


# --- Main Program ---
accounts = [
    SavingsAccount("Sneha", 150),
    CurrentAccount("Amit", 200),
]

for acc in accounts:
    acc.deposit(100)
    acc.withdraw(200)
    acc.print_transactions()
    print("-" * 40)
