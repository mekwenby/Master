import time
from threading import Thread


def dowmload(string):
    """编写工作函数"""
    print('Start Load:', string)
    time.sleep(5)


class Dowload(Thread):
    """将函数重写为类"""
    """
    使用__init__()接收函数传参
    使用run(self)处理函数步骤
    使用start() 启动该线程
    """

    def __init__(self, string):
        super().__init__()
        self.info = string

    def run(self):
        print('Start Load:', self.info)
        time.sleep(5)


'''通过函数创建线程'''
t1 = Thread(target=dowmload, args=('mek.pdf',))
t2 = Thread(target=dowmload, args=('mek.py',))
t1.start()
t2.start()

'''通过重写类创建线程'''
a = Dowload('hello.txt')
b = Dowload('mek.txt')
a.start()
b.start()
