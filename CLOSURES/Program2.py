#2. Write a function salary(bonus).
# The outer function receives the bonus amount.
# The inner function receives the employee’s basic salary.
# Print the total salary after adding the bonus.
# Return the inner function.
def salary(bonus):
    def total_salary(basic_salary):
        print("Total Salary =", basic_salary + bonus)
    return total_salary

s = salary(5000)
s(25000)