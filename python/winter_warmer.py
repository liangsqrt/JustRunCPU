import numpy as np
from multiprocessing import Process, Pool
import multiprocessing
import log
import os
import time
import psutil


BaseDir = os.path.dirname(__file__)
LogDir = os.path.join(BaseDir, "logs")


def run(i):
    pid = os.getpid()
    print(pid)
    aa = np.random.randint(1, 1000, [1000000, 10])
    for i in range(10000):
        aa = aa + aa




if __name__ == '__main__':
    cores = multiprocessing.cpu_count()
    pool = Pool(cores)
    print(cores)
    ree = pool.map(run, [1,2,3,4,5,6,7,8])
    pool.close()
    pool.join()

    