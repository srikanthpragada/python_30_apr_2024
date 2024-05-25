
st = input("Enter number :")
try:
    n = int(st)
    print(100 // n)
except ValueError:
    print("Sorry! Invalid number!")
else:
    print("Okay")
finally:
    print("Done!")

print("The End")


