cijfer = float(input("Cijfer: "))
cijfer = round(cijfer, 1)
print(cijfer)
if cijfer > 0 and cijfer <= 10:
    if cijfer >= 8.5:
        print("A")
    elif cijfer >= 7.5:
        print("B")
    elif cijfer >= 6.5:
        print("C")
    elif cijfer >= 5.5:
        print("D")
    elif cijfer <= 5:
        print("F")
else:
    print("Error: Type een nummer van 0 tot en met 10")
