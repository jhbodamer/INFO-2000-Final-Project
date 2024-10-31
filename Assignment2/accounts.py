
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount=0.00):
        if amount > 0:
            self.balance += amount
        else:
            raise Exception("Please select a positive number")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise Exception("Not enough funds, select a lower amount")

    def check_balance(self):
        return self.balance

    def __str__(self):
        return f"This bank account has {self.balance} dollars in it"


class SavingsAccount:
    def __init__(self, initial_balance=0, interest_rate=0.02):
        self.balance = initial_balance
        self.interest = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise Exception("Please select a positive number")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise Exception("Not enough funds, select a lower amount")

    def apply_interest(self):
        self.balance *= 1 + self.interest

    def __str__(self):
        return f"This is a checking account with {self.balance} dollars and an interest rate of {self.interest}"

