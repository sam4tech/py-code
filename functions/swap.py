def swapnum(x,y) :
    print("before swap",x,y)
    x,y=y,x

x=10
y=20
swapnum(10,20)
print("swapped num : ",x,y)


# before swap 10 20
# swapped num :  10 20

def func(list1) :
    print(list1, id(list1))

mylist=[10,20]
func(mylist)


print("++++++++++++++++++++++++++=")
def func1(list1) :
    print(list1[0])

mylist=[10,20]
func1(mylist)


print("++++++++++++++++++++++++++=")
def func1(list1) :
    list1[0] =200
    print(list1)

mylist=[10,20]
func1(mylist)
print(mylist)