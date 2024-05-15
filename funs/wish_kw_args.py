def wish(name, message):
    print(f"{message} {name}")


wish("Steve", "Hi")  # positional args
wish(message = "Hello", name = 'Tom')   # keyword args 
#wish(message = "Hi", "Tom")
