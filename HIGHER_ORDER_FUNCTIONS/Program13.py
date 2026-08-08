#13. Given a list of integers, use map() with id() to print the memory address of each element.
# Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.
nums = [10, 350, 10, 350, 20]
addresses = list(map(id, nums))
print(addresses)

#Why some addresses repeat
print("Same integer objects may have the same memory address because Python can reuse immutable integer objects.")
print("Repeated values can therefore show the same id() within a running program.")