x = str(input("Woord: "))
y = str(input("woord: "))
z = ""
for letter in x:
    if (letter in y) and (letter not in z):
        z += letter
if z == "":
    print( "Geen overeenkomsten" )
else:
    print( "Result: ", z )