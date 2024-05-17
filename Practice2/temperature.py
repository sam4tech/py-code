# 3. Write a program that will determine weather when the value of temperature and
# humidity is provided by the user.


temp = int (input("Enter the temperature value : "))
humid = int (input("Enter the humidity value : "))

if temp >=30 :
    if humid >= 90 :
        print("Weather is HOT AND HUMID")
    else : 
        print("Weather is HOT")
elif temp < 30 : 
    if humid >= 90 :
        print("Weather is COOL AND HUMID")
    else : 
        print("Weather is COOL")

