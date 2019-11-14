from random import randrange
from math import log
from ecCalcuations import EllipticCurve
from ecdh import ECDH


class ECMQV:
    def __init__(self):
        self.curve = EllipticCurve()
        self.ecdh = ECDH()

    def computeKeys(self):

        # get ECDH parameters
        ecdhParas = self.ecdh.computeKeys()

        # Alice
        a = ecdhParas[1]
        print(a)
        A = ecdhParas[2]

        # Bob
        b = ecdhParas[3]
        B = ecdhParas[4]

        # sharedKey
        K = ecdhParas[5]

        # -----------------------------
        # start of actual ECMQV
        # -----------------------------

        # Alice
        x = randrange(1, self.curve.q)
        X = self.curve.xTimesG(a)

        # Bob
        y = randrange(1, self.curve.q)
        Y = self.curve.xTimesG(b)

        # n = bitlength of q divided by 2
        n = int((len(bin(self.curve.q)[2:]))/2)

        d = self.curve.xTimesPoint(
            int(2**n), self.curve.xTimesG(int(x % 2**n)))
        d = self.curve.xTimesPoint(
            2**n, self.curve.xTimesG(int(y % 2**n)))

        # Alice
        sigmaA = self.curve.xTimesPoint(
            (x+d*a), self.curve.pointAddition(self.curve.xTimesPoint(e, B), Y))

        # Bob
        sigmaB = self.curve.xTimesPoint(
            (y+e*b), self.curve.pointAddition(self.curve.xTimesPoint(d, A), X))

        print(sigmaA)
        print(sigmaB)
        print(sigmaA == sigmaB)


ecmqv = ECMQV()
ecmqv.computeKeys()
