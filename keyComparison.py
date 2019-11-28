from ecdh import ECDH
from ecmqv import ECMQV
from point import Point

ecdhKey = Point()
ecmqvKey = Point()
ecdh = ECDH()
ecmqv = ECMQV()

while(ecdhKey.isPointOfInfinity() or ecdhKey != ecmqvKey or ecmqvKey.isPointOfInfinity()):
    ecdhKey = ecdh.computeKeys()
    ecmqvKey = ecmqv.computeKeys()

print(ecdhKey, ecmqvKey)

# ecdhKey = bin(ecdhKey)[2:]
# ecmqvKey = bin(ecmqvKey)[2:]
# print(len(ecdhKey), len(ecmqvKey))
