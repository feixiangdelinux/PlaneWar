import socket


def main():
    # 1.创建socket
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 2.绑定本地信息(IP+Port)
    localaddr = ("",7788)
    udp_socket.bind(localaddr)
    # 3.接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        # 4.打印收到的数据
        print("%s:%s" % (str(send_addr),recv_msg.decode("gbk")))
    # 5.关闭socket
    udp_socket.close()

if __name__ == '__main__':
    main()