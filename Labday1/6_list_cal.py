# ##  Write a program which will perform sum and multiplication ,that sums and multiplies
# (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10,
# and multiply([1, 2, 3, 4]) should return 24.

mylist = [1, 2, 3, 4]
sum = 0
mul = 1
for i in mylist :
    sum = sum + i
print("Sum of all elements in the list : ", sum)

for i in mylist :
    mul = mul * i
print("Multiplication of all elements in the list : ", mul)

##OUTPUT 

# Sum of all elements in the list :  10
# Multiplication of all elements in the list :  24