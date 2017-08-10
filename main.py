# coding=utf-8
from __future__ import division
from __future__ import unicode_literals
import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')  # @UndefinedVariable

from PIL import Image,ImageFont,ImageDraw
import random

def Binarized(Image,Threshold):

    ImgNew=Image.crop()
    Pixels = ImgNew.load()
    (Width, Height) = ImgNew.size
    for i in xrange(Width):
        for j in xrange(Height):
            if Pixels[i, j] > Threshold: # 大于阈值的置为白色，否则黑色
                Pixels[i, j] = 255 # 白色
            else:
                Pixels[i, j] = 0 # 黑色
    return ImgNew

 
# 返回随机字母
def charRandom():
    return chr((random.randint(65,90)))
 
# 返回随机数字
def numRandom():
    return chr(random.randint(48,57))

# 返回随机字母或者数字
def textRandom():
    # 0-1的随机数
    if random.random()>0.7:
        return numRandom()
    else:
        return charRandom()
    
 
# 随机颜色
def colorRandom1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
 
# 随机长生颜色2
def colorRandom2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
 
def create_security_img():
    width = 60 * 4
    height = 60
    # 创建一个全白的图片 
    image = Image.new('RGB', (width,height), (255,255,255));
    
    # 创建draw对象
    draw = ImageDraw.Draw(image)
    
    # 创建font对象 注意这里网上大部分资料都有问题 这里应该自己去python对应的目录找字体文件的路径
    font = ImageFont.truetype(r'C:\Users\Li\Documents\GitHub\NJU_jiaowu_ValidateCode\venv\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\cmr10.ttf',36);
    
    # 输出文字
    for t in range(4):
        # 起始位置 要写的字母 字体 颜色
        draw.text((60*t+10,10), textRandom(), font=font, fill=colorRandom2())
    return image

if __name__ == '__main__':
    img=create_security_img()
    img.show()
	
