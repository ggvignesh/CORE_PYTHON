#10. Member — BMI + Class Limit + Static Validation
class Member:
    bmi_limit = 25

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight / (self.height * self.height)

    def fit_status(self):
        if self.calculate_bmi() <= Member.bmi_limit:
            return "Fit"
        else:
            return "Not Fit"

    @classmethod
    def update_bmi_limit(cls, new_limit):
        cls.bmi_limit = new_limit

    @staticmethod
    def valid_input(height, weight):
        if type(height) == int or type(height) == float:
            if type(weight) == int or type(weight) == float:
                if height > 0 and weight > 0:
                    return True
        return False

    def display(self):
        print(f"name = {self.name}")
        print(f"height = {self.height}")
        print(f"weight = {self.weight}")
        print(f"BMI = {self.calculate_bmi():.2f}")
        print(f"status = {self.fit_status()}")

M1 = Member("Rajesh", 1.75, 70)
M2 = Member("Ramesh", 1.70, 80)
M3 = Member("Suresh", 1.80, 90)

print("Member Details:")

M1.display()
M2.display()
M3.display()

print("\nInput Validation:")

print("1.75, 70 =", Member.valid_input(1.75, 70))
print("-1.75, 70 =", Member.valid_input(-1.75, 70))
print("1.75, -70 =", Member.valid_input(1.75, -70))

Member.update_bmi_limit(27)

print("\nAfter updating BMI standard:")

M1.display()
M2.display()
M3.display()