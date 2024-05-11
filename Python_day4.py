# find the total character in a string without using len function

str = input("Enter a string to find number of characters : ")
# print(str)
count = 0
for i in str :
    count += 1

print(count)

# find the no. of vowels in a string.

str = input("Enter a string to check vowels : ") 
v_cnt = 0
for i in str :
    # 
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ) :
        v_cnt += 1
print(v_cnt)


# find the no. of consonants in a string.

str = input("Enter a string to check consonants : ") 
cons_cnt = 0
for i in str :
    #print(i)
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i== 'u' ) :
        cons_cnt += 0
    else :
        cons_cnt += 1

print("Count of consonants in the string : ", cons_cnt)


# Make a loop from 99 to 4 and print numbers that are divisible by 5 and 7

for i in range (99, 3, -1) :
    # print(i)
    if (i%5 == 0 and i%7 == 0) :
        print(i, end = " ")

#take a user input and do the following 

from datetime import datetime

import os

print("1. Print current system time. ")
print("2. Create a folder with name. ")
print("3. Create a file with name. ")
print("4. shutdown os. ")
ch = input("Enter your choice :")

if (ch == '1') :
    now = datetime.now()
    print("Current time =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)

elif (ch == '2') :

    path = "C:\\Users\\cutes\\OneDrive\\Desktop\\Python\\samiii"

    if not os.path.exists(path) :
        # os.chdir(path)
        new_folder =input("Enter folder name : ")
        os.makedirs(new_folder)
        print("Folder created ")
    else :
        print("Folder already exists")

elif (ch == '3') :
    new_file = "file1.txt"
    file = open(new_file, "w")
    file.write("heyy sam")
    file.close()

elif (ch == '4') :
    
    shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 
    
    if shutdown == 'no': 
        exit() 
    else: 
        os.system("shutdown /s /t 1") 


# Take a string from user and check according to the below conditions :
# 1. string must have 3 capital letters. 
# 2. string must have 3 small letters.
# 3. string must have a number.
# 4. string must have a minimum length between 5 and 15.
# 5. string must have only one of these #, @, !



s = input("Enter your password : ")
# s = "SMRiti31#"

lower, upper, special, count = 0, 0, 0, 0
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="#@!"
digits="0123456789"
if ( 5<=len(s)<= 15) :
    for i in s:
 
         # counting uppercase alphabets
        if (i in capitalalphabets):
            upper+=1 

        # counting lowercase alphabets
        if (i in smallalphabets):
            lower+=1           
   
         # counting digits
        if (i in digits):
            count+=1           
 
        # counting the mentioned special characters
        if(i in specialchar):
            special+=1  
                 
if (lower>=2 and upper>=3 and special>=1 and count>=1 and lower+special+upper+count==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")

