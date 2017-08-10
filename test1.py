import requests
from flask import render_template, Flask, Response
from PIL import Image
import os
import pytesseract

app = Flask(__name__)

def Binarized(Image,Threshold):
	ImgNew=Image.crop()
	Pixels = ImgNew.load()
	(Width, Height) = ImgNew.size
	for i in range(Width):
		for j in range(Height):
			if Pixels[i, j] > Threshold: # 大于阈值的置为白色，否则黑色
				Pixels[i, j] = (255, 255, 255) # 白色
			else:
				Pixels[i, j] = (0, 0, 0) # 黑色
	return ImgNew

def get_vcode(i):
	im1 = Image.open('./{}_1.jpg'.format(i))
	im2 = Image.open('./{}_2.jpg'.format(i))
	# code1 = pytesseract.image_to_string(im1, config='-psm 7')
	code2 = pytesseract.image_to_string(im2, config='-psm 7 digits')
	print(code2)
	return code2

@app.route('/')
def index():
	vcode = []
	for i in range(20):
		req = requests.get('http://desktop.nju.edu.cn:8080/jiaowu/ValidateCode.jsp')
		img = req.content
		with open('./{}_1.jpg'.format(i), 'wb') as f:
			f.write(img)
		im = Image.open('./{}_1.jpg'.format(i))
		im2 = Binarized(im, (150, 150, 150))
		im2 = im2.crop((1,1,60,19))
		im2.save('./{}_2.jpg'.format(i))
		vcode.append(get_vcode(i))

	return render_template('index.html', vcode=vcode)

@app.route('/image/<name>')
def image(name):
	img = open(u'{}.jpg'.format(name), 'rb')
	resp = Response(img, mimetype="image/jpeg")
	return resp
	
if __name__ == '__main__':
    app.run()