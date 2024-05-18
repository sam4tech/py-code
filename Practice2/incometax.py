# 1. Calculate income tax for the given income by adhering to the below rules
# a. first 10k => 0%
# b. second 10 => 10%
# c. Remaining => 20%
# d. For example, suppose the taxable income is 45000 the income tax payable is
# $6000


total_income = int(input("What's your annual income?\n>>> "))

if total_income <= 10000 :
    print("No tax applicable. ")
elif total_income <= 20000 :
    amount = total_income - 10000
    tax = (amount * 10) / 100
    print(tax)
else :
    amount = total_income - 20000
    tax = (amount * 20) / 100  + (10000 * 10) / 100
    print(tax)


##output

# What's your annual income?
# >>> 45000
# 6000.0