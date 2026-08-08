#6. Write your own version of map() called my_map(func, lst) using a regular loop. Verify if it gives the same results as the built-in.
def my_map(func, lst):
    result = []
    for item in lst:
        result.append(func(item))
    return result

numbers = [1, 2, 3, 4, 5]
print(my_map(lambda x: x * 2, numbers))
print(list(map(lambda x: x * 2, numbers)))