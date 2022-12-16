from PIL import Image

TARGET_SIZE = (240, 240)
def resize(fn):
	img = Image.open(fn)
	w, h = img.size
	offset = (w - h)/2
	if w > h:
		img = img.crop((offset, 0, w - offset, h))
	else:
		offset = -offset
		img = img.crop((0, h - offset, w, offset))
	assert img.size[0] == img.size[1]
	return img.resize(TARGET_SIZE)

#resize('xinjiang detainees full_files/20180705123752969_653121199905.jpg').show()