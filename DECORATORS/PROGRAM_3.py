#3. What is the purpose of *args and **kwargs in the wrapper function inside a decorator? Why is it important to include them?

print("*args is used to accept any number of positional arguments.")
print("**kwargs is used to accept any number of keyword arguments.")
print("They are important because a decorator should be able to")
print("work with functions having different numbers and types of arguments.")
print("Without *args and **kwargs, the wrapper may fail when the")
print("decorated function requires parameters.")