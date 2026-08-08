#1. Use map() to convert a list of temperatures in Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
print(fahrenheit)