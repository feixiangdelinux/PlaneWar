import multiprocessing
import time

'''
进程是代码和资源的集合；多进程：多份资源+一套代码，重量级，非越多越好
线程是具体执行代码的人；多线程：一份资源+一套代码，轻量级
'''
if __name__ == '__main__':

    q = multiprocessing.Queue(3)
    q.put("1")
    q.put(22)
    q.put(["a", 1, 1.5])

    while True:
        print(q.get())

        if q.empty():
            break
