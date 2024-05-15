# List in python

# # The list is written as a list of comma-separated values (items) between square brackets. 
# Items in a list need not be of the same type.
# List is a mutable data type means elements can be changed.
# The first element of the list is stored at index 0 and the last element is stored at the location n-1 where n is the size of list. 
# Also when a list is printed then no need to print each element separately we just need to pass name of list to print() function.

mylist = [10,20,"hello"]

print(type(mylist)) 
#list type

print(mylist[0]) #10

print(mylist[2])  #hello

print(mylist[-1]) # hello

print(mylist[0:3]) #[10, 20, "hello"]

# value update

mylist[0] = 50

print(mylist) #[50, 20, 'hello']

# APPEND FUNCTION to add only one  element
mylist.append(88)

print(mylist) # [50, 20, 'hello', 88]

# EXTEND FUNCTION to add multiple elements.

mylist.extend("yash")   # [50, 20, 'hello', 88, 'y', 'a', 's', 'h']

print(mylist)

mylist.extend(["yash"])   #[50, 20, 'hello', 88, 'y', 'a', 's', 'h', 'yash']

print(mylist)

mylist.extend(["yash", 101])   #[50, 20, 'hello', 88, 'y', 'a', 's', 'h', 'yash']

print(mylist)   ## [50, 20, 'hello', 88, 'y', 'a', 's', 'h', 'yash', 'yash', 101]

##delete last element

mylist.pop() 
deleted_item = mylist.pop(0) #stores the deleted element

print(mylist)  ## [20, 'hello', 88, 'y', 'a', 's', 'h', 'yash', 'yash']


mylist.remove("h")

##create a list and if the item is INT then append its square to the list.


numlist = [2, 4, "a", 6.0, "s"]
print(numlist)
newlist =[]
for i in numlist :
    if(type(i) is int) :
        x = i**2
        newlist.append(x)

print(newlist)

###neww

strlist = [2, 4, "Smriti", 6.0, 'y']
print(strlist)   #[2, 4, 'Smriti', 6.0, 'y']
newstrlist =[]
for i in strlist :
    if(type(i) is str) :
        x = i[0] + i[-1]
        print(x)
        newstrlist.extend([x])

print(newstrlist)  #['Si', 'yy']
