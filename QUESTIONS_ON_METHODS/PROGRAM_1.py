#1. display_details() to print all the student's details
class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"marks = {self.marks}")

s1 = student("Vignesh",23,85)
s2 = student("Rajesh",25,90)
s3 = student("Srinivas",24,60)
s1.display()