
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount=0.00):
        if amount > 0:
            self.balance += amount
        else:
            raise Exception("Please select a positive number")