import imagehash
from PIL import Image,ImageTk
import qrcode
import tkinter
import os
from pyzbar import pyzbar

def get_image_hash(file): #获取图片的哈希值，用于判断图片是否相同
    image = Image.open(file)
    return imagehash.average_hash(image)

def get_image_size(file): #获取图片尺寸
    image = Image.open(file)
    return image.size

def Create_QRcode(Data='Mek',file=None): #二维码生成工具
    IMG=qrcode.make(Data) #创建图片对象二进制数据流
    if file!=None: #保持二维码到文件
        with open(file,'wb') as f:
            IMG.save(f) #图片对象保存到文件

    else: #不输入文件名直接弹出窗口显示二维码
        root = tkinter.Tk()
        root.title(Data)
        IMG = ImageTk.PhotoImage(IMG)
        L = tkinter.Label(root,image=IMG).pack()
        root.mainloop()

def decode_QRcode(file): #解析二维码
    if not os.path.exists(file):
        raise FileExistsError(file)
    ''' data 直接返回读取到的数据 二进制格式'''
    return pyzbar.decode(Image.open(file),symbols=[pyzbar.ZBarSymbol.QRCODE])[0].data


if __name__ == '__main__':
    pass


''' 支持库安装
pip install Imagehash -i "http://mirrors.aliyun.com/pypi/simple" --trusted-host "mirrors.aliyun.com"
pip install qrcode -i "http://mirrors.aliyun.com/pypi/simple" --trusted-host "mirrors.aliyun.com"
pip install pyzbar -i "http://mirrors.aliyun.com/pypi/simple" --trusted-host "mirrors.aliyun.com"


'''