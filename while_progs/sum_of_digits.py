i=int(input("Enter a number  :"))
sum = 0
while( i>0 ) :
    rem = i%10
    sum = sum + (rem*rem)
    i=i//10