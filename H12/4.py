zin = 'Dit is de zin waarvan ik ga tellen hoe vaak elke letter voorkomt in de zin.'
zin2 = zin.lower()
checked = []
for char in zin2:
    if char >= 'a' and char <= 'z':
        if char not in checked:
            checked.append(char)
            print(char, 'komt', zin2.count(char), 'keer voor.')
print(checked)