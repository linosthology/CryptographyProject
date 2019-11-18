from time import time
from ecdh import ECDH


def timingComparison(n):

    timeECDH: float

    # ECDH
    dh = ECDH()
    start_time = time()
    for x in range(0, n, 1):
        dh.computeKeys()
    timeECDH = (time() - start_time)

    # format computation times
    output = f", {n}, {str(timeECDH)}, {str(timeECDH/60)}, {str((timeECDH/n)*1000)}"

    # insert output into file
    out_file = open("times.csv", "a+")
    out_file.write(f"\n{output}")
    out_file.close()

    return output
