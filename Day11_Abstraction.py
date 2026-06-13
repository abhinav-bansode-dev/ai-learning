# Day 11 - Abstraction in Python
from abc import ABC, abstractmethod

# Abstract class
class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass  # Child classes must implement this

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")


# Child class: SavingsAccount
class SavingsAccount(Account):
    def withdraw(self, amount):
        if self.balance - amount >= 100:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"{self.owner} - Cannot withdraw, must keep minimum balance of 100")


# Child class: CurrentAccount
class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"{self.owner} - Overdraft limit exceeded!")


# --- Main Program ---
accounts = [
    SavingsAccount("Sneha", 150),
    CurrentAccount("Amit", 200)
]

for acc in accounts:
    acc.deposit(100)
    acc.withdraw(200)
