# main_program.py
# Import Module
from bankutils import *


# Bank account test
account = BankAccount(-50)  # expected error message
account = BankAccount(300) # successful object creation
account.deposit(50) # successful deposit
account.deposit(-1) # negative deposit error
print(account)# Expected balance: $350
account.withdraw(500)  # Expected: "Insufficient balance"
account.withdraw(-1) # Negative withdraw amount
account.withdraw(100) # successful withdraw
print(account)  # Expected balance: $250
print(account.check_balance()) # testing check_balance function

# SavingsAccount Test Case
savings = SavingsAccount(300, -0.1) # Error: Negative interest rate
savings = SavingsAccount(200, 0.05) # 5% interest rate
savings.deposit(100) # Expected balance: $300
savings.deposit(-2) # Negative deposit
savings.withdraw(1000) # Insufficient funds
savings.withdraw(55) # Successful withdraw
savings.withdraw(-1) # Negative withdraw amount
print(savings) # Check values $245
savings.apply_interest() # Expected balance after interest: $257.25
savings.apply_interest() # Expected balance after interest: $270.11
print(savings) # Expected output: $270.11
print(savings.check_balance()) # testing check_balance function