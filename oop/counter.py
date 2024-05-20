class Counter:
    #constructor 
    def __init__(self, value = 0):
        # Object attribute 
        self.initvalue = value 
        self.value = value 
    
    # Method 
    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1
    
    def getvalue(self):
        return self.value 
    
    def reset(self):
        self.value =  self.initvalue 


c1 = Counter()    # Create an Object 
c1.inc()
c1.inc()
print(c1.getvalue())

c2 = Counter(10)     # Create an Object
c2.dec()
c2.reset()
print(c2.getvalue())


