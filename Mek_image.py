import imagehash
from PIL import Image, ImageTk
import qrcode
import tkinter
import os
from pyzbar import pyzbar

"""
ImageHash==4.3.1
qrcode==7.3.1
pyzbar==0.1.9
"""

"""获取图片信息"""


def get_image_hash(file):  # 获取图片的哈希值，用于判断图片是否相同
    image = Image.open(file)
    return imagehash.average_hash(image)


def get_image_size(file):  # 获取图片尺寸
    image = Image.open(file)
    return image.size


def image_convert_webp(file):
    """将图片转换为webp格式"""
    im = Image.open(file).convert("RGB")
    im.save(f'{file}.webp', "WEBP")


def image_jpg_compress(file, quality=75):
    """用Jpg 对文件进行压缩"""
    img2 = Image.open(file)
    # quality参数： 保存图像的质量，值的范围从1（最差）到95（最佳）。 默认值为75，使用中应尽量避免高
    # 于95的值; 100会禁用部分JPEG压缩算法，并导致大文件图像质量几乎没有任何增益。
    # subsampling参数：子采样，通过实现色度信息的分辨率低于亮度信息来对图像进行编码的实践
    # （自己尝试）可能的子采样值是0,1和2，对应于4：4：4,4：2：2和4：1：1（或4：2：0？）。

    img2.save(f'quality_{quality}_{file}', quality=quality, subsampling=2)


"""二维码工具"""


def Create_QRcode(Data='Mek', file=None):  # 二维码生成工具
    IMG = qrcode.make(Data)  # 创建图片对象二进制数据流
    if file != None:  # 保持二维码到文件
        with open(file, 'wb') as f:
            IMG.save(f)  # 图片对象保存到文件

    else:  # 不输入文件名直接弹出窗口显示二维码
        root = tkinter.Tk()
        root.title(Data)
        IMG = ImageTk.PhotoImage(IMG)
        tkinter.Label(root, image=IMG).pack()
        root.mainloop()


def decode_QRcode(file):  # 解析二维码
    if not os.path.exists(file):
        raise FileExistsError(file)
    ''' data 直接返回读取到的数据 二进制格式'''
    return pyzbar.decode(Image.open(file), symbols=[pyzbar.ZBarSymbol.QRCODE])[0].data


if __name__ == '__main__':
    pass
