import time
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

    # format computation times
    output = f"\n\nfor {n} computations it took:\n\ntimeECDH:\n{str(timeECDH)} seconds or\n{str(timeECDH/60)} minutes\nper addition: {str((timeECDH/n)*1000 )} miliseconds"

    # print out information about the computing time
    print(output)

    # seperator to better see where another entry starts
    seperator = "\n\n-----------------------------------------------"

    # insert output into file
    out_file = open("times.txt", "a+")
    out_file.write(
        output + seperator)
    out_file.close


out_file = open("times.txt", "a+")
out_file.flush()
out_file.close
for i in range(1, 2):
    timingComparison(i)
