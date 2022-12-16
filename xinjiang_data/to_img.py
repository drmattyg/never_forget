from PIL import Image, ImageDraw, ImageFont
import json

TARGET_SIZE = (240, 240)
IMAGE_DIR = "/Users/matthewgordon/repo/never_forget/xinjiang_data/xinjiang detainees full_files/"
def resize(fn):
	img = Image.open(IMAGE_DIR + fn)
	w, h = img.size
	offset = (w - h)/2
	if w > h:
		img = img.crop((offset, 0, w - offset, h))
	else:
		offset = -offset
		img = img.crop((0, h - offset, w, offset))
	assert img.size[0] == img.size[1]
	return img.resize(TARGET_SIZE)

def text_image(d, font_size=20):
	name = d['name']
	age = d['age']
	img = resize(d['img'])
	I1 = ImageDraw.Draw(img)
	font = ImageFont.truetype('AmericanTypewriter.ttc',font_size)
	I1.text((0, 0), f'Name: {name}', fill=(0, 0, 0), font=font)
	I1.text((0, font_size), f'Age: {age}', fill=(0, 0, 0), font=font)
	return img

with open('detainees.json', 'r') as f:
	j = json.load(f)
	text_image(j[0]).show()