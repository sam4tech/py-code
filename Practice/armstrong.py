# Q5 Write a program that will check whether the number is armstrong number or not.

num = input("Enter a number : ")
# temp = num
sum = 0

for i in num :
    c = int(i) ** 3
    sum = sum + c 
print (f"Cube of digits : {sum}")

if sum == int(num)  :
    print("Armstrong number")
else :
    print("Not armstrong.")
