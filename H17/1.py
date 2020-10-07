numlist = [ 100, 101, 0, "103", 104 ]
try:
    i1 = int( input( "Geef een index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ZeroDivisionError:
    print("Je kan niet delen door 0!!!")
except IndexError:
    print("Die index bestaat helemaal niet!!")
except ValueError:
    print("Dat was geen integer >:(")
except TypeError:
    print("Dit is geen int, float of een tekst")
except:
    print("er klopt iets niet")
