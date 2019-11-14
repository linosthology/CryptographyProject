import time
import ecCalcuations
import ecdh


def timingComparison(n):

    timeECDH: float
    # timeECMQV: float

    # ECDH
    dh = ecdh.ECDH()
    start_time = time.time()
    for x in range(0, n, 1):
        dh.computeKeys()
        timeECDH = (time.time() - start_time)

    # print out information about the computing time
    print("\ntimeECDH:\n" + str(timeECDH) + " seconds \n" + "per addition: " +
          str((timeECDH/n) * (10**9)) + " nanoseconds")


timingComparison(1000000)
