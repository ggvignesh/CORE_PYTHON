# Given a list of numbers:
# [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# Use map() to square each number
# Use filter() to keep only numbers divisible by 5
# Use reduce() to calculate the sum of remaining numbers
from functools import reduce
numbers = [5, 10, 15, 20, 25, 30]
result = reduce(lambda x, y: x + y,filter(lambda x: x % 5 == 0,map(lambda x: x ** 2, numbers)))
print(result)