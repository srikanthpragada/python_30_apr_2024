# Take numbers until 0 is given and dispaly sum of numbers 

total = 0

while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break    # terminate loop 

    total += num 


print(total)
