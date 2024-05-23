# 11. Print the sum of the current number and the previous number.
# a. Write a program to iterate the first 10 numbers and in each iteration, print the
# sum of the current and previous number.
# b. Expected result: 0,1,3,5,7,9,11,13,15,17


# n1 = 0
# n2 = 11
print ("Sum of the current and previous number.")
for i in range (0, 11) :
    n3 = i +(i+1)
    print(n3, end = " ")

# OUTPUT
# Sum of the current and previous number.
# 1 3 5 7 9 11 13 15 17 19 21 