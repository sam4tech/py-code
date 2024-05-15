## 8. Write a program that has two lists and print True if they have at least one member in common,
# False otherwise. You may use your is_member() function, or the in operator, but for the sake of the
# exercise, you should (also) write it using two nested for-loops.

list1 = [10, 30, 55, 87]

list2 = [20, 55, 40, 99]

for i in list1 :
    # print(i)
    for j in list2 :
        if i == j :
            print("elements are common in both lists : ", i)


##OUTPUT

# elements are common in both lists :  55