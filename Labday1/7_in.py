# ## Write a program that takes a value (i.e. a number, string, etc) x and a list of values a, and returns
# True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for
# the sake of the exercise you should pretend Python did not have this operator.)


# numlist = input


lst = []
 
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
    lst.append(ele)  
 
print(lst)

x = 7

# for i in lst :
if(i == x) :
    print("true")
else :
    print("False")