from brainpoolP160r1 import BrainpoolP160r1
from ecdh import ECDH
from random import randrange
from math import log
from point import Point


class ECMQV:
    def __init__(self):
        self.curve = BrainpoolP160r1()
        self.ecdh = ECDH()

    def computeKeys(self):

        # -----------------------------
        # ECDH -> Static Keys
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
        # Ephemeral Keys
        # -----------------------------

        qA = Point()

        while(qA.isPointOfInfinity()):

            # Alice
            b = randrange(1, self.curve.q)
            B = self.curve.xTimesG(a)

            # Bob
            d = randrange(1, self.curve.q)
            D = self.curve.xTimesG(b)

            # -----------------------------
            # MQV
            # -----------------------------

            # n = bitlength of q divided by 2
            n = int((len(bin(self.curve.q))-2)/2)

            # Alice

            uA = int((B.x % 2**n) + 2**n)

            sA = int((b + uA*a) % self.curve.q)

            vA = int((D.x % 2**n) + 2**n)

            qA = self.curve.xTimesPoint(
                sA, self.curve.pointAddition(D, self.curve.xTimesPoint(vA, C)))

            # Bob

            uB = int((D.x % 2**n) + 2**n)

            sB = int((d + uB*c) % self.curve.q)

            vB = int((B.x % 2**n) + 2**n)

            qB = self.curve.xTimesPoint(
                sB, self.curve.pointAddition(B, self.curve.xTimesPoint(vB, A)))

            print(qA)
            print(qB)
            print(qA == qB)

        return qA


test = ECMQV()
test.computeKeys()
