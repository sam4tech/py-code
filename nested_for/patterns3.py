print("1==================================================================")

# 1 2 3 4 *
# 5 6 7 * *
# 8 9 * * *

row = 5
count = 1
for i in range(1,row+1) :
    for j in range(i,row):
        print(count, end=" ")
        count+=1
    for k in range(1,i+1):
        print("*", end=" ")
    print("")



print("2==================================================================")

# A B C D 1 
# A B C 1 2 
# A B 1 2 3 
# A 1 2 3 4


for i in range(1,5) :
    
    for j in range(1, 6-i):
        print(chr(64+j), end =" ")
    for k in range(1,i+1):
        print(k, end=" ")
    print("")




print("3==================================================================")

# A B C D 1 
# E F G 1 2 
# H I 1 2 3 
# J 1 2 3 4
# 1 2 3 4 5

row = 5
cnt = 1
for i in range(1,row+1) :
    for j in range(i, row):
        print(chr(cnt+64), end=" ")
        cnt+=1
    for k in range(1,i+1):
        print(k, end=" ")
    print("")



print("4==================================================================")

#         A
#       B C
#     D E F
#   G H I J
# K L M N O

row = 4
c = 1
num = 1
for i in range(1,row+1) :
    for j in range(i, row):
        print(" ", end=" ")
    #    cnt+=1
    for k in range(1,i+1):
        print(chr(c+64), end=" ")
        c+=1
    print("")



print("=======================================5========================================================")

# A B C D
# A B C
# A B
# A

for i in range(1,5) :
    for j in range(1, 6-i):
        print(chr(64+j), end =" ")
           
    print("")

print("=======================================6========================================================")

# *****
#  ***
#   *

row = 3
for i in range(1, row+1) :
  
    for j in range(1, i):
        print("", end=" ")

    for j in range(1, 2*(row-i)+2) :
        print("*", end="")

    print("") 



print("=======================================7========================================================")

# * * * * *
#  * * * *
#   * * *
#    * *
#     *
row = 5
for i in range(1, row+1) :
  
    for j in range(1, i):
        print("", end=" ")

    for j in range(1, (row-i)+2) :
        print("*", end=" ")

    print("") 