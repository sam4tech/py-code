# Calculation of numbers

choice = input("Enter your choice : ")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if (choice == "addition"):
    result = num1 + num2
    print(result)

elif (choice == "subtraction") :
    result = num1 - num2
    print(result)

elif (choice == "multiplication") :
    result = num1 * num2
    print(result)

else :
    print("Try again...")
