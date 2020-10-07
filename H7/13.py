from random import randint
pogingen = 1000
steen = 5
w = 0
for x in range(pogingen):
    z = 0
    for y in range(steen):
        rol = randint( 1, 6 )
        if rol < z:
            break
        z = rol
    else:
        w += 1
print( "Kans: {:.3f}".format( w/pogingen ) )