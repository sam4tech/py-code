# Take a string from user and check according to the below conditions :
# 1. string must have 3 capital letters. 
# 2. string must have 3 small letters.
# 3. string must have a number.
# 4. string must have a minimum length between 5 and 15.
# 5. string must have only one of these #, @, !



s = input("Enter your password : ")
# s = "SMRiti31#"

lower, upper, special, count = 0, 0, 0, 0
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="#@!"
digits="0123456789"
if ( 5<=len(s)<= 15) :
    for i in s:
 
         # counting uppercase alphabets
        if (i in capitalalphabets):
            upper+=1 

        # counting lowercase alphabets
        if (i in smallalphabets):
            lower+=1           
   
         # counting digits
        if (i in digits):
            count+=1           
 
        # counting the mentioned special characters
        if(i in specialchar):
            special+=1  
                 
if (lower>=2 and upper>=3 and special>=1 and count>=1 and lower+special+upper+count==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")