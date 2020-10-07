klinkers = 0
zin = input("Schrijf een zin: ")
if "a" in zin:
    klinkers += 1
if "e" in zin:
    klinkers += 1
if "i" in zin:
    klinkers += 1
if "o" in zin:
    klinkers += 1
if "u" in zin:
    klinkers += 1
if klinkers == 0:
    print("Er zitten geen klinkers in de zin")
else:
    print("Er zitten", klinkers, "klinkers in de zin")