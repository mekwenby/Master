# 下载工具集

"""
wget
requests
"""

import wget
import os
import requests
from urllib.parse import quote, unquote

compile_time = 20230131


def url_encode(string):
    """把字符串转换为URL编码"""
    return quote(string)


def url_decode(string):
    """把URL编码解码为字符串,默认使用UTF8字符集"""
    return unquote(string)


def from_url_filename(url):
    """从url获取文件名"""
    return url.split('/')[-1]


# wget 下载文件
def wget_download(url):
    # 通过url直接下载,保存到当前目录
    wget.download(url=url)


def wget_get_file_name(url):
    # 通过网络获取文件名
    name = wget.filename_from_url(url)
    return name


def wget_file_not_download(url):
    # 判断文件是否存在，不存在则下载
    if os.path.isfile(wget_get_file_name(url)):
        print('文件已存在！')
    else:
        wget.download(url)


# requests 下载文件
def r_download(url):
    # 获取文件名
    filename = from_url_filename(url)
    # 判断文件是否存在,不存在则下载
    if not os.path.isfile(filename):
        responder = requests.get(url)
        # 判断连接状态
        if responder.ok:
            with open(filename, 'wb') as f:
                # responder.content 获得响应主体
                f.write(responder.content)


"""
关于获取文件名：
通过url获取文件名效率高，需要url中包含文件名才能使用
通过网络获取文件名效率低，获取的文件名准确

关于下载：
不建议直接引入内置的下载函数

"""
