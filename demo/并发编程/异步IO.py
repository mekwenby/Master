import asyncio
import time

"""
使用async关键字定义函数该函数不能直接运行,运行会返回一个coroutine object 对象
<coroutine object work at 0x000002099BB84240>

coroutine   -- 使用async定义的函数,coroutine需要变成task才能被event_loop执行
task        -- 被event_loop执行的对象 
event_loop  -- 存放task的容器,依次执行里面的task
await       -- 用该关键字定义的代码会阻塞等待执行完成
"""

'''定义一个工作函数'''


async def download(string, delay):
    print('下载:', string)
    # 用asyncio.sleep() 模拟IO阻塞过程
    await asyncio.sleep(delay)
    # 函数返回值
    return string


"""定义一个主函数"""


async def main():
    print(f"开始 at {time.strftime('%X')}")

    '''使用asyncio.create_task将coroutine转换为task并添加到event_loop'''
    task1 = asyncio.create_task(
        download('C++.pdf', 2)
    )
    task2 = asyncio.create_task(
        download('C++.ppt', 2)
    )
    '''执行task并拿回返回值'''
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)

    '''使用asyncio.gather将coroutine添加到event_loop,并用ret接收函数返回值,是一个列表'''

    ret = await asyncio.gather(
        download('Java.txt', 2),
        download('Golang.txt', 3)
    )
    print(ret)
    print(f"结束 at {time.strftime('%X')}")


"""使用asyncio.run()即可运行coroutine"""

asyncio.run(main())

"""只有在需要IO阻塞的情况下使用异步IO才能获得性能提升"""
