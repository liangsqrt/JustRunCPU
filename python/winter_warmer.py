import numpy as np
from multiprocessing import Process, Pool
import multiprocessing
import logging
import os
import datetime
import time
import psutil
from logging.handlers import TimedRotatingFileHandler


BaseDir = os.path.dirname(__file__)
LogDir = os.path.join(BaseDir, "logs")


def get_logger(pid, level=logging.DEBUG, when='midnight', back_count=0):
    logger = logging.getLogger(str(pid))
    log_path = os.path.join(LogDir, datetime.datetime.now().strftime("%Y_%m_%d_%H_")+str(pid)+".log")
    if not os.path.exists(LogDir):
        os.mkdir(LogDir)
    formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    fh = TimedRotatingFileHandler(
        filename=log_path,
        when=when,
        backupCount=back_count,
        encoding='utf-8')
    fh.setLevel(level)
    ch = logging.StreamHandler()
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.warning("log创建成功")
    return logger


def executer(interval=20):
    pid = os.getpid()
    print(pid)
    logger = get_logger(pid=pid)
    logger.info("开始运行，pid是{}".format(str(pid)))
    psutil.cpu_stats()
    aa = np.random.randint(1, 1000, [1000000, 10])
    for i in range(10000):
        aa = aa + aa
        if i % interval == 0:  # 运行一定次数时统计一下
            cpu_info = psutil.cpu_times(percpu=True)
            cpu_info2 = [
                (round((x.user + x.system) / (x.user + x.system + x.idle), 3), round(x.user / (x.user + x.system), 3),
                 round(x.system / (x.user + x.system), 3)) for x in cpu_info]
            for _cpu in cpu_info2:
                logger.info("总体占用:{}, 用户占比:{}, 系统占比:{}".format(_cpu[0], _cpu[1], _cpu[2]))


if __name__ == '__main__':
    threshold = 0.8
    total_time = 1*3600

    time1 = time.time()
    process_list = []
    while True:
        time.sleep(2)
        cpu_info = psutil.cpu_times(percpu=True)
        total = sum([(x.user + x.system + x.nice)/(x.user + x.system + x.nice + x.idle) for x in cpu_info])/len(cpu_info)
        print(total)
        if total < threshold and time.time()-time1 < total_time:
            process = multiprocessing.Process(target=executer, args=(20,))
            process.start()
            process_list.append(process)
        if time.time() - time1 > total_time:
            break

    print("等待进程结束")
    for _p in process_list:
        _p.join()







