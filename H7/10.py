priem = 6
tries = 0
for x in range(2, priem):
    tries += 1
    if priem % x == 0:
        print("Het is geen priem")
        break
if tries == priem - 2:
    print("Het is een priem!")