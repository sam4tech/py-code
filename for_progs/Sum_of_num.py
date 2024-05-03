#  Python program to calculate the sum of all numbers from 1 to a given number.

start_value = int (input("\nEnter starting value :"))
end_value = int (input("\nEnter ending value :"))
sum = 0

print("\Sum of all numbers")
for i in range (start_value , end_value) :
    sum = sum + i 

print(sum)

