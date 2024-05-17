# Q2 : Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the
# digits.



# num = int (input("Enter first number :"))
num = 7536
tmp = num
sum = 0

while num > 0:
    rem = num % 10
    sum = sum * 10 + rem
    num //= 10    

# reverse_number = num [ : : -1]
# print(reverse_number )
print(f"original : {tmp}")

print(f"reverse :  {sum}")
print(" ".join(str(sum)))
# print (str(sum).split()) ==> converts string to list
