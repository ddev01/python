max = None
min = None
divideby3 = 0
for y in range (1, 11):
    number = int(input("Enter a number: "))
    if max is None:
        max = number
    if min is None:
        min = number
    if number > max:
        max = number
        if number % 3 == 0:
            divideby3 += 1
    elif number < min:
        min = number
    elif number & 3 == 0:
        divideby3 += 1
print(max, min, divideby3)