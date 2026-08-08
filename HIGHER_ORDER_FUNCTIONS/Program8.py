#8. Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.
from functools import reduce
numbers = list(map(int, input("Enter numbers: ").split()))
largest = reduce(lambda a, b: a if a > b else b, numbers)
print("Largest =", largest)