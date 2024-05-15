mydict = {10: 'yash', 20 : 'sam'}

print(mydict)

print(mydict[10])





str = "hello sam"
c = 0
for char in str :
    if(char is not " ") :
        print(char)
        c+=1

print(c)



######


string = "hey hello tushar"
# cnt = 0
dict = { 'char': 0}
for char in string :
    # if (char =='a' or char =='e' or char =='i' or char =='o'  or char =='u'):
    if char in 'aeiou' :

        if char not in dict :
            dict[char] = 1
        else :
            dict[char] = dict[char] + 1

print(dict)


    
