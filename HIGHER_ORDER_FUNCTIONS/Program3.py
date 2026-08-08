# Given a list:
# nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by 5 but NOT divisible by both.
# Explain how the logical condition works.

nums = [12, 15, 7, 18, 20, 21, 25]
result = list(filter(lambda x: (x % 3 == 0) ^ (x % 5 == 0), nums))
print(result)
