

num = int(input("Enter the number : \n >>> "))
# num = 1634
temp = num
sum = 0
print(len(str(temp)))
while num > 0 :
    sum = sum  +((num % 10)**len(str(temp)))
    num = num//10

print("original number : ", temp)
print("Sum of numbers : ", sum)


if temp == sum :
    print("Number is Narcissist.")
else :
    print("Number is NOT Narcissist.")











# num = input("Enter a number : ")
# # temp = num
# sum = 0
# cnt = 0
# length = len(num)
# for i in num :
#     c = int(i) ** length
#     sum = sum + c 
#     cnt +=1 
# print (f"sum of power of digits : {sum}")
# print(cnt)
# print(len(num))

# if cnt == length and sum == int(num)  :
#         print("Narcissist number")
# else :
#         print("Not Narcissist.")




