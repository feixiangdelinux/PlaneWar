from socket import *

def main():
    # 创建TCP socket
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    # 绑定本机IP和端口
    server_ip = input("请输入服务器IP：")
    server_port = int(input("请输入服务器端口："))
    tcp_client_socket.connect((server_ip,server_port))

    # 发送数据
    send_data = input("请输入要发送的数据")
    tcp_client_socket.send(send_data.encode("gbk"))

    # 关闭socket
    tcp_client_socket.close()

if __name__ == '__main__':
    main()
