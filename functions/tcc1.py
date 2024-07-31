# Question1 :  write a program to create a function show_emp() using conditions :

# 1. It should accept the employees name and salary and display both.
# 2. If the salary is missing in the function call, then assign default value of 10k to salary.


# def show_emp(emp_name, salary):
#     if (salary == "") :
#         salary = 10000
#     print ("Employee name : ", emp_name)
#     print ("Employee salary : ", salary)

# e_name = input("Enter employee name :")
# e_sal = input("Enter employee salary :")
# show_emp(e_name, e_sal)

# Question2 : Create an inner function to calculate the addition
# 1. Create an outer function that accepts 2 parameters a, b.
# 2  Create an inner function inside the outer one that calc addition of a and b .
# 3. At last, the outer function will add 5 to the additon and return it.

def outer_fn(a, b) :
    print(a,b)
    def inner_fn(a,b) :
        sum = a + b
        return sum
    result = inner_fn(a,b) + 5
    print ("Result = ", result)
    return result

x = outer_fn(2,5)
print (x)

