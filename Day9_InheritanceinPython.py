# Day 9 - Inheritance in Python

# Parent class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            self.transactions.append("Failed withdrawal attempt")
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")


# Child class (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        # Call parent constructor
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    # New method specific to SavingsAccount
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added: {interest}")
        print(f"Interest of {interest} added. New balance: {self.balance}")


# --- Main Program ---
account1 = SavingsAccount("Ravi", 1000, 0.10)

account1.deposit(500)
account1.add_interest()
account1.withdraw(300)
account1.check_balance()

print("Transaction history:", account1.transactions)
