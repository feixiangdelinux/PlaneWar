import multiprocessing
import time
'''
进程是代码和资源的集合；多进程：多份资源+一套代码，重量级，非越多越好
线程是具体执行代码的人；多线程：一份资源+一套代码，轻量级
'''
gum = 0


def add1():
    global gum
    for i in range(10):
        print(i)


def add2():
    global gum
    for i in range(10):
        print(i)



if __name__ == '__main__':
    t = multiprocessing.Process(target=add1)
    t.start()
    t1 = multiprocessing.Process(target=add2)
    t1.start()
