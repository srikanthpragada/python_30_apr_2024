class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.message = f"Invalid Amount --> {amount}"
       

    def __str__(self) -> str:
        return self.message 
        

class Account:
    def __init__(self, acno : int, customer : str, balance = 0) -> None:
        self.acno = acno
        self.customer = customer 
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0 :
            raise InvalidAmountError(amount)
        
        self.balance += amount 

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount 
        else:
            raise ValueError("Insufficient Balance!")    

    def getbalance(self):
        return self.balance 
    

a1 = Account(customer = "Bill Gates", acno = 101)
a1.deposit(-100000)
a1.deposit(50000)
print(a1.getbalance())

a2 = Account(2, "Larry Page", 100000)
a2.withdraw(150000)
print(a2.getbalance())



        