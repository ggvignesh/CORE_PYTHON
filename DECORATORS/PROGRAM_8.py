#8. Explain the difference between these two usages and what error (if any) the wrong one produces: Option A: @my_decorator Option B: @my_decorator() When is each form correct?
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()

print()
print("@my_decorator is correct when the decorator directly takes")
print("the function as its argument.")

print()
print("@my_decorator() is used when the decorator is a decorator factory")
print("that first accepts configuration arguments and returns a decorator.")