def msg(name) :
    print("hello " + name)


msg("sam")


# def prime(x) :
#     for i in range (1, x) :
#         if(x%i == 0) :
#             print("not prime")
#         else :
#             print('prime')
# prime (12)

print("==============================")



# def pattern (x) :
#     cnt = x
#     a = int(10)
#     for i in range (1, 4) :
#         for j in range(i, 4) :
#             print (chr(cnt+64) + (a+10) , end =" ")
#             cnt+=1
#             a+=1
#         print(" ")
        

# pattern (4)

print("===============================================")
#  find LCM

# x=3
# y=10
def lcm(x, y):

    if (x<y) :
        max = y 
    else :
        max = x

    while(True) :

        if (max%x==0 and max%y==0) :
            print("lcm : ", max)
            break
        max +=1
        


lcm(3,10)



#hcf

# x=3
# y=10
def hcf(x, y):

    if (x<y) :
        min = x
    else :
        min = y

    while(True) :

        if (x%min==0 and y%min==0) :
            print("hcf : ", min)
            break
        min -=1
        


hcf(21,49)