for i in range(1,5) :
    # print("*", end=" ")
    for j in range(1,5):
        print("*", end=" ")
    print("")


print("\n\n\n")
# triangle pattern
# *
# * *
# * * *
# * * * *

for i in range(1,5) :
    # print("*", end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print("")



# 1 1 1 1
# 2 2 2 2
# 3 3 3 3 
# 4 4 4 4
print("\n\n\n")

for i in range(1,5) :
    # print("*", end=" ")
    for j in range(1,5):
        print(i, end=" ")
    print("")


# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
print("\n\n\n")

for i in range(1,5) :
    # print("*", end=" ")
    for j in range(1,5):
        print(j, end=" ")
    print("")



# 4 3 2 1
# 4 3 2 1
# 4 3 2 1
# 4 3 2 1

print("\n\n\n")

for i in range(1,5) :
    # print("*", end=" ")
    for j in range(4,0, -1):
        print(j, end=" ")
    print("")



# 100 101 102
# 100 101 102
# 100 101 102

print("\n\n\n")

for i in range(100,103) :
    # print("*", end=" ")
    for j in range(100,103):
        print(j, end=" ")
     
    print("")

print("\n\n\n")

# * * * *
# * * *
# * *
# * 
for i in range(1,5) :
    # print("*", end=" ")
    # for j in range(4,i-1, -1):
    for j in range(i,5):
        print("*", end=" ")
    print("")


print("============================================================")

#   $ $ $ *   
#   $ $ * *
#   $ * * *
#   * * * *
for i in range(1,5) :
    for j in range(i,4):
        print("$", end=" ")
    for k in range(1,i+1):
        print("*", end=" ")
    print("")

# or
row = 5
for i in range(1,row+1) :
    for j in range(i,row):
        print("$", end=" ")
    for k in range(1,i+1):
        print("*", end=" ")
    print("")

