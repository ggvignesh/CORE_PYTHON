#4. Loan — Interest Rate + Eligibility
class Loan:
    interest_rate = 0.10

    def __init__(self, borrower, principal):
        self.borrower = borrower
        self.principal = principal

    def total_payable(self):
        return self.principal + (self.principal * Loan.interest_rate)

    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @staticmethod
    def check_eligibility(salary):
        if salary > 30000:
            return True
        else:
            return False

    def display(self):
        print(f"borrower = {self.borrower}")
        print(f"principal = {self.principal}")
        print(f"total_payable = {self.total_payable()}")

L1 = Loan("Rajesh", 100000)
L2 = Loan("Ramesh", 200000)

print("Loan Details:")

L1.display()
L2.display()

print("\nEligibility:")

print("Rajesh =", Loan.check_eligibility(50000))
print("Ramesh =", Loan.check_eligibility(25000))

Loan.update_interest_rate(0.15)

print("\nAfter updating interest rate:")

L1.display()
L2.display()