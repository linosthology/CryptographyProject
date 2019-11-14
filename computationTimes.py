from time import time
from ecdh import ECDH


def timingComparison(n):

    timeECDH: float
    # timeECMQV: float

    # ECDH
    dh = ecdh.ECDH()
    start_time = time.time()
    for x in range(0, n, 1):
        dh.computeKeys()
        timeECDH = (time.time() - start_time)

    # format computation times
    output = f"\n\nfor {n} computations it took:\n\ntimeECDH:\n  totalTime:\n      in seconds:\t{str(timeECDH)}\n      in minutes:\t{str(timeECDH/60)}\n  per addition:\n      miliseconds:\t{str((timeECDH/n)*1000 )}"

    # print out information about the computing time
    print(output)

    # seperator to better see where another entry starts
    seperator = "\n\n-----------------------------------------------"

    # insert output into file
    out_file = open("times.txt", "a+")
    out_file.write(
        output + seperator)
    out_file.close


out_file = open("times.txt", "w")
out_file.writelines("")
out_file.close
for i in range(1, 2):
    timingComparison(i)
