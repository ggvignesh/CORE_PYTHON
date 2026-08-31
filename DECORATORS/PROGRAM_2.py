#2. Write a simple decorator called my_decorator that prints 'Function is starting' before and 'Function is done' after any function it wraps. Apply it to a function greet() that prints 'Hello!'.

def my_decorator(func):
    def wrapper():
        print("Function is starting")
        func()
        print("Function is done")
    return wrapper

@my_decorator
def greet():
    print("Hello!")
greet()