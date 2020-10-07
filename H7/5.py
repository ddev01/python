x = 1
y = 1
print(x, y)
while x+y < 1000:
    y = x + y
    print(y)
    x = x + y
    print(x)
print(x + y)