

state = "RAJASTHAN"
# R A J A S T H A N
# 0 1 2 3 4 5 6 7 8
#


print(state[0])   ##R
print(state[5])  ##T
print(state[-1])  ##N
print(state[-7])  ##J



#slicing

state = "RAJASTHAN"
# R A J A S T H A N
# 0 1 2 3 4 5 6 7 8
#

print(state[0:4]) #RAJA

print(state[0:4:1]) #RAJA

print(state[1:6:3]) #AS

print(state[ 1: : 5]) #AH

print(state[0::2]) #RJSHN

print(state[0:4:-1]) ## NO OUTPUT

print(state[-1:-4:])  # NO OUTPUT

print(state[-1:-4:-1])  # NO OUTPUT

print(state[0:-6:])  # NO OUTPUT


