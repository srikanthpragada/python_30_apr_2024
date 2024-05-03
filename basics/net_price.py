# Calculate net price after 10% discount 

data = input("Enter Price :")
price = int(data)   # convert str to int 
discount = price * 10 // 100   # Caculate 10% discount
net_price = price - discount 

print('Net price =', net_price)




