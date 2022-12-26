#Suffix Array

string = 'AAAAA'
suffixes = []

for i in range(len(string)): #List of suffixes
    suffixes.append([string[i:], i])

suffixes.sort()

for suffix in suffixes:
    print(suffix[1])


###  

# update

###