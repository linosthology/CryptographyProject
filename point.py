class Point:

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __repr__(self):
        return (f"\nPoint:\nx = {self.x}\ny = {self.y}")

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def isPointOfInfinity(self):
        return (self.x == None or self.y == None)
