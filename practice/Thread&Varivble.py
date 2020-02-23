import threading
import time

num = 100
numlist = [1, 2, 3]


def needGlobal():
    global num  # 修改全局变量的指向，需要加global
    num += 100


def noGlobal():
    numlist.append(100)  # 不修改全局变量的指向，不需要加global


def print1():
    '''
    多线程间共享全局变量--方法1
    '''
    print("Thread-print num = %d" % num)
    print("Thread-print numlist = %s" % numlist)

def print2(temp):
    '''
    多线程间共享全局变量--方法2
        通过args传参方式共享全局变量
    '''
    print("Thread-print temp = %s" % temp)


if __name__ == '__main__':
    print("Thread-main num = %d" % num)
    print("Thread-main numlist = %s" % numlist)
    t1 = threading.Thread(target=needGlobal)
    t2 = threading.Thread(target=noGlobal)
    t3 = threading.Thread(target=print1)
    a = (33,)
    t4 = threading.Thread(target=print2,args=a)
    t1.start()
    t2.start()
    time.sleep(1)
    t3.start()
    time.sleep(1)
    t4.start()
    print("Thread-main num = %d" % num) # 多线程间共享全局变量
    print("Thread-main numlist = %s" % numlist) # 多线程间共享全局变量

