# Explain the difference between:
# map(str, [1, 2, 3])
# map(lambda x: str(x), [1, 2, 3])
# Which one is faster and why?
result = list(map(str, [1,2,3]))
print(result)

result = list(map(lambda x: str(x), [1,2,3]))
print(result)

#Which is faster?
print("map(str, ...) is slightly faster because it directly uses the built-in str() function without the extra lambda call.")