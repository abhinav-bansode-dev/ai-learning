# Day 10 - Polymorphism in Python (Corrected with minimum balance error demo)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"{self.owner} - Insufficient funds!")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    # Polymorphic behavior: withdraw has different rules
    def withdraw(self, amount):
        if amount <= self.balance:
            # Must keep minimum balance of 100
            if self.balance - amount >= 100:
                self.balance -= amount
                print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
            else:
                print(f"{self.owner} - Cannot withdraw, must keep minimum balance of 100")
        else:
            print(f"{self.owner} - Insufficient funds!")


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    # Polymorphic behavior: withdraw allows overdraft
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"{self.owner} - Overdraft limit exceeded!")


# --- Main Program ---
accounts = [
    BankAccount("Ravi", 1000),
    SavingsAccount("Sneha", 150),   # 👈 adjusted balance so error will show
    CurrentAccount("Amit", 200)
]

for acc in accounts:
    acc.withdraw(100)  # Same method name, different behavior
