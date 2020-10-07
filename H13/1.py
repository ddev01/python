tekst = "Kapper Knap , de knappe kapper , knipt en kapt heel knap , maar de knecht van kapper Knap , maar de knecht van kapper Knap , maar de knecht van kapper Knap , de knappe kapper , knipt en kapt nog knapper dan kapper Knap , de knappe kapper."
tekst = tekst.lower()
dict = {}
splitted = tekst.split(",")
for woord in splitted:
    dict[woord] = tekst.count(woord)
print( dict)
volg = list(dict.keys())
print(volg)
volg.sort()
for key in volg:
    print("{}: {}".format(key, dict[key]))

