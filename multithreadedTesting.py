from multiprocessing import Pool
from testing import timingComparison

if __name__ == '__main__':

    total = 0
    t = range(1, 1001)
    intList = []
    for x in t:
        intList.append(x)
        total += x

    out_file = open("ecTimes.csv", "w")
    out_file.write(
        f"Total Key Exchanges, How many Key Exchanges?, Overall Time (seconds), Overall Time (minutes), time per key exchange (miliseconds)\n{total}")
    out_file.close()

    out_file = open("mqvTimes.csv", "w")
    out_file.write(
        f"Total Key Exchanges, How many Key Exchanges?, Overall Time (seconds), Overall Time (minutes), time per key exchange (miliseconds)\n{total}")
    out_file.close()

   # how many threads does your cpu have?
    threads = 12

    p = Pool(threads)
    p.map(timingComparison, intList)
    p.close()
