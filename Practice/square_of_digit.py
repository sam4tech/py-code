# Q4 Write a program that will take three digits from the user and add the square of each digit.

num = input("Enter a number : ")
sum = 0
for i in num :
    sq =int(i)* int(i)
    sum = sum + sq 
print (f"Square of digits : {sum}")

#output
# Enter a number : 123
# 14