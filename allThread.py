from multiprocessing import Pool
from computationTimes import timingComparison


def __main__():
    with Pool(processes=12) as p:
        p.map(timingComparison(20), range(200), chunksize=10)
