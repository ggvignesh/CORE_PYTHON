#2. Write a function create_profile(username, email, age) and call it using keyword arguments.
def create_profile(username, email, age):
    print("Username :", username)
    print("Email    :", email)
    print("Age      :", age)

create_profile(
    age=23,
    username="GouriVignesh",
    email="gouri@gmail.com"
)