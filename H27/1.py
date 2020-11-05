from collections import Counter

zin = "Dit is een test zin om te zien welk letter het meest voorkomt"
zin2 = ""
for char in zin.lower():
    if char >= 'a' and char <= 'z':
        zin2 += char

counted = Counter( zin2 ).most_common( 5 )
for char in counted:
    print( "{}: {}".format( char[0], char[1] ) )