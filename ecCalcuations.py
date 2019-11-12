#!/usr/bin/env python3

# with this script you can compute all the points of an elliptic curve and its order.
# you can also compute point addition or duplication
# with timing comparison you can compare the computing times between point duplication and addition
#
# on input it takes the modulus p, a and b of the curve
# python ellipticCurveGroupOperations p a b
#
# optionally you can input either one point for point duplication
# python ellipticCurveGroupOperations p a b x y
# or two points for point addition
# python ellipticCurveGroupOperations p a b x1 y1 x2 y2
#
#
# new goals for a more realistic approach
#   use a standardized elliptic curve and don't compute all points
#       takes way too long
#   get a curve and its generator and be able
#   to compute points with the generator in a
#   effective way
# source for standardized curves
# https://tools.ietf.org/html/rfc5639
# in this script brainpoolP160r1 is used

import extendedEuclidian
import time
import random


class ellipticCurve:
    def __init__(self, p, a, b, G):
        p = p
        a = a
        b = b
        calculateOrder()

    # function for calculating the order of the curve
    def calculateOrder(self):
        points = []
        possibleYs = []

        # get all possible y values
        for x in range(0, p, 1):
            possibleYs.append((x*x) % p)

        # check if y values exist for current x
        for x in range(0, p, 1):
            fX = (x ** 3 + a * x + b) % p
            for i in range(len(possibleYs)):
                if possibleYs[i] == fX:
                    y = i

                    # if point exists, add it to the curves points
                    points.append((x, y))

        # set the order of the group after computing all the points
        order = len(points) + 1

    # getInfo prints out information about the curve in the terminal
    def getInfo(self):
        print(
            f"\nthe given elliptic curve\ny^2 = x^3 + {a}x + {b} mod {p} has these points:\n\n{points} and the point of infinity\n\nand an order of {len(points)}\n")

    # pointAddition takes a two Points and calculates the addition of those on instantiation
    def pointAddition(P, Q):
        gradient: int

        # check whether addition is possible
        if P == Q:
            print(
                "you can't do addition with the same point, you need to perform point duplication")
        else:
            isPointOfInfinity = False
            if P[0] == Q[0]:
                isPointOfInfinity = True
            else:

                # perform the addition
                divident = turnPositive(curve.p, Q[1]-P[1] % curve.p)
                diviser = Q[0]-P[0] % curve.p
                inverse = extendedEuclidian.getInverse(curve.p, diviser)
                gradient = divident*inverse % curve.p
                x = (gradient ** 2 - P[0] - Q[0]) % curve.p
                y = turnPositive(
                    curve.p, ((gradient*(P[0]-x)-P[1]) % curve.p))
            # print out the new point
            if isPointOfInfinity:
                print(f"\n{P} + {P} is the point of infinity!")
            else:
                print(f"\n{P} + {Q} is ({x}, {y})!")

    # pointDuplication takes the point it has to duplicate and computes the duplication on instantiation
    def pointDuplication(P):
        isPointOfInfinity = False
        if P[1] == 0:
            isPointOfInfinity = True
        else:
            gradient: int
            divident = (3*(P[0]**2) + curve.a) % curve.p
            diviser = 2 * P[1] % curve.p
            inverse = extendedEuclidian.getInverse(curve.p, diviser)
            gradient = divident*inverse % curve.p
            x = turnPositive(
                curve.p, (gradient ** 2 - P[0] - P[0]) % curve.p)
            y = turnPositive(
                curve.p, ((gradient*(P[0]-x)-P[1]) % curve.p))
        # print out the new point
        if isPointOfInfinity:
            print(f"\n{P} + {P} is the point of infinity!")
        else:
            print(f"\n{P} + {P} is ({x}, {y})!")

    def pointExists(x, y):
        givenPoint = (x, y)
        isPoint = False
        for point in curve.points:
            if givenPoint == point:
                isPoint = True
        return isPoint


def hasSinguarities(p, a, b):
    return True if (4*a**3+27*self.b**2) % p == 0 else False


def turnPositive(p, element):
    return p + element if element < 0 else element
