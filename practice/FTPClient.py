import socket


def main():
    # 创建socket链接
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取FTP服务器的地址
    dest_ip = input("请输入FTP服务器IP：")
    dest_port = int(input("请输入FTP服务器port:"))
    # 连接服务器
    tcp_socket.connect((dest_ip, dest_port))
    # 输入要下载的文件名
    download_file_name = input("请输入要下载的文件名：")
    # 发送下载请求
    tcp_socket.send(download_file_name.encode("gbk"))
    # 接收返回结果，最大接收1024个字节，即1KB
    recv_data = tcp_socket.recv(1024 * 1024)
    if recv_data:
        # 将结果保存到文件
        with open("copy" + download_file_name, "wb") as f:
            f.write(recv_data)
    # 关闭socket
    tcp_socket.close()


if __name__ == '__main__':
    main()
