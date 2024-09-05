print("Select One Of The Following Options")
print("Enter {A} For Multiply")
print("Enter {B} For Divide")
print("Enter {C} For Add")
print("Enter {D} For Subtract")
print("Enter {E} For Remainder Division")
choice = input(">").lower()
num1 = float(input("Enter Your First Number: "))
num2 = float(input("Enter Your Second Number: "))
total = 0
if choice == "a":
    total = num1 * num2
elif choice == "b":
    total = num1 / num2
elif choice == "c":
    total = num1 + num2
elif choice == "d":
    total = num1 - num2
elif choice == "e":
    total = num1 % num2
else:
    print("You Did Not Enter A Valid Choice")
print(total)