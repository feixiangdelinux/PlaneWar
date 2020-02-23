import os
import random
import time
from multiprocessing.pool import Pool


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("%s执行完毕，耗时%0.2f" % (t_stop - t_start))


po = Pool(3)  # 定义一个进程池，最大进程数3
for i in range(0, 10):
    po.apply_async(worker, (i,))

print("------------start--------")
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中所有子进程执行完毕，必须放在close语句之后
print("------------stop--------")
