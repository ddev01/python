zin = "Dit is de zin waarvan ik de klinkers ga tellen"
klinkers = ""
for char in zin.lower():
    if char in  ('a', 'e', 'i', 'o', 'u'):
        klinkers += char
if len(klinkers) == 1:
    print('De string heeft 1 klinker')
else:
    print('De string heeft:',len(klinkers),'klinkers.')