#1. Write a function intro(name, city, hobby) that prints a sentence about a person. Call it in two different orders and observe the difference.
def intro(name, city, hobby):
    print(name, "is from", city, "and likes", hobby + ".")

# Correct order
intro("Rahul", "Hyderabad", "Cricket")

# Different order
intro("Cricket", "Rahul", "Hyderabad")