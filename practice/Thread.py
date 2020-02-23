import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(100):
            msg = "I'm" + self.name + "@" + str(i)  # name中保存的是当前线程的名字
            print(msg)
            self.login()
            # time.sleep(1)

    def login(self):
        print("This is run ")

def sing():
    for i in range(10):
        print("唱歌第%s次"  %i)
        # time.sleep(1)

if __name__ == '__main__':
    t = MyThread()  # 方法1:通过继承Thread类完成多线程
    t.start()
    t1 = threading.Thread(target=sing)  # 方法2:通过target属性定义多线程，注意target后的函数不能加（）
    t1.start()
    print("It's done")


