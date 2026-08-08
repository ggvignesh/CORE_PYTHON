#3. Write a function describe_person(name, *hobbies) where name is a regular param and hobbies are collected into a tuple.
def describe_person(name, *hobbies):
    print("Name :", name)
    print("Hobbies :", hobbies)

describe_person("Rahul", "Cricket", "Reading", "Music")