# Take 5 numbers and display sum 
# Handle exceptions 

total = 0
count = 0 
while count < 5:
    try:
        n = int(input("Enter number :"))
        total += n
        count += 1
    except:
        print("Invalid number!")


print(total)

