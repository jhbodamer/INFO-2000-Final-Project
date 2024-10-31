# accounts.py
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = 0
        try:
            x = testpos(initial_balance)
            if x:
                self.balance = initial_balance
        except ValueError:
            print("Balance can't be negative")

    def deposit(self, amount=0.00):
        try:
            x = testpos(amount)
            if x:
                self.balance += amount
        except ValueError:
            print("Deposit can't be negative")

    def withdraw(self, amount):
        try:
            x = testsufficient(amount, self.balance)
            if x:
                self.balance -= amount
        except ValueError:
            print("Insufficient Funds")

    def check_balance(self):
        return self.balance

    def __str__(self):
        return f"This bank account has {self.balance} dollars in it"


class SavingsAccount:
    def __init__(self, initial_balance=0, interest_rate=0.02):
        self.balance = initial_balance
        self.interest = interest_rate

    def deposit(self, amount):
        try:
            x = testpos(amount)
            if x:
                self.balance += amount
        except ValueError:
            print("Deposit can't be negative")

    def withdraw(self, amount):
        try:
            x = testsufficient(amount, self.balance)
            if x:
                self.balance -= amount
        except ValueError:
            print("Insufficient Funds")
            
    def apply_interest(self):
        self.balance *= 1 + self.interest

    def __str__(self):
        return f"This is a savings account with {self.balance} dollars and an interest rate of {self.interest}"


def testpos(amount):
    if amount < 0:
        raise ValueError()
    else:
        return(True)

def testsufficient(amount, balance):
    if amount > balance:
        raise ValueError()
    else:
        return(True)