#3. Store the functions upper, lower, and title (string methods) in a dictionary. Let the user choose which one to apply.
operations = {
    "upper": str.upper,
    "lower": str.lower,
    "title": str.title
}

text = input("Enter a string: ")
choice = input("Choose (upper/lower/title): ")

if choice in operations:
    print(operations[choice](text))
else:
    print("Invalid Choice")