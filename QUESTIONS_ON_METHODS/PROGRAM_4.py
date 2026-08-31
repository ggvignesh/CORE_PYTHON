#4. change_company(new_company) to change the company name
class Employee:
    company = "Infosys"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"emp_id = {self.emp_id}")
        print(f"name = {self.name}")
        print(f"company = {self.company}")
        print(f"salary = {self.salary}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

E1 = Employee(1, "Rajesh", 25000)
E2 = Employee(2, "Ramesh", 50000)
E3 = Employee(3, "Suresh", 75000)
E4 = Employee(4, "Naresh", 100000)
E2.display()
E2.change_company("Google")
E2.display()
E1.display()
E3.display()
E4.display()