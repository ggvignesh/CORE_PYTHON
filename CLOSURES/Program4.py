#4. Write a function bank_account(balance).
# The outer function receives the initial balance.
# The inner function receives an amount to withdraw.
# Print the remaining balance.
# Return the inner function.
def bank_account(balance):
    def withdraw(amount):
        print("Remaining Balance =", balance - amount)
    return withdraw

b = bank_account(50000)
b(12000)