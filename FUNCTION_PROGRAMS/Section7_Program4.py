#4. Write a function that returns another function. Example: make_multiplier(3) should return a function that multiplies any number by 3.

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

triple = make_multiplier(3)

print(triple(5))
print(triple(10))