#4. Sort a list of tuples (name, age) by age in descending order using sorted() with a lambda key.
students = [("Rahul", 20),("Anil", 25),("Priya", 22),("Sneha", 19)]
result = sorted(students,key=lambda x: x[1],reverse=True)
print(result)