# 10 . List of athletes participated in 100m and 200m running race.
# a. hundred_meters = [‘Vikay’,’John’,’Kumar’,’Rajesh’,’Malar’,’Vaihai’]
# b. two_hundred_meters = [‘Vetry’,’Petter’,’Priyanka’,’Kumar’,’Malar’]

# Find the answer for below question from above lists (using set and Boolean Operators)
# a. Find the athletes who participated only in 100m race
# b. Find the athletes who participated only in 200m race
# c. Find the athletes who participated both 100m and 200m race
# d. Find the athletes who participated only one race


hundred_meters = ['Vikay','John','Kumar','Rajesh','Malar','Vaihai']
two_hundred_meters = ['Vetry','Petter','Priyanka','Kumar','Malar']

# for i in hundred_meters :
#     for j in two_hundred_meters :
#         if i not in j:
            

list = hundred_meters ^ two_hundred_meters
print(list)