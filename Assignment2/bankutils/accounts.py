# accounts.py

class BankAccount:
    # initialize and test for valid parameter
    def __init__(self, initial_balance=0):
        self.balance = 0
        try:
            x = testpos(initial_balance)
            if x:
                self.balance = initial_balance
        except ValueError:
            print("Balance can't be negative")
        finally:
            print("Have a nice day")

    # deposit if amount is positive
    def deposit(self, amount=0.00):
        try:
            x = testpos(amount)
            if x:
                self.balance += amount
        except ValueError:
            print("Deposit can't be negative")

    # withdraw if amount is positive and less than or equal to balance
    def withdraw(self, amount):
        try:
            x = testsufficient(amount, self.balance)
            y = testpos(amount)
            if x and y:
                self.balance -= amount
        except ValueError:
            print("Insufficient Funds / Negative Amount")

    # simple function
    def check_balance(self):
        return self.balance

    # defines how object is converted to string
    def __str__(self):
        return f"This bank account has {self.balance} dollars in it"


class SavingsAccount:
    # initialize and check for valid parameters
    def __init__(self, initial_balance=0, interest_rate=0.02):
        self.balance = 0
        try:
            x = testpos(initial_balance)
            if x:
                self.balance = initial_balance
        except ValueError:
            print("Balance can't be negative")

        self.interest = 0
        try:
            x = testpos(interest_rate)
            if x:
                self.interest = interest_rate
        except ValueError:
            print("Interest Rate can't be negative")

    # deposit if amount is positive
    def deposit(self, amount):
        try:
            x = testpos(amount)
            if x:
                self.balance += amount
        except ValueError:
            print("Deposit can't be negative")

    # withdraw if amount is positive and less than or equal to balance
    def withdraw(self, amount):
        try:
            x = testsufficient(amount, self.balance)
            y = testpos(amount)
            if x and y:
                self.balance -= amount
        except ValueError:
            print("Insufficient Funds / Negative Amount")

    # update balance to reflect interest
    def apply_interest(self):
        self.balance *= 1 + self.interest

    # defines how object is converted to string
    def __str__(self):
        return f"This is a savings account with {self.balance} dollars and an interest rate of {self.interest}"

    # simple function
    def check_balance(self):
        return self.balance

# used in both classes to raise error if value is negative and return true otherwise
def testpos(amount):
    if amount < 0:
        raise ValueError()
    else:
        return(True)

# used for withdraws to see if the amount is less than the balance
def testsufficient(amount, balance):
    if amount > balance:
        raise ValueError()
    else:
        return(True)