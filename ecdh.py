# Elliptic Curve Diffie Hellman

import random
import ecCalcuations

curve = ecCalcuations.EllipticCurve()

# Alice
a = random.randrange(1, curve.q)
# A

# Bob
b = random.randrange(1, curve.q)
