pogingen = 0
min = 0
max = 1000
print( "kies een nummer 0- 1000 " )
while 1 > 0:
    pogingen += 1
    gok = int((min + max) / 2)
    print("Python gokt: ", gok, "Is it [H]oger, [L]ager of [G]oed?")
    answer = input("H, L or G: ")
    if answer == "H" or answer == "h":
        min = gok
    elif answer == "L" or answer == "l":
        max = gok
    elif answer == "G" or answer == "g":
        break
print(gok, "Is het antwoord. Het kostte: ", pogingen, "pogingen")