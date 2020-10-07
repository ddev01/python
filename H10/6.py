zin = "en zo gebeurde het dat dat onze toevallige ontmoeting \
met de EErwaarde aRTHUR BElling een ommekeer betekende in ons \
leven , en vanaf dat moment gingen we iedere zondag naar \
de kerk van Sint sIMPEL bij Roombroodje MEt Jam."

zinh = zin[0].upper() + zin[1:]
zinsplit = zinh.split()
lastw = ""
newz = ""
newz2 = ""
newz3 = ""
newz4 = ""
#Dubbele woorden vervangen.
for woord in zinsplit:
    currrentword = woord
    if currrentword == lastw:
        continue
    else:
        newz += currrentword + " "
    lastw = woord

#2 Eerste 2 hoofdletters vervangen.
for woord in newz.split():
    if len(woord) <= 2:
        newz2 += woord + " "
        continue
    elif woord[0] == woord[0].upper() and woord[1] == woord[1].upper() and woord[2] == woord[2].lower():
        newz2 += woord[0].upper() + woord[1:].lower() + " "
    else:
        newz2 += woord + " "

# 1e kleine letter, rest hoofdletter vervangen.
for woord in newz2.split():
    if woord[0] == woord[0].lower() and woord[1:] == woord[1:].upper():
        newz3 += woord[0].upper() + woord[1:].lower() + " "
    else:
        newz3 += woord + " "
#Hoofdletter voor dagen.
for woord in newz3.split():
    dagen = "maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"
    if woord.lower() in dagen:
        newz4 += woord.title() + " "
    else:
        newz4 += woord + " "
