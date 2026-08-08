#5. Why would you use a default parameter instead of just hardcoding a value inside the function? Explain with an example.
print("Default parameters make a function flexible. The default value is used when no argument is supplied, but it can still be changed whenever needed.")

def greet(name, message="Hello"):
    print(message, name)

greet("Alice")
greet("Bob", "Good Morning")