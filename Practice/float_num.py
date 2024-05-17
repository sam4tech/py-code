# 7. Display float number with 2 decimal places using print()

num = float (input("Enter a decimal number : "))

print("Original number :", num)

print("Rounding the number to 2 decimal places : ", round(num, 2))


#second method 
rounded_number = format(num, ".2f")  

print("Rounding the number to 2 decimal places : ", rounded_number )
