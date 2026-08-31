#3. Employee class. increment_salary(amount) to increase employer's salary
class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def increment_salary(self,amount):
        self.salary += amount

e1 = Employee(1,"Rajesh",25000)
e2 = Employee(2,"Ravikanth",50000)
e3 = Employee(3,"Suresh",75000)
e4 = Employee(4,"Naresh",100000)
e1.increment_salary(10000)
print(e1.salary)