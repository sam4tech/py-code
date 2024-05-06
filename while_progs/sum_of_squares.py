i = int(input("Enter the first number :"))
n = int(input("Enter the last number :"))
sum = 0
while(i<=n) : 
    sum = sum + (i*i)
    i=i+1

print("Sum of sqaures of numbers from i to n : ", sum)