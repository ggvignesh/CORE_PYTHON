#2. Write a function run_twice(func, value) that calls func on value twice and returns the final result.
def square(x):
    return x * x

def run_twice(func, value):
    return func(func(value))

result = run_twice(square, 2)
print(result)