from random import randrange
from math import log
from ecCalcuations import EllipticCurve
from ecdh import ECDH


class ECMQV:
    def __init__(self):
        self.curve = EllipticCurve()
        self.ecdh = ECDH()

    def computeKeys(self):

        # -----------------------------
        # static keys
        # -----------------------------

        # get ECDH parameters
        ecdhParas = self.ecdh.computeKeys()

        # Alice
        a = ecdhParas[1]
        A = ecdhParas[2]

        # Bob
        c = ecdhParas[3]
        C = ecdhParas[4]

        # sharedKey
        K = ecdhParas[5]

        # -----------------------------
        # ephemeral keys
        # -----------------------------

        # Alice
        b = randrange(1, self.curve.q)
        B = self.curve.xTimesG(a)

        # Bob
        d = randrange(1, self.curve.q)
        D = self.curve.xTimesG(b)

        # n = bitlength of q divided by 2
        n = log(self.curve.q, 2)/2

        x = randrange(1, self.curve.q)

    def computeQ(self, x, staticPublicSelf, staticPublicOther, ephemeralPublicSelf, ephemeralPublicOther, staticPrivate, ephemeralPrivate):
        # HOW POINT MOD 2^n
        u = (self.curve.xTimesPoint(x, ephemeralPublicSelf))


ecmqv = ECMQV()
ecmqv.computeKeys()
