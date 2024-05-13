# Make a loop from 99 to 4 and print numbers that are divisible by 5 and 7

for i in range (99, 3, -1) :
    # print(i)
    if (i%5 == 0 and i%7 == 0) :
        print(i, end = " ")
