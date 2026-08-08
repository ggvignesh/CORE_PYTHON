#12. Use reduce() to concatenate a list of characters into a single string.
# Example input: ['P', 'y', 't', 'h', 'o', 'n'].
from functools import reduce
letters = ['P', 'y', 't', 'h', 'o', 'n']
word = reduce(lambda x, y: x + y, letters)
print(word)