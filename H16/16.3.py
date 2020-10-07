import os
from os.path import isfile
countread = 0
countwrite = 0
read = open("pc_woodchuck.txt")
def removeKlinker(zin):
    newzin = ""
    for letter in zin:
        if letter not in "aeiouAEIOU":
            newzin += letter
    return newzin

writeCopy = open("makenewfile.txt", "w")
while True:
    temp = read.readline()
    countread += len(temp)
    if temp == "":
        break
    writeCopy.write(removeKlinker(temp))
    countwrite += len(removeKlinker(temp))
read.close()
writeCopy.close()
saus = open("makenewfile.txt")
print(saus.readlines())
print(countread)
print(countwrite)