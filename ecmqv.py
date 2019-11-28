from brainpoolP160r1 import BrainpoolP160r1
from random import randrange
from point import Point


class ECMQV:
    def __init__(self):
        self.curve = BrainpoolP160r1()

    def computeStaticKeys(self):

        # -----------------------------
        # Static Keys
        # -----------------------------

        # Alice
        self.a = randrange(1, self.curve.q)
        self.A = self.curve.xTimesG(self.a)

        # Bob
        self.c = randrange(1, self.curve.q)
        self.C = self.curve.xTimesG(self.c)

    def computeSessionKeys(self):

        if not hasattr(self, "a"):
            return print(
                "\n\nyou need to create static keys first!\nuse the function computeStaticKeys for that\n\n")

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

            sA = (b + uA * self.a) % self.curve.q

            vA = (D.x % 2**n) + 2**n

            qA = self.curve.xTimesPoint(
                sA, self.curve.pointAddition(D, self.curve.xTimesPoint(vA, self.C)))

            # Bob

            uB = (D.x % 2**n) + 2**n

            sB = (d + uB*self.c) % self.curve.q

            vB = (B.x % 2**n) + 2**n

            qB = self.curve.xTimesPoint(
                sB, self.curve.pointAddition(B, self.curve.xTimesPoint(vB, self.A)))

        return qA
