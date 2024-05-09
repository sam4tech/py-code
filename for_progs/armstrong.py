# Python program to check if a given number is an Armstrong number

num = int(input("\n Enter a number : "))
sum = 0
# rev = " "
end_value = str(num)
for i in end_value :
    rem = num%10
    sum = sum * 10 + rem
    num = num/10

print(sum)


