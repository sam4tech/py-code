# Q8 Print all factors of a given number provided by the user.


num = int(input("Enter the number to find the factors : "))

for i in range (1, num+1) :
    if(num%i==0) :
        print(i)