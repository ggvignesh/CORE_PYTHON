#3. What is the SyntaxError in: def func(name='Guest', age)? Fix it.
def func(age, name="Guest"):
    print("Name :", name)
    print("Age  :", age)

func(22)
func(25, "Rahul")