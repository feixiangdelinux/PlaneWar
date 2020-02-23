import multiprocessing


def download_from_web(q):
    '''下载数据'''
    # 获取数据
    data = [1, 2, 3]
    # 写入队列
    for temp in data:
        q.put(temp)
    print("队列写入成功")


def analysis_data(q):
    '''数据处理'''
    # 从队列中取数据
    waitting_analysis_data = list()
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        if q.empty():
            break
    print("队列消费成功")
    print("队列内容：%s" % waitting_analysis_data)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()

    # 创建多个进程，将队列的引用当做实参进行传递
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
