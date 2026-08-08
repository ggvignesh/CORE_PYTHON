#5. Chain map() and filter(): from [1..10], first filter out odds, then square the remaining evens.
numbers = list(range(1, 11))
result = list(map(lambda x: x ** 2,filter(lambda x: x % 2 == 0, numbers)))
print(result)