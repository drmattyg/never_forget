from PIL import Image, ImageDraw, ImageFont
import json

TARGET_SIZE = (240, 240)
IMAGE_DIR = "/Users/matthewgordon/repo/never_forget/xinjiang_data/xinjiang detainees full_files/"
OUTPUT_DIR = '/Users/matthewgordon/repo/never_forget/xinjiang_data/processed_images/'
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

def text_image(d, font_size=20, small_font_size=12):
	name = d['name']
	age = d['age']
	print(d['img'])
	img = resize(d['img'])
	I1 = ImageDraw.Draw(img)
	font = ImageFont.truetype('AmericanTypewriter.ttc',font_size)
	small_font = ImageFont.truetype('AmericanTypewriter.ttc',small_font_size)
	if len(name) < 16:
		
		I1.text((0, 0), f'Name: {name}', fill=(0, 0, 0), font=font)
	else:
		I1.text((0, 0), f'Name: ', fill=(0, 0, 0), font=font)
		I1.text((70, 9), name, fill=(0, 0, 0), font=small_font)
	
	I1.text((0, font_size), f'Age: {age}', fill=(0, 0, 0), font=font)
	return img

with open('detainees.json', 'r') as f:
	j = json.load(f)
	for i, rec in enumerate(j):
		img = text_image(rec)
		img.save(OUTPUT_DIR + f'{i}.bmp')
