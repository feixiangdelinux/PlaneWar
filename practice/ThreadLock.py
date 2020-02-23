import threading
import time

gum = 0


def add1():
    global gum
    for i in range(10000):
        # 上锁（若锁空闲，则上锁成功；若锁在占用中，则等待锁释放后再上锁）
        mutex.acquire()
        gum += 1
        # 释放锁
        mutex.release()

def add2():
    global gum
    for i in range(10000):
        mutex.acquire()
        gum += 1
        mutex.release()

# 互斥锁，解决资源竞争问题
# ---同一时间，只能有一个处于锁定状态。多次请求锁定，后请求的需要等待上一个锁释放后才能使用
# 当程序中存在多个异步锁，当两方都在锁定状态，且都在等待对方解锁时，就会出现死锁
#   避免死锁的方法：程序设计时尽量避免（银行家算法）；添加超时时间
mutex = threading.Lock()

if __name__ == '__main__':
    print("gum = %s" % gum)
    t = threading.Thread(target=add1)
    t.start()
    print("gum = %s" % gum)
    t1 = threading.Thread(target=add2)
    t1.start()
    print("gum = %s" % gum)
