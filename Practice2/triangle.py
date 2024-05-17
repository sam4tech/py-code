# 2. Write a program that take a user input of three angles and will find out whether it can
# form a triangle or not.


x, y, z = map(int,input("Enter the three angles : ").split(','))
print("Angle 1: ", x)
print("Angle 2: ", y)
print("Angle 3: ", z)

angle = x+y+z
print(angle)
if angle == 180 :
    print("Its a triangle")
else :
    print("Not a triangle.")

##output
# Enter the three angles : 90,45,45
# Angle 1:  90
# Angle 2:  45
# Angle 3:  45
# 180
# Its a triangle