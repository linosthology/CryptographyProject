'''
elliptic curve
    takes the following parameters on instantiation
        p -> mod for F
        a, b -> weierstrass equation coefficients
        G -> Generator
        q -> |G|

    supports addition and duplication
        xTimesG
            takes an int
            returns the generator times the int
        xTimesPoint
            takes an int and a point
            returns the point times the int
'''

from extendedEuclidian import getInverse
from point import Point


def turnPositive(p, element):
    return p + element if element < 0 else element


class EllipticCurve:

    # constructor -> sets parameters for the curve
    def __init__(self, p: int, a: int, b: int, generatorX: int, generatorY: int, q: int):

        # mod of coordinates
        self.p = p

        # a coefficient of the curve
        self.a = a
        # b coefficient of the curve
        self.b = b

        # x of generator
        self.generatorX = generatorX
        # y of generator
        self.generatorY = generatorY

        # q of generator
        self.q = q

        # generator
        self.G = Point(self.generatorX, self.generatorY)

        if self.hasSinguarities():
            print("the elliptic curve has singularities!")

    def __repr__(self):

        return (f"\n\ny^2 = x^3 + {self.a}x + {self.b} over F_{self.p} with <G> =\n{self.G.__repr__()},\n\nwhere |G| = {self.q}\n\n")

        # pointAddition takes two points and returns their sum
    def pointAddition(self, P: Point, Q: Point) -> Point:
        # is one of them the point of infinity?
        if P.isPointOfInfinity() or Q.isPointOfInfinity():
            if P.isPointOfInfinity():
                return Q
            else:
                return P
        # are they identical? perform duplication
        elif P == Q:
            return self.pointDuplication(P)
        elif P.x == Q.x:
            return Point()
        else:
            # perform the addition
            divident = Q.y-P.y % self.p
            diviser = Q.x-P.x % self.p
            inverse = getInverse(self.p, diviser)
            gradient = divident*inverse % self.p

            x = turnPositive(
                self.p, ((gradient ** 2 % self.p) - P.x - Q.x) % self.p)
            y = turnPositive(self.p, ((gradient*(P.x-x)-P.y) % self.p))

            return Point(x, y)

    # pointDuplication takes the point it has to duplicate and computes the duplication on instantiation

    def pointDuplication(self, P: Point) -> Point:

        if P.isPointOfInfinity():
            return P
        elif P.y == 0:
            return Point()
        else:
            divident = (3*((P.x**2) % self.p) + self.a) % self.p
            diviser = 2 * P.y % self.p
            inverse = getInverse(self.p, diviser)
            gradient = divident*inverse % self.p

            x = turnPositive(
                self.p, ((gradient ** 2 % self.p) - P.x - P.x) % self.p)
            y = turnPositive(
                self.p, ((gradient*(P.x - x)-P.y) % self.p))

            return Point(x, y)

    def xTimesG(self, times) -> Point:

        if times == 1:
            return self.G

        Q = Point()
        N = self.G

        timesInBinary = (bin(times))[2:]

        for digit in reversed(timesInBinary):
            if digit == "1":
                Q = self.pointAddition(Q, N)
            N = self.pointDuplication(N)
        return Q

    def xTimesPoint(self, times, P: Point) -> Point:

        if times == 1:
            return P

        Q = Point()
        N = P

        timesInBinary = (bin(times))[2:]

        for digit in reversed(timesInBinary):
            if digit == "1":
                Q = self.pointAddition(Q, N)
            N = self.pointDuplication(N)
        return Q

    def hasSinguarities(self):
        return True if (4*self.a**3+27*self.b**2) % self.p == 0 else False
