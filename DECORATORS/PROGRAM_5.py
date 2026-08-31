#5. Write a decorator called validate_positive that checks all positional arguments passed to a function. If any argument is negative, print an error message and return None without calling the function.
# Test it on a function multiply(a, b).
import functools
def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if value < 0:
                print("Error: Negative argument is not allowed.")
                return None
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def multiply(a, b):
    return a * b

print("Result:", multiply(5, 4))
print("Result:", multiply(-5, 4))