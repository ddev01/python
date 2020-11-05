def Tafel():
    a = int(input('Vul een nummer in: '))
    counter = 1
    for i in range(1, 11):
        print(counter*a)
        counter+= 1
Tafel()
