# for(start_value_included, last_value_excluded)
for i in range(1, 6) :
    print(i) #1.2.3.4.5

print('\nNew task....')

# for(start_value_included, last_value_excluded, step_value)
for j in range(1,10,3) :
    print(j) #1,4,7
print("\n")

for j in range(10 , 4, -1) :
    print(j) #1,4,7
print("\n")

sum=0
for j in range(1,11) :
    sum = sum+j
    print(j) #1......10
print("\n")
print(sum) #55


#for loop in STring data
for j in "Hello" :
    print(j) #1......10
print("\n")




#for loop in string vertically
a = "sam"
for i in a :
    print(i)
    
#for loop in string horizontally
print("\n")
a = "sam"
for i in a :
    print(i, end=" ")


print("\n")

#len method
data = "Mountain"
print(len(data))

for index in range(0,8) :
    print(index, data, data[index])