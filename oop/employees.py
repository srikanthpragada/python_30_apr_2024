class Employee:
    def __init__(self, name, email) -> None:
        self.name = name 
        self.email = email 
    
    def show(self):
        print(self.name)
        print(self.email)

    def setemail(self, newemail):
        self.email = newemail 

    @property 
    def firstname(self):
        pos = self.name.find(' ')
        return self.name[:pos]
    

class FTEmployee(Employee):
    def __init__(self, name, email, salary) -> None:
        super().__init__(name, email)
        self.salary = salary 

    # Overriding 
    def show(self):
        super().show()
        print(self.salary)

    def getsalary(self):
        return self.salary 


fe = FTEmployee("Scott Guithrie", "scott@microsoft.com", 300000)
fe.show() 
print(fe.firstname)




