#swap without third variable

a = int (input("Enter first number :"))
b = int (input("Enter second number :"))

print(f"a = {a} , b = {b}")
a = a + b
b = a - b
a = a - b
print("After swapping : ")
print(f"a = {a} , b = {b}")

# ## output 
# Enter first number :35
# Enter second number :66
# a = 35 , b = 66
# After swapping :
# a = 66 , b = 35