#2. Create a function display_tags(**kwargs) that prints each keyword-value pair on its own line.
def display_tags(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_tags(name="Rahul",city="Hyderabad",age=22)