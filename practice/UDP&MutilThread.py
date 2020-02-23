import socket
import threading

# 1.创建socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    '''完成UDP聊天器的整体控制'''
    # 2.绑定本地信息
    global udp_socket
    udp_socket.bind(("", 7890))
    # 3.获取对方的地址
    dest_ip = input("请输入对方的IP：")
    dest_port = int(input("请输入对方的Port："))
    # 创建两个线程，分别执行接收、发送数据功能
    t_recv = threading.Thread(target=recv_msg)
    t_send = threading.Thread(target=send_msg,args=(dest_ip, dest_port))
    # 接收数据
    t_recv.start()
    # 发送数据
    t_send.start()


def recv_msg():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(dest_ip, dest_port):
    while True:
        send_data = input("输入要发送的数据：")
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))


if __name__ == '__main__':
    main()
