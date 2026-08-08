#10. Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.
text = "Python"
result = list(map(ord, text))
print(result)