class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, point, width, height ):
        self.point = point
        self.width = width
        self.height = height
    def __repr__( self ):
        if self.width >= 0 and self.height >= 0:
                return "[{},w={},h={}]".format( self.point, self.width, self.height )
        else:
                return "Error, negative values"

p = Point( 3.5, 5.0 )
print(p)
print(type(p))
r = Rectangle( p, 4.0, 2.0 )
print( r )

p.x = 1.0
p.y = 1.0
print( r )