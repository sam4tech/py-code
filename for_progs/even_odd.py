# Python program to print all the even numbers within the given range.
 
start_value = int (input("\nEnter starting value :"))
end_value = int (input("\nEnter ending value :"))

print("\nEven numbers")
for i in range (start_value , end_value) :
    if(i%2==0):
        print(i, end = ' ')

print("\nOdd numbers")
for i in range (start_value , end_value) :
    if(i%2!=0):
        print(i, end = ' ')