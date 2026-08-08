#6. Write a function multiplier(number).
# The outer function receives one number.
# The inner function receives another number.
# Print their multiplication.
# Return the inner function.
def multiplier(number):
    def multiply(num):
        print("Multiplication =", number * num)
    return multiply

mul = multiplier(8)
mul(5)