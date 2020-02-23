import socket


def main():
    # 创建一个UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息（IP+Port）
    udp_socket.bind(("",7890))
    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")
        # 使用socket发送数据
        udp_socket.sendto(send_data.encode("gbk"), ("127.0.0.1", 8080))

    # 关闭socket
    udp_socket.close()


if __name__ == '__main__':
    main()
