#2. Use filter() to extract all words from a list that start with a capital letter.
words = ["Apple","banana","Cat","dog","Elephant","fish"]
result = list(filter(lambda word: word[0].isupper(), words))
print(result)