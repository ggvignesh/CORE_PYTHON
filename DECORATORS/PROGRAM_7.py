#7. Write a decorator called count_calls that tracks how many times a function has been called and prints the count each time.
# Hint: you will need to store state — use a mutable object (like a list or a dictionary attribute on the wrapper).
import functools
def count_calls(func):
    count = [0]
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        count[0] += 1
        print("Function called", count[0], "time(s)")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")
greet("Carol")
greet("David")