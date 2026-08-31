#12. Design a decorator pipeline: write three separate decorators — @authenticate(role), @timer, and @logger — and apply all three to a single function. Then write a detailed explanation of the exact order in which execution flows through the three wrappers when the function is called, and when it returns.
# Include a diagram in code comments showing the nesting.
import functools
import time

def authenticate(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            print("Authentication: Checking user role...")
            if user.get("role") != role:
                print("Authentication: Access Denied")
                return None
            print("Authentication: Access Granted")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Timer: Starting timer")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("Timer: Execution time:",
              round(end - start, 6),
              "seconds")
        return result
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Logger: Function started")
        result = func(*args, **kwargs)
        print("Logger: Function finished")
        return result
    return wrapper

@authenticate("admin")
@timer
@logger
def delete_record(user):
    print(user["name"], "deleted the record.")
admin = {
    "name": "Alice",
    "role": "admin"
}

guest = {
    "name": "Bob",
    "role": "guest"
}

print("----- ADMIN USER -----")
delete_record(admin)
print()
print("----- GUEST USER -----")
delete_record(guest)