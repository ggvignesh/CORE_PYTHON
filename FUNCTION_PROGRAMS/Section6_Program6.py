#6. Write a function mixed(a, b, *args, **kwargs) and call it with at least 6 arguments. Print each part.
def mixed(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("*args =", args)
    print("**kwargs =", kwargs)

mixed(10,20,30,40,50,name="Rahul",city="Hyderabad")