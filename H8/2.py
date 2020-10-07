def strings (x, y):
    z = ""
    for letter in x:
        if letter in y and letter not in z:
            z += letter
            return z
w1 = input("Geef een woord: ")
w2 = input("Geef een woord: ")
test = strings(w1, w2)
print(test)
print("Overeenkomsten : ", len(test))