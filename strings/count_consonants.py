# find the no. of consonants in a string.

str = input("Enter a string : ") 
cons_cnt = 0
for i in str :
    #print(i)
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i== 'u' ) :
        cons_cnt += 0
    else :
        cons_cnt += 1

print("Count of consonants in the string : ", cons_cnt)