## 2. Write a program that adds two numbers and then prints out whether the sum of those two numbers
# is positive or negative.


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

result = num1 + num2
# print(result)

if(result>=0) :
    print("addition of two numbers is positive ")
else :
    print("addition of two numbers is negative ")

print(result)