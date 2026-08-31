#8. Course — Class + Instance + Static Methods
class Course:
    total_students = 0

    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self):
        Course.total_students = Course.total_students + 1
        print(self.student_name, "enrolled successfully")

    @classmethod
    def show_total(cls):
        print(f"Total students = {cls.total_students}")

    @staticmethod
    def is_eligible(age):
        if age >= 18:
            return True
        else:
            return False

C1 = Course("Rajesh")
C2 = Course("Ramesh")
C3 = Course("Suresh")

if Course.is_eligible(21):
    C1.enroll()
else:
    print("Rajesh is not eligible")

if Course.is_eligible(19):
    C2.enroll()
else:
    print("Ramesh is not eligible")

if Course.is_eligible(16):
    C3.enroll()
else:
    print("Suresh is not eligible")

Course.show_total()