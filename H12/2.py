soort = ["Harten", "Schoppen", "Klaveren", "Ruiten"]
waarde = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas"]
alles = []
for waardes in waarde:
    for soorten in soort:
        print(waardes + " " + soorten)
        alles.append((waardes + " " + soorten))
print("Origineel: ", alles)
random.shuffle(alles)
print("Shuffle:", alles)