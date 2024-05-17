# Q5 Write a program that will check whether the number is armstrong number or not.

num = int(input("Enter the number : \n >>> "))
temp = num
sum = 0

while num > 0 :
    sum = sum  +((num % 10)**3)
    num = num//10

print("original number : ", temp)
print("Sum of numbers : ", sum)


if temp == sum :
    print("Number is Armstrong.")
else :
    print("Number is NOT Armstrong.")
























# num = input("Enter a number : ")
# # temp = num
# sum = 0

# for i in num :
#     c = int(i) ** 3
#     sum = sum + c 
# print (f"Cube of digits : {sum}")

# if sum == int(num)  :
#     print("Armstrong number")
# else :
#     print("Not armstrong.")
