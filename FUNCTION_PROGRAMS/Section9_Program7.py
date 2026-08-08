#7. Use reduce() to find the longest string in a list: ['cat', 'elephant', 'dog', 'rhinoceros']
from functools import reduce
words = ["cat","elephant","dog","rhinoceros"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b,words)
print(longest)