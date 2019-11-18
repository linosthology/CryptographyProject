from multiprocessing import Pool
from computationTimes import timingComparison

if __name__ == '__main__':

    t = range(100, 200)
    intList = []
    for x in t:
        intList.append(x)

    out_file = open("times.txt", "w")
    out_file.writelines("")
    out_file.close

   # how many threads does your cpu have?
    threads = 12

    p = Pool(threads)
    p.map(timingComparison, intList)
    p.close()
