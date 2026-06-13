# Day 8 Extended - OOP with Transaction History

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []  # list to store history

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

    def print_transactions(self):
        print(f"Transaction history for {self.owner}:")
        for t in self.transactions:
            print("-", t)


# --- Main Program ---
account1 = BankAccount("Ravi", 1000)

account1.deposit(200)
account1.withdraw(300)
account1.withdraw(2000)  # will fail
account1.check_balance()
account1.print_transactions()
