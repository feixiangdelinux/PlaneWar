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
        # 将文件内容返回客户端
        send_file_2_client(client_socket)
        # 关闭accept返回的socket，意味着，TCP服务器不会再为这个客户端服务
        client_socket.close()

    # 关闭TCP服务器听监听socket，意味着关闭TCP的监听服务，即不能响应来自TCP客户端的请求，即****。accept会失败
    tcp_server_socket.close()


def send_file_2_client(client_socket):
    # 1.接收客户端发来的，要下载的文件名
    file_name = client_socket.recv(1024).decode("gbk")
    # 2.打开文件，读取数据
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as e:
        print("找不到文件：%s" % file_name)
    # 3.将文件内容返回给客户端
    if file_content:
        client_socket.send("this is callback".encode("gbk"))


if __name__ == '__main__':
    main()
