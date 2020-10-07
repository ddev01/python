def gekkigheid (a):
    b = 0
    count = -1
    for i in range (1, (a+1)):
        count += 2
        b += 1 / count
        count += 2
        b -= 1 / count
    return 4 * b
print(gekkigheid(10))