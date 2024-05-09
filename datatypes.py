x = 20
print(id(x))
y = x
print(id(y))
y = 25
print(id(y), id(x))

#Python follows Call by object reference