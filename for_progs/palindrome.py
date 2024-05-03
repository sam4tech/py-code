# Python program to check if the given string is a palindrome.

num = str (input("\n Enter a string : "))
sum = 0
rev = " "

for i in num :
    rev = i + rev
print(rev)
