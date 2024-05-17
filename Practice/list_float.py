# Q9 Accept a list of 5 float numbers as an input from the user


list = []

for i in range (1,6) :
    n = input("enter {}th number : " .format(i))
    list.append(n)
print(list)


# OUTPUT

# enter 1th number : 2
# enter 2th number : 36
# enter 3th number : 54
# enter 4th number : 86
# enter 5th number : 95
# ['2', '36', '54', '86', '95']