import numpy as np
import psutil
import time


def run(percent:float):
    assert percent > 0, "percent value error"
    assert percent < 98, "percent too high!"
    list = []
    print("going to using memroy at least {}".format(percent))
    print("now it is ", psutil.virtual_memory()[2])
    while True:
        if psutil.virtual_memory()[2] < percent:
            arr = np.ones((1001,131)) 
            # sys.getsizeof(arr)/1024/1024 = 1.0005569  # 约等于1M
            print("system memory info: ",psutil.virtual_memory())
            time.sleep(0.01)
            list.append(arr)
        else:
            time.sleep(2)


if __name__ == '__main__':
    run(percent=82.0)
    