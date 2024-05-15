# 11. Find the duplicate numbers from below list
# a. List = [5, 8,4,18,8,55,6,8,3,18,5,3,44,




List = [5, 8, 4, 18, 8, 55, 6, 8, 3, 18 , 5, 3, 44]

uniq_list = []

duplicate_list = []

for i in List :
    if i not in uniq_list :
        uniq_list.append(i)
    elif i not in duplicate_list :
        duplicate_list.append(i)

print(duplicate_list)


#output
# [8, 18, 5, 3]