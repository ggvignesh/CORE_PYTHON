#2. Employee — Class Method
class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"name = {self.name}")
        print(f"company_name = {self.company_name}")

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

E1 = Employee("Rajesh")
E2 = Employee("Ramesh")
E3 = Employee("Suresh")

E1.display()
E2.display()
E3.display()

Employee.change_company("Infosys")
print("\nAfter changing company name:")

E1.display()
E2.display()
E3.display()