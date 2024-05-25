
st = input("Enter number :")
try:
    n = int(st)
    print(100 // n)
except ValueError:
    print("Sorry! Invalid number!")
except ZeroDivisionError:
    print("Sorry! Zero is not valid!")

print("The End")


