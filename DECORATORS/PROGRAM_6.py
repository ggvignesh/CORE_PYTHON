#6. Create a decorator factory called repeat(n) that runs the decorated function exactly n times. Then stack it with a logger decorator and apply both to a function.
# Trace the exact order in which the wrappers execute.
import functools
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Logger: Function started")
        result = func(*args, **kwargs)
        print("Logger: Function finished")
        return result
    return wrapper

def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                print("Repeat:", i + 1)
                func(*args, **kwargs)
        return wrapper
    return decorator

@logger
@repeat(3)
def greet():
    print("Hello!")
greet()