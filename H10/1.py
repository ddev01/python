teksts = "Hallo dit is een test met klinkers."
tela = 0
tele = 0
teli = 0
telo = 0
telu = 0

for x in teksts:
    if x.lower() == "a":
        tela += 1
    elif x.lower() == "e":
        tele += 1
    elif x.lower() == "i":
        teli += 1
    elif x.lower() == "o":
        telo += 1
    elif x.lower() == "u":
        telu += 1

print("A: ", tela, "E: ", tele, "I: ", teli, "O: ", telo, "U: ", telu)




