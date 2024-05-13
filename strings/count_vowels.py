# find the no. of vowels in a string.

str = input("Enter a string : ") 
v_cnt = 0
for i in str :
    # 
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ) :
        v_cnt += 1
print(v_cnt)