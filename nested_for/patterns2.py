# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1,5) :
    for j in range(1, i+1):
        print(j, end=" ")
    print("")

print("==================================================================")
# 1
# 2 3
# 4 5 6
# 7 8 9 10
cnt = 1
for i in range(1,5) :
    for j in range(1, i+1):
        print(cnt, end=" ")
        cnt+=1
    print("")


print("==================================================================")


# 10
# 9 8
# 7 6 5
# 4 3 2 1
cnt = 10
for i in range(1,5) :
    for j in range(1, i+1):
        print(cnt, end=" ")
        cnt-=1
    print("")

print("==================================================================")

# A 
# A B
# A B C 
# A B C D 

# alpha = chr(65) -> A
for i in range(1,5) :
    for j in range(1, i+1):
        print(chr(j+64), end =" ")
        
    print("")


print("==================================================================")

# A 
# B C 
# D E F 
# G H I J
count = 1
for i in range(1,5) :
    for j in range(1, i+1):
        print(chr(count+64), end =" ")
        count +=1
        
    print("")

print("==================================================================")

# Z 
# X V 
# T R P
# N L J H


# z = chr(90)
# print(z)
count = 90
for i in range(1,5) :
    for j in range(1, i+1):
        print(chr(count), end =" ")
        count -=2
        
    print("")


print("==================================================================")

# A 
# B C 
# D E F 
# G H I J
count = 1
n = 1
for i in range(1,5) :
    for j in range(1, i+1):
        print(str(n) + chr(count+96), end =" ")
        count +=1
        n+=1
    print("")

print("==================================================================")

# *
# * *
# *   *
# *     *
# * * * * *
row = 5
for i in range(1, row+1) :
    for j in range(1,row+1):
        if(j==1 or i==row or j==i) :
            print("*", end =" ")
        else :
            print(" ",end =" ")
                
    print("")