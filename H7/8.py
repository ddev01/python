import random
x = 5
gok = 0
pogingen = 0
while gok != x:
    pogingen += 1
    gok = int(input("Gok: "))
    if gok > x:
        print("Je moet lager gokken")
    else:
        print("Je moet hoger gokken")
print("Het nummer was", x, "Je hebt er", pogingen, "pogingen over gedaan.")