from os import listdir, getcwd

list = listdir( "." )
for name in flist:
    print( getcwd() + "/" + name )