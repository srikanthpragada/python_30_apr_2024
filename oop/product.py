
class Product:
    # class attribute or static attribute 
    taxrate = 15 
    count = 0

    @staticmethod
    def getcount():
        return Product.count 
    
    def __init__(self, name, price = 0) -> None:
        # Object attributes 
        self.name = name 
        self.price = price 
        Product.count += 1

       
    def getprice(self):
        return self.price 
    
    def getnetprice(self):
        return self.price + self.price * Product.taxrate / 100 
    
    def setprice(self,newprice):
        self.price = newprice 

    def hikeprice(self, hikerate):
        self.price = self.price + self.price * hikerate / 100 

    @staticmethod
    def gettaxrate():
        return Product.taxrate 
    
    
p = Product('Bose Speakers', 30000)
print(Product.gettaxrate())
print(p.gettaxrate())

p.hikeprice(10)
print(p.getnetprice())

