# Q10 : Write a program to find the volume of the cylinder. Also find the cost when ,when the
# cost of 1 litre milk is 40Rs.


#vol = pi*r**2*h

# r = 2
# h = 5
r = int (input("Enter radius of the cylinder : "))
h = int (input("Enter height of the cylinder : "))
pi = 22/7

vol = pi * h * r**2

print("The volume of cylinder is ", format(vol, ".2f"))

# cost of 1 litre milk is Rs. 40
tot_cost = vol * 40

print("Total cost of milk in the cylinder is Rs.", format(tot_cost, ".2f"))


#output
# Enter radius of the cylinder : 2
# Enter height of the cylinder : 5
# The volume of cylinder is  62.86
# Total cost of milk in the cylinder is Rs. 2514.29