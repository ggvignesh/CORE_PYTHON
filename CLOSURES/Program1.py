#1. Write a function electricity(rate_per_unit).
# The outer function receives the cost per unit.
# The inner function receives the number of units consumed.
# Print the total electricity bill.
# Return the inner function.
def electricity(rate_per_unit):
    def bill(units):
        print("Electricity Bill =", rate_per_unit * units)
    return bill

e = electricity(8)
e(120)