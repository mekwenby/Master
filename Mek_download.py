# 下载工具集

import wget
import os

compile_time = 20220426

class _wget():
    def __init__(self,url):
        '''url  = 资源路径  DL = 下载保存路径'''
        self.url = url
        self.DL = 'DL'

    def download(self):
        #通过url直接下载
        wget.download(url=self.url)

    def get_file_name(self):
        #获取文件名
        self.name = wget.filename_from_url(self.url)
        return self.name

    def file_not_download(self):
        #判断文件是否存在，不存在则下载
        if os.path.isfile(self.get_file_name()):
            print('文件已存在！')
        else:
            file_path = os.path.join(self.DL,self.get_file_name())
            wget.download(self.url,out=file_path)

            