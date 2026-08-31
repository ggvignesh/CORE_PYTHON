#2. deposit(amount) to display the updated balance
class Bank:
    Bank_Name = "Axis"
    def __init__(self, name, acc_no, pin):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = 0
    @classmethod
    def change_bank(cls,new):
        cls.Bank_Name = new

    def display(self):
        print(f"name: {self.name}")
        print(f"acc_no: {self.acc_no}")
        print(f"balance: {self.balance}")

    def deposit(self, amount, pin):
        if pin == self.pin:
            if amount > 0:
                self.balance += amount
                print("Deposit successful")
            else:
                print("Amount must be greater than 0")
        else:
            print("Wrong PIN")

b1 = Bank(name="Rajesh", acc_no=123456, pin=1234)
b1.display()
b1.deposit(100000, 1234)
b1.display()