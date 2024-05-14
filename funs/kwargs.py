def show(**kwargs):
   print(kwargs)

def showall(*args, **kwargs):
   print(args)
   print(kwargs)


show(a = 10, b = 20)
show(name = "Abc", age = 20)

showall(10,20, x = 10)


