#5. Can you store the same function under multiple names in a dictionary? Test it and explain what happens.
def greet():
    return "Welcome to Python"

functions = {"hello": greet,"welcome": greet,"start": greet}

print(functions["hello"]())
print(functions["welcome"]())
print(functions["start"]())