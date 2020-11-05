import os
import os.path
#16.1:
openit = open("pc_woodchuck.txt")
readden = openit.readlines()
listed = []
counts = dict()
for woord in readden:
    x = woord.split()
    for woord in x:
        listed.append(woord)
for word in listed:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
