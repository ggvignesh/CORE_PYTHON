#7. voting eligible or not eligible
class Voting:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
    @staticmethod
    def is_eligible(age):
        if age>18:
            return "Eligible to vote"
        return "Not Eligible"
V1 = Voting("Ram",28)
V2 = Voting("Charan",20)
V3 = Voting("Arjun",17)
V1.display()
print(V1.is_eligible(V1.age))