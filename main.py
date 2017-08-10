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
            if Pixels[i, j] > Threshold: # ������ֵ����Ϊ��ɫ�������ɫ
                Pixels[i, j] = 255 # ��ɫ
            else:
                Pixels[i, j] = 0 # ��ɫ
    return ImgNew

 
# ���������ĸ
def charRandom():
    return chr((random.randint(65,90)))
 
# �����������
def numRandom():
    return chr(random.randint(48,57))

# ���������ĸ��������
def textRandom():
    # 0-1�������
    if random.random()>0.7:
        return numRandom()
    else:
        return charRandom()
    
 
# �����ɫ
def colorRandom1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
 
# ���������ɫ2
def colorRandom2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
 
def create_security_img():
    width = 60 * 4
    height = 60
    # ����һ��ȫ�׵�ͼƬ 
    image = Image.new('RGB', (width,height), (255,255,255));
    
    # ����draw����
    draw = ImageDraw.Draw(image)
    
    # ����font���� ע���������ϴ󲿷����϶������� ����Ӧ���Լ�ȥpython��Ӧ��Ŀ¼�������ļ���·��
    font = ImageFont.truetype(r'C:\Users\Li\Documents\GitHub\NJU_jiaowu_ValidateCode\venv\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\cmr10.ttf',36);
    
    # �������
    for t in range(4):
        # ��ʼλ�� Ҫд����ĸ ���� ��ɫ
        draw.text((60*t+10,10), textRandom(), font=font, fill=colorRandom2())
    return image

if __name__ == '__main__':
    img=create_security_img()
    img.show()
	
