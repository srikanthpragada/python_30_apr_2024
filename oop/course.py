class Course:
    def __init__(self, title, fee) -> None:
        self.title = title
        self.__fee = fee

    def getfee(self):
        return self.__fee 
    
c = Course("AWS", 5000)
print(c.getfee())
print(c.__fee)

