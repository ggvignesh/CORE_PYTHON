#3. Employee — Promotion Criteria + Department Validation
class Employee:
    minimum_experience = 3

    def __init__(self, name, experience, department):
        self.name = name
        self.experience = experience
        self.department = department

    def promotion_eligibility(self):
        if self.experience >= Employee.minimum_experience:
            return "Eligible"
        else:
            return "Not Eligible"

    @classmethod
    def update_criteria(cls, new_experience):
        cls.minimum_experience = new_experience

    @staticmethod
    def valid_department(department):
        if department == "HR" or department == "Tech" or department == "Admin":
            return True
        else:
            return False

    def display(self):
        print(f"name = {self.name}")
        print(f"experience = {self.experience}")
        print(f"department = {self.department}")
        print(f"promotion = {self.promotion_eligibility()}")

E1 = Employee("Rajesh", 4, "Tech")
E2 = Employee("Ramesh", 2, "HR")
E3 = Employee("Suresh", 5, "Admin")

E1.display()
E2.display()
E3.display()

print("\nDepartment Validation:")

print("Tech =", Employee.valid_department("Tech"))
print("Finance =", Employee.valid_department("Finance"))

Employee.update_criteria(5)

print("\nAfter changing promotion criteria:")

E1.display()
E2.display()
E3.display()