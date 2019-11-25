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
        qB = Point()

        while(qA.isPointOfInfinity() or qB.isPointOfInfinity() or qA != qB):

            # Alice
            b = randrange(1, self.curve.q)
            B = self.curve.xTimesG(b)

            # Bob
            d = randrange(1, self.curve.q)
            D = self.curve.xTimesG(d)

            # -----------------------------
            # MQV
            # -----------------------------

            # n = bitlength of q divided by 2
            n = int((len(bin(self.curve.q))-2)/2)

            # Alice

            uA = (B.x % 2**n) + 2**n

            sA = (b + uA*a) % self.curve.q

            vA = (D.x % 2**n) + 2**n

            qA = self.curve.xTimesPoint(
                sA, self.curve.pointAddition(D, self.curve.xTimesPoint(vA, C)))

            # Bob

            uB = (D.x % 2**n) + 2**n

            sB = (d + uB*c) % self.curve.q

            vB = (B.x % 2**n) + 2**n

            qB = self.curve.xTimesPoint(
                sB, self.curve.pointAddition(B, self.curve.xTimesPoint(vB, A)))

            if(qA == qB):
                print("\n\nthey are the same:" + str(qA == qB) + "\n\n")
            elif qA.isPointOfInfinity() and qB.isPointOfInfinity():
                print("both poi")
            elif qA.isPointOfInfinity():
                print("qA is poi")
            elif qB.isPointOfInfinity():
                print("qB is poi")
            else:
                print("nothing works")

        return qA


test = ECMQV()
test.computeKeys()
