
def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False 
        
    return True 


print(isprime(11), isprime(113), isprime(27))