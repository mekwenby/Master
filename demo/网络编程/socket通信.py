import socket
import threading
import Mek_master


# 创建一个socket连接
class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定端口和IP
        self.s.bind(('127.0.0.1', 9090))
        # 把socket变成一个被动监听的socket 128位最大请求数
        # x=s.accept()#接收客户端的请求
        self.s.listen(128)
        # 结果是元组 拆分信息
        # 用第一个信息的recv方法获得数据
        while True:
            client_socket, client_addr = self.s.accept()
            # tcp里使用recv获取数据,1024指获取的字节
            data = client_socket.recv(5120)
            print('接收到了{}客户端{}端口号发送的数据，内容是：{}'.format(
                client_addr[0], client_addr[1], data.decode('utf8')))
            #print(len(data.decode('utf8')))


class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设置连接的IP地址和端口号
        self.s.connect(('127.0.0.1', 9090))
        # 发送数据

        self.s.send(Mek_master.get_random_letters(16).encode('utf8'))
        self.s.close()


def s():
    Server()


def c():
    for i in range(10):
        Client()


if __name__ == '__main__':
    # 创建服务线程
    st = threading.Thread(target=s)
    ct = threading.Thread(target=c)
    # 启动线程
    st.start()
    ct.start()
