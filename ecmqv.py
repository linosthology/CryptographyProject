from brainpoolP160r1 import BrainpoolP160r1
from random import randrange
from point import Point


class ECMQV:
    def __init__(self):
        self.curve = BrainpoolP160r1()

    def computeKeys(self):

        # -----------------------------
        # Static Keys
        # -----------------------------

        # Alice
        a = randrange(1, self.curve.q)
        A = self.curve.xTimesG(a)

        # Bob
        c = randrange(1, self.curve.q)
        C = self.curve.xTimesG(c)

        qA = Point()

        while(qA.isPointOfInfinity()):

            # -----------------------------
            # Ephemeral Keys
            # -----------------------------

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

        return qA
