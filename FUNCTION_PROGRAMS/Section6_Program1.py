#1. Write a function multiply_all(*args) that returns the product of all numbers passed.
def multiply_all(*args):
    product = 1
    for num in args:
        product *= num
    return product

print(multiply_all(2, 3, 4))
print(multiply_all(5, 10))