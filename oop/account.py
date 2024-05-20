class Account:
    def __init__(self, acno : int, customer : str, balance = 0) -> None:
        self.acno = acno
        self.customer = customer 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 

    def withdraw(self, amount):
        self.balance -= amount 

    def getbalance(self):
        return self.balance 
    

a1 = Account(customer = "Bill Gates", acno = 101)
a1.deposit(100000)
a1.deposit(50000)
print(a1.getbalance())

a2 = Account(2, "Larry Page", 100000)
a2.withdraw(50000)
print(a2.getbalance())



        