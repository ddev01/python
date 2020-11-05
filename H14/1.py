allthings = {"Socrates", "Plato", "Eratosthenes", "Zeus", "Hera", 
    "Athens", "Acropolis", "Cat", "Dog"}
men = {"Socrates", "Plato", "Eratosthenes"}
mortalthings = {"Socrates","Plato","Eratosthenes","Cat","Dog"}

print( men.issubset( mortalthings ) )
print( "Socrates" in men )
print( "Socrates" in mortalthings )
print( len( mortalthings.difference( men ) ) > 0 )
print( len( allthings.difference( mortalthings ) ) > 0 )