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
print("==================================")
#write a program in python to calculate savings as:
#a person save 1rs on monday, 2 on tuesday, 3 on wednesday, 4 on thursday, 5 on friday and 6 on saturday and 7 on sunday.
# next week day savings  starts from 2 rs on Monday, and so on.
# calculate the total savings as per the days 

def calculate_total_savings(num_weeks):
    total_savings = 0
    day_savings = 1  # Initial savings for Monday
    for week in range(num_weeks):
        for day in range(7):
            total_savings += day_savings
            day_savings += 1
            if day_savings > 7:
                day_savings = 1  # Reset day savings to 1 for Monday
    return total_savings

num_weeks = int(input("Enter the number of weeks: "))
total = calculate_total_savings(num_weeks)
print("Total savings over {} weeks: {}".format(num_weeks, total))



    
