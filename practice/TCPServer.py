import socket


def main():
    # socket创建一个套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind绑定套接字变为可以被动链接
    server_ip = "127.0.0.1"
    server_port = 7890
    tcp_server_socket.bind((server_ip, server_port))

    # listen设置socket接受被动链接
    tcp_server_socket.listen(128)
    while True:  # 循环为多个客户端服务
        # accept等待客户端的链接
        client_socket, client_addr = tcp_server_socket.accept()

        while True:  # 循环为某个客户端服务多次
            # recv/send接收发送数据
            recv_data = client_socket.recv(1024)
            print("客户端发来的请求是：%s" % recv_data.decode("gbk"))

            # 如果recv解堵塞，那么有两种方式：
            # 1.客户端发送过来数据
            # 2.客户端调用close导致
            if recv_data:
                # 给客户端回数据
                client_socket.send("this is callback".encode("gbk"))
            else:
                break

        # 关闭accept返回的socket，意味着，TCP服务器不会再为这个客户端服务
        client_socket.close()

    # 关闭TCP服务器听监听socket，意味着关闭TCP的监听服务，即不能响应来自TCP客户端的请求，即****。accept会失败
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
