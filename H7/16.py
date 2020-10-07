from random import randint
dagen = 0
instadeath = 0
death = 0
mieren = 100000
for x in range (0, mieren):
    if randint(1, 3) == 1:
        instadeath += 1
    else:
        dagen += 1
        while True:
            if randint(1, 2) == 2:
                dagen += 1
            else:
                break
print("Gemiddeld: ", dagen/mieren)