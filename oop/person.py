class Person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"
    
    def __eq__(self, other) -> bool:
        return  self.name == other.name and self.age == other.age 
    
    def __gt__(self, other):
        return  self.age > other.age 
    
    def __int__(self):
        return  self.age 
    

p1 = Person("Rosum", 50)
p2 = Person("Larry", 40)
p3 = Person("Rosum", 50)

print( int(p1) + int(p2))   # p1.__int__()


print(p1, str(p1))  # p1.__str__()
print(p1 == p2)     # p1.__eq__(p2)
print(p1 == p3)     # p1.__eq__(p3)
print(p1 > p2)      # p1.__gt__(p2)

people = [p1,p2,p3]
for p in sorted(people):
    print(p)

