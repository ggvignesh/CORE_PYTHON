#11. Use filter() to remove all vowels from a string and print the final string.
text = "Python Programming"
vowels = "aeiouAEIOU"
result = "".join(filter(lambda x: x not in vowels, text))
print(result)