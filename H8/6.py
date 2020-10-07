def bino(x):
    b = x
    for y in range ((x-1) ,0 , -1):
        b = y * x
        print(b)

bino(5)