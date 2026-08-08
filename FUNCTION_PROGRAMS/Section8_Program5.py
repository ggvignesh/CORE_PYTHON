#5. Can a lambda function call another function inside it? Write an example.
def square(x):
    return x * x

result = lambda n: square(n) + 10
print(result(5))