# build a class to represent a point in 2-d space
# it should be able to respond with a pretty printout
# we should be able to change x and y by any numeric amount
# Static members and methods should expose a count of how many points we have

class Point: # Python 2 MUST have the brackets i.e. class Point(object):
    #static members of this class
    points = 0
    # static methods
    @staticmethod
    def how_many_points(): # NB no 'self'
        return Point.points
    def __init__(self, x=0, y=0):
        self.x = x # these are instance properties, not static properties
        self.y = y
        # we should increment the couht of how many points
        Point.points += 1
    def __str__(self): # override the print feature
        return (f'Point is at x:{self.x} y:{self.y}')
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    p1 = Point(5, 7)
    p2 = Point(15, 17)
    p3 = Point()
    p1.move_by(1,1)
    print(p1)
    print(Point.how_many_points())
    p2.move_by(10,-10)
    print(p2)
    p3.move_by(99,-1)
    print(p3)
    