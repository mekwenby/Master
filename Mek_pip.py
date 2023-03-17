# 包管理工具的二次封装

import sys
import os


class _pip():

    def get_requirements(self):  # 获取依赖列表
        '''pip freeze > requirements.txt'''
        os.system('pip freeze > requirements.txt')

    def install(self, name):  # 安装指定库
        cmd = f'pip install {name} -i "http://mirrors.aliyun.com/pypi/simple" --trusted-host "mirrors.aliyun.com"'
        os.system(cmd)

    def requirements(self, file='requirements.txt'):  # 通过列表文件安装库
        cmd = f'pip install -r {file} -i "http://mirrors.aliyun.com/pypi/simple" --trusted-host "mirrors.aliyun.com"'
        os.system(cmd)


if __name__ == '__main__':
    pip = _pip()
    pip.get_requirements()

    # pip.get_requirements()
    # pip.requirements()
