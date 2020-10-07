#12.5 niet af
gek = list(range(1, 101))
for nummer in gek:
    for x in range(2, nummer):
        if nummer % x == 0:
            gek.remove(nummer)
        else:
            print(nummer, "Is een priem")