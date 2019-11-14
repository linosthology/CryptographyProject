# Ellipticself.curve Diffie Hellman

from random import randrange
from ecCalcuations import EllipticCurve


class ECDH:
    def __init__(self):
        self.curve = EllipticCurve()

    def computeKeys(self):
        # Alice
        a = randrange(1, self.curve.q)
        A = self.curve.xTimesG(a)

        # Bob
        b = randrange(1, self.curve.q)
        B = self.curve.xTimesG(b)

        # K's
        kA = self.curve.xTimesPoint(a, B)
        kB = self.curve.xTimesPoint(b, A)

        print("\n\na: ", a, "\n\nA: ", A, "\n\nb: ", b,
              "\n\nB: ", B, "\n\nkey Alice: ", kA, "\n\nkey Bob: ", kB)
