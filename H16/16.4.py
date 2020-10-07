wood = open("pc_woodchuck.txt")
rose = open("pc_rose.txt")
jabb = open("pc_jabberwocky.txt")
woodwords = []
def clean(x):
    cleaned = ""
    for letter in x:
        if letter.lower() >= "a" and letter.lower() <= "z" or letter == " ":
            cleaned += letter
    return cleaned
while True:
    test = wood.readline()
    if test == "":
        break
    for woord in test.split():
        cleaned = clean(woord)
        print(cleaned)
        if len(cleaned) >= 3:
            woodwords += cleaned
print(woodwords)