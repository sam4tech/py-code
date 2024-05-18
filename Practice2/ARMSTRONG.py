# 13. Print all the armstrong numbers in the range of 100 to 1000
# a. Output : 153, 370,371,407

# num = int(input("Enter the number : \n >>> "))
# temp = num

start = 100
end = 1000
for num in range (start, end+1) :
    temp = num
    size = len(str(num))
    sum = 0
    
    while temp > 0 :
        sum = sum + ((temp % 10)**size)
        temp = temp//10

    # print("original number : ", temp)
    # print("Sum of numbers : ", sum)


    if num == sum :
        print("Armstrong : ", num)
       
    # # else :
    #     print("Number is NOT Armstrong.")


