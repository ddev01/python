from copy import copy
class Point:
    def __init__( self , x=0.0 , y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rechthoek:
    def __init__( self , point , width , height ):
        self.point = copy( point )
        self.width = width
        self.height = height
    def __repr__( self ):
        return "[{},b={},h={}]".format( self.point , self.width , self.height )
    def getbotright(self):
        return Point(self.point.x + self.width, self.point.y)
    def getoppervlak(self):
        return

p = Point( 0.0, 0.0 )
r = Rechthoek( p, 6.0, 6.0 )
print(r.getbotright())


p2 = Point( 3.0, 3.0 )
r2 = Rechthoek( p2, 6.0, 6.0 )
print( r )
print(r2)
