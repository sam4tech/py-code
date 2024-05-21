# 4. Write a menu driven program
# a. In case the user has given the value from the option the following task should
# be done
# b. 1 cm to ft
# c. 2 km to miles
# d. 3 usd to inr
# e. 4 exit


print("Select the Conversion type.")
print("b. 1 cm to ft") 
print("c. 2 km to miles")
print("d. 3 usd to inr")
print("e. 4 exit")

ch = input("Enter the choice : ")

if ch == 'b' :
    print("cm to ft")
    num = float(input("Enter value in cm : "))
    res = num * 0.0328 
    print(f"value in ft is {res} ft")

elif ch == 'c' :
    print("km to miles")
    num = float(input("Enter value in km : "))
    res = num / 1.609
    print(f"value in miles is {res} miles")

elif ch == 'd' :
    print("usd to inr")
    num = float(input("Enter value in USD : "))
    res = num * 83.30 
    print(f"value in miles is {res} INR")
elif ch == 'e' :
    print("exit")
else :
    print("Invalid Input... Try again.")

