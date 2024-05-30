import json 

class Person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age

    
p = Person("Bill Gates", 65)
print(json.dumps(p.__dict__))
