##CONDITIONAL statements 

city = "Jaipur"
if(city == "jaipur") :
    print("city is correct")
else :
    print("city is incorrect")


x = 15
y = 16
if(x>10 and y>18) :
    print("age is valid")
else :
    print("age is not valid")

    

# Checks MInimum of three

a = 5
b = 4
c = 20
if(a<b and a<c) :
    print("a is minimum")
elif(b<a and b<c) :
    print("b is minimum")
else :
    print("c is minimum")


# CHeck grades based on marks 
marks  = 105

if(marks > 60 and marks <=75 ) :
    print("Averge")
elif(marks > 75 and marks <=85) :
    print("Good")
elif(marks > 85 and marks <=95) :
    print("Excellent")
elif(marks > 95) :
    print("Brilliant")
else :
    print("FAIL")



# Program to check month number

month_number = 7
# month_number = int(input("Enter a month number :: "))
if(month_number == 1) :
    print("January")
elif(month_number == 2) :
    print("February")
elif(month_number == 3) :
    print("March")
elif(month_number == 4) :
    print("April")
elif(month_number == 5) :
    print("May")
elif(month_number == 6) :
    print("June")
elif(month_number == 7) :
    print("July")
elif(month_number == 8) :
    print("AUgust")
elif(month_number == 9) :
    print("September")
elif(month_number == 10) :
    print("October")
elif(month_number == 11) :
    print("November")
elif(month_number == 12) :
    print("December")
else :
    print("Invalid")


# Take a number and check its divisibility by 6

num = 56
# num = int(input("Enter a number :: "))
if(num%2 == 0 and num%3 == 0) :
    print("Number is divisible by 6")
else :
    print("number is NOT divisible by 6")


# Take a user input units  and calc the total amount
# first 10 units = 50 rs.
# next 20 units = 20 rs.
# next 10 units = 10 rs.
# other units = 5 rs.

units = int(input("Enter number of units : "))
# units = 25
totalamt = 0
if ( units > 0 ) : 
    if( units <= 10) :
        firstunit = units * 50
        totalamt = totalamt + firstunit
        print(f"Total amount for {units} units is Rs. {totalamt}")
 
    elif( units <= 30) :
        firstunit = (10 * 50) + (units - 10) * 20
        totalamt = totalamt + firstunit
        print(f"Total amount for {units} units is Rs. {totalamt}")

    elif( units <= 40) :
        firstunit = (10 * 50) + (20 * 20) + (units - 30) * 10
        totalamt = totalamt + firstunit
        print(f"Total amount for {units} units is Rs. {totalamt}")


    else :
        firstunit = (10 * 50) + (20 * 20) + (10 * 10) + (units - 40) * 5
        totalamt = totalamt + firstunit
        #print(totalamt)
        print(f"Total amount for {units} units is Rs. {totalamt}")


else :
    print("Enter positive number : ")
























# a = int(input("Enter your age"))

# if(0<=a<=20):
#     print("child")
    
# elif(21<=a<=50):
#     print("Young")
# elif(51<=a<=80):
#     print("Old")
# else :
#     print("Try again")
