from time import time
from ecdh import ECDH
from ecmqv import ECMQV


def timingComparison(n):

    timeECDH: float
    timeMQV: float

    # ECDH
    dh = ECDH()
    mqv = ECMQV()

    start_time = time()
    for x in range(0, n, 1):
        dh.computeKeys()
    timeECDH = (time() - start_time)

    # format computation times
    output = f", {n}, {str(timeECDH)}, {str(timeECDH/60)}, {str((timeECDH/n)*1000)}"

    # insert output into file
    out_file = open("ecTimes.csv", "a+")
    out_file.write(f"\n{output}")
    out_file.close()

    start_time = time()
    for x in range(0, n, 1):
        if x == 0:
            mqv.computeStaticKeys()
        mqv.computeSessionKeys()
    timeMQV = (time() - start_time)

    # format computation times
    output = f", {n}, {str(timeMQV)}, {str(timeMQV/60)}, {str((timeMQV/n)*1000)}"

    # insert output into file
    out_file = open("mqvTimes.csv", "a+")
    out_file.write(f"\n{output}")
    out_file.close()

    return output
