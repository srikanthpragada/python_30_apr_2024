
g = 100  # Global variable 

def f1():
    a = 10  #Enclosing variable
    global g
    g = 200

    # Local function 
    def f2():
        nonlocal a 
        a = 1 
        b = 20    # Local variable 

        print(a, b)

    f2()
    print(a)

f1() 
