import os
from multiprocessing import Pool
import time


def work(i):
    """工作函数,再该函数内执行程序操作"""
    print(os.getpid())
    time.sleep(10)  # 等待 模拟IO阻塞


def work2():
    print(os.getpid(), "*")
    time.sleep(5)


if __name__ == '__main__':
    """
    processes=54   
    设置进程池进程数量
    
    pool.apply_async(work, (i,), )
    将函数添加到进程,传参为元组
    
    进程池可以运行多种函数
    """

    pool = Pool(processes=54)
    for i in range(100):
        pool.apply_async(work, (i,), )
        pool.apply_async(work2, )

    pool.close()  # 关闭进程池不在接受新任务
    pool.join()  # 等待进程内任务完成
