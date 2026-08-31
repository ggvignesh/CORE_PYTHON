#9. BankAccount — All Three Methods
class BankAccount:
    bank_name = "SBI"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance = self.balance + amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid amount")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        else:
            return False

    def display(self):
        print(f"holder = {self.holder}")
        print(f"balance = {self.balance}")
        print(f"bank_name = {self.bank_name}")

B1 = BankAccount("Rajesh", 10000)
B2 = BankAccount("Ramesh", 20000)

B1.display()
B2.display()

print("\nTransactions:")

B1.deposit(5000)
B2.deposit(3000)

B1.display()
B2.display()

BankAccount.change_bank_name("HDFC Bank")

print("\nAfter changing bank name:")

B1.display()
B2.display()