#4. Use a lambda with .sort() to sort this list of tuples by the second element: [(1,'banana'),(2,'apple'),(3,'cherry')]
fruits = [(1, "banana"),(2, "apple"),(3, "cherry")]
fruits.sort(key=lambda x: x[1])
print(fruits)