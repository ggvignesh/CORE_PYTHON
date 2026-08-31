#7. Employee — Instance + Class + Static Methods
class Employee:
    bonus_rate = 0.1

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def final_salary(self):
        return self.base_salary + (self.base_salary * Employee.bonus_rate)

    @classmethod
    def update_bonus(cls, new_rate):
        cls.bonus_rate = new_rate

    @staticmethod
    def is_valid_salary(sal):
        if sal > 0:
            return True
        else:
            return False

    def display(self):
        print(f"name = {self.name}")
        print(f"base_salary = {self.base_salary}")
        print(f"final_salary = {self.final_salary()}")

E1 = Employee("Rajesh", 50000)
E2 = Employee("Ramesh", 60000)

if Employee.is_valid_salary(E1.base_salary):
    E1.display()

if Employee.is_valid_salary(E2.base_salary):
    E2.display()

Employee.update_bonus(0.2)

print("\nAfter updating bonus rate:")

E1.display()
E2.display()