
num = input("Enter a number : ")
# temp = num
sum = 0
cnt = 0
length = len(num)
for i in num :
    c = int(i) ** length
    sum = sum + c 
    cnt +=1 
print (f"sum of power of digits : {sum}")
print(cnt)
print(len(num))

if cnt == length and sum == int(num)  :
        print("Narcissist number")
else :
        print("Not Narcissist.")

