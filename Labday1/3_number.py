# 3. Write a program that stores a number and keeps trying to get user input until the user enters the
# number correctly. As soon as the correct number is entered, it prints: Correct!


num = 60 
u_number = int(input("Enter the number : "))

if(num == u_number) :
    print("Correct!!")
else :
    print("Incorrect, Keep trying...")


## OUTPUT
# Enter the number : 50
# Incorrect, Keep trying...