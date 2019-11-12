# goals for a realistic approach on elliptic curve computations
#   use a standardized elliptic curve and don't compute all points
#       takes way too long
#   get a curve and its generator and be able
#   to compute points with the generator in a
#   effective way
#
# source for standardized curves
# https://tools.ietf.org/html/rfc5639
# in this script brainpoolP160r1 is used
#   p is the prime specifying the base field.
#   A and B are the coefficients of the equation y ^ 2 = x ^ 3 + A*x + B
#   mod p defining the elliptic curve.
#   G = (x, y) is the base point, i.e., a point in E of prime q,
#   with x and y being its x - and y-coordinates, respectively.
#   q is the prime q of the group generated by G.
#   h is the cofactor of G in E, i.e.,  # E(GF(p))/q.
#
#       p = E95E4A5F737059DC60DFC7AD95B3D8139515620F_16
#           1332297598440044874827085558802491743757193798159_10

#       A = 340E7BE2A280EB74E2BE61BADA745D97E8F7C300_16
#           297190522446607939568481567949428902921613329152_10

#       B = 1E589A8595423412134FAA2DBDEC95C8D8675E58_16
#           173245649450172891208247283053495198538671808088_10

#       x = BED5AF16EA3F6A4F62938C4631EB5AF7BDBCDBC3_16
#           1089473557631435284577962539738532515920566082499_10

#       y = 1667CB477A1A8EC338F94741669C976316DA6321_16
#           127912481829969033206777085249718746721365418785_10

#       q = E95E4A5F737059DC60DF5991D45029409E60FC09_16
#           1332297598440044874827085038830181364212942568457_10

#       h = 1

import extendedEuclidian
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def turnPositive(p, element):
    return p + element if element < 0 else element


class ellipticCurve:

    # constructor -> sets parameters for the curve
    def __init__(self):

        # mod of coordinates
        self.p = 1332297598440044874827085558802491743757193798159

        # a coefficient of the curve
        self.a = 297190522446607939568481567949428902921613329152
        # b coefficient of the curve
        self.b = 173245649450172891208247283053495198538671808088

        # x of generator
        self.generatorX = 1089473557631435284577962539738532515920566082499
        # y of generator
        self.generatorY = 127912481829969033206777085249718746721365418785

        # q of generator
        self.q = 1332297598440044874827085038830181364212942568457

        # generator
        self.G = Point(generatorX, generatorY)

    # pointAddition takes two points and returns their sum
    def pointAddition(self, P: Point, Q: Point) -> Point:
        # check whether addition is possible
        if P.x == Q.x:
            return Point(None, None)
        else:
            # perform the addition
            divident = Q.y-P.y % self.p
            diviser = Q.x-P.x % self.p
            inverse = extendedEuclidian.getInverse(self.p, diviser)
            gradient = divident*inverse % self.p
            x = turnPositive(self.p, (gradient ** 2 - P.x - Q.x) % self.p)
            y = turnPositive(self.p, ((gradient*(P.x-x)-P.y) % self.p))

            return Point(x, y)

    # pointDuplication takes the point it has to duplicate and computes the duplication on instantiation
    def pointDuplication(self, P: Point) -> Point:
        if P.y == 0:
            return Point(None, None)
        else:
            divident = (3*(P.x**2) + self.a) % self.p
            diviser = 2 * P.y % self.p
            inverse = extendedEuclidian.getInverse(self.p, diviser)
            gradient = divident*inverse % self.p
            x = turnPositive(
                self.p, (gradient ** 2 - P.x - P.x) % self.p)
            y = turnPositive(
                self.p, ((gradient*(P.x - x)-P.y) % self.p))

            return Point(x, y)

    def hasSinguarities(self):
        return True if (4*self.a**3+27*self.b**2) % self.p == 0 else False
