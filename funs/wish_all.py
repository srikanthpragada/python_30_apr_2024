# varying args 
def wish(*names, message = "Hi"):
    for n in names:
        print(message , n)


wish('Andy', "Mark", "Bill", message =  "Hello")
wish('Scott','James')
