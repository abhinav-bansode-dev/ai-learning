# Day 8 - OOP in Python

class BankAccount:
    # Constructor (special method to initialize object)
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    # Method to check balance
    def check_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")


# --- Main Program ---
# Create accounts
account1 = BankAccount("Ravi", 1000)
account2 = BankAccount("Sneha", 500)

# Perform operations
account1.deposit(200)
account1.withdraw(300)
account1.check_balance()

account2.deposit(1000)
account2.withdraw(2000)  # Will show insufficient funds
account2.check_balance()
