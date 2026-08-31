#9. Build a complete caching decorator called memoize that stores the results of previous calls in a dictionary (keyed by the arguments). If the same arguments are passed again, return the cached result without re-running the function.
# Test it on a recursive Fibonacci function and show how many function calls are saved.
import functools
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

normal_calls = 0
def fibonacci_normal(n):
    global normal_calls
    normal_calls += 1
    if n <= 1:
        return n
    return fibonacci_normal(n - 1) + fibonacci_normal(n - 2)

memoized_calls = 0
@memoize
def fibonacci(n):
    global memoized_calls
    memoized_calls += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
result1 = fibonacci_normal(n)
result2 = fibonacci(n)
print("Fibonacci result:", result1)
print("Normal function calls:", normal_calls)
print("Memoized function calls:", memoized_calls)
print("Function calls saved:", normal_calls - memoized_calls)