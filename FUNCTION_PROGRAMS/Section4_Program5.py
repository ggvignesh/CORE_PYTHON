#5. Why are keyword arguments considered more readable? Write an example that demonstrates this clearly.
print("Keyword arguments improve readability because each value is explicitly associated with its parameter name.")
print("This makes the code easier to understand and reduces mistakes caused by incorrect argument order.")

def employee(name, salary, department):
    print("Name       :", name)
    print("Salary     :", salary)
    print("Department :", department)

employee(
    department="IT",
    salary=50000,
    name="Rahul"
)