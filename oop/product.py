class Product:
    def __init__(self, name, price = 0) -> None:
        self.name = name 
        self.price = price 

    def getprice(self):
        return self.price 
    
    def getnetprice(self):
        return self.price * 1.12 
    
    def setprice(self,newprice):
        self.price = newprice 

    def hikeprice(self, hikerate):
        self.price = self.price + self.price * hikerate / 100 

    
p = Product('Bose Speakers', 30000)
p.hikeprice(10)
print(p.getnetprice())

