# default arguments 
def wish(name = 'Guest', message = 'Hello'):
    print(f"{message} {name}")


wish("Steve", "Hi")  # positional args
wish(message = "Hi")   # keyword args 
wish() 
wish("Bob")



