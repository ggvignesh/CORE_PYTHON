#1. Student — Instance Method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks > 40:
            return True
        else:
            return False

S1 = Student("Rajesh", 75)
S2 = Student("Ramesh", 35)

if S1.is_passed():
    print(S1.name, "Passed")
else:
    print(S1.name, "Failed")

if S2.is_passed():
    print(S2.name, "Passed")
else:
    print(S2.name, "Failed")