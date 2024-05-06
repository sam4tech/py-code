i=1
n= int(input("Enter last no :"))
sum = 0
while(i<=n) :
    if(i%2 ==0) :
        sum = sum + i

    i=i+1

print("Sum of even numbers : ", sum)
