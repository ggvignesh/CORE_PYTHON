#5. change_bank(new_bank) to update the bank name
class Bank1:
    bank_name = "SBI"
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    def display(self):
        print(f"name = {self.name}")
        print(f"acc_no = {self.acc_no}")
        print(f"balance = {self.balance}")
    @classmethod
    def change_bank(cls,new_bank):
        cls.bank_name = new_bank
B1 = Bank1("PNB",1014,10000)
B2 = Bank1("AXIS",1021,20000)
B3 = Bank1("ICICI",1035,50000)
B1.display()
B1.change_bank(new_bank="CanaraBank")
print(B1.name)