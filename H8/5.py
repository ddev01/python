num = 0
def getNumber():
    while True:
        num = int(input("Nummer: "))
        if num < 0 or num > 1000:
            print( "Kies iets tussen 0-1000" )
            continue
        return num
print(getNumber())
##### niet af