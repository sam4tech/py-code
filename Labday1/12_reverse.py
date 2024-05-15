# 12. Reverse the below list without using any inbuilt keywords (like reverse() or [::-1])
# List = ["cat","tiger","lion", "zebra" , "crocodile", "snack"]



list = ["cat","tiger","lion", "zebra" , "crocodile", "snack"]
rev_list = []
for i in range (len(list)-1, -1, -1) :
    print(list[i])
    rev_list.append(list[i])

print(rev_list)
