class Course:
    def __init__(self, title, fee) -> None:
        self.title = title
        self.__fee = fee

    def getfee(self):
        return self.__fee 
    
c = Course("AWS", 5000)
print(c.getfee())
print(c._Course__fee)
print(c.__dict__)



