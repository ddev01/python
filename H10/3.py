a = "abcdefghijklmnopqrstuvwxyz"

for letter in a:
    print(letter, end="")

print()
for y in a:
    print(chr(ord(y) + 13), end="")

tekst = """
    Kapper
    Knap, de
    knappe
    kapper, knipt
    en
    kapt
    heel knap , maar de knecht van kapper Knap , de knappe kapper ,
    knipt en kapt nog knapper dan kapper Knap , de knappe kapper."""


def getKnap(a, y):
    b = a.split()
    counter = 0
    for x in b:
        if x.lower() == y:
            counter += 1
    print(counter)

getKnap(tekst, "knipt")


text = "Hello, world!"
newtext = ""
oba = """Hallo
dit
is
een test"""
print(oba)