#1. Student — Class Variable + Instance Method + Class Method + Static Method
class Student:
    total_students = 0
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students = Student.total_students + 1

    def result(self):
        if self.marks >= Student.passing_marks:
            return "Passed"
        else:
            return "Failed"

    @classmethod
    def curve_marks(cls, percentage):
        # This method increases marks of all existing objects
        cls.curve_percentage = percentage

    @staticmethod
    def grade(marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "D"

S1 = Student("Rajesh", 75)
S2 = Student("Ramesh", 55)
S3 = Student("Suresh", 35)

print("Total students =", Student.total_students)

Student.curve_marks(10)

S1.marks = S1.marks + (S1.marks * Student.curve_percentage / 100)
S2.marks = S2.marks + (S2.marks * Student.curve_percentage / 100)
S3.marks = S3.marks + (S3.marks * Student.curve_percentage / 100)

print("\nUpdated Results:")

print(S1.name, S1.marks, Student.grade(S1.marks), S1.result())
print(S2.name, S2.marks, Student.grade(S2.marks), S2.result())
print(S3.name, S3.marks, Student.grade(S3.marks), S3.result())