#5. Course — Total Courses + Enrollment + Minimum Duration
class Course:
    total_courses = 0
    minimum_duration = 1

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.enrolled_students = []
        Course.total_courses = Course.total_courses + 1

    def enroll(self, student_name):
        self.enrolled_students.append(student_name)
        print(student_name, "enrolled in", self.title)

    @classmethod
    def update_minimum_duration(cls, new_duration):
        cls.minimum_duration = new_duration

    @staticmethod
    def valid_duration(duration):
        if duration >= 0 and duration <= 60:
            return True
        else:
            return False

    def display(self):
        print(f"title = {self.title}")
        print(f"duration = {self.duration}")
        print(f"enrolled_students = {self.enrolled_students}")

C1 = Course("Python", 3)
C2 = Course("Data Science", 6)
C3 = Course("Machine Learning", 8)

C1.enroll("Rajesh")
C1.enroll("Ramesh")

C2.enroll("Suresh")

print("\nCourse Details:")

C1.display()
C2.display()
C3.display()

print("\nTotal courses =", Course.total_courses)

print("\nDuration Validation:")

print("6 =", Course.valid_duration(6))
print("-2 =", Course.valid_duration(-2))

Course.update_minimum_duration(5)

print("\nMinimum duration =", Course.minimum_duration)