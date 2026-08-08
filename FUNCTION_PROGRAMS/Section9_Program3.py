#3. Use reduce() to find the product of all numbers in a list: [1, 2, 3, 4, 5] → 120
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)