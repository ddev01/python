y = ["Ochtend", "Middag", "Avond"]
while True:
    print("Current queue: ", y)
    x = input("Voeg iets toe aan de queue, ? popt en enter breakt: ")
    if x == "":
        break
    if x == "?":
        print("Verwijderd van queu: ", y.pop(0))

    else:
        y.append(x)