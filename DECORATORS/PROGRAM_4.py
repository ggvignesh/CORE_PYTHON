#4. What does @functools.wraps(func) do? Write an example showing what happens to __name__ with and without it.
import functools
# Without functools.wraps()
def decorator_without_wraps(func):
    def wrapper():
        func()
    return wrapper

@decorator_without_wraps
def greet_without_wraps():
    print("Hello")

print("Without functools.wraps:")
print(greet_without_wraps.__name__)

# With functools.wraps()
def decorator_with_wraps(func):
    @functools.wraps(func)
    def wrapper():
        func()
    return wrapper

@decorator_with_wraps
def greet_with_wraps():
    print("Hello")

print()
print("With functools.wraps:")
print(greet_with_wraps.__name__)