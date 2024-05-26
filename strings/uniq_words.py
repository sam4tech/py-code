str = "hey tushar hello aman hey naina tushar"
words = {}
print(str.split())

list = str.split()

for i in list :
    if (i not in words) :
        words[i] = 1
    else :
        words[i] = words[i] + 1

print(words)
    

#output

{'hey': 2, 'tushar': 2, 'hello': 1, 'aman': 1, 'naina': 1}
    


