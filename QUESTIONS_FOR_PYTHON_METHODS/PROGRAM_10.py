#10. Student — All Three Methods
class Student:
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(f"{self.name} Passed")
        else:
            print(f"{self.name} Failed")

    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks

    @staticmethod
    def grade_category(marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"

    def display(self):
        print(f"name = {self.name}")
        print(f"marks = {self.marks}")
        print(f"grade = {Student.grade_category(self.marks)}")
        self.result()

S1 = Student("Rajesh", 85)
S2 = Student("Ramesh", 65)
S3 = Student("Suresh", 35)

print("Before updating passing marks:")

S1.display()
S2.display()
S3.display()

Student.update_passing_marks(50)

print("\nAfter updating passing marks:")

S1.display()
S2.display()
S3.display()