# Import Module
from bankutils import *


# Bank account test
account = BankAccount(-50)  # expected error message
account = BankAccount(300)
account.deposit(50)
print(account)  # Expected balance: $150
account.withdraw(500)  # Expected: "Insufficient balance"
account.withdraw(100)
print(account)  # Expected balance: $50
