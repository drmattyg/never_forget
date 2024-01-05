import sys
import tkinter
from PIL import Image, ImageTk
from time import sleep

root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()    
root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
canvas = tkinter.Canvas(root,width=w,height=h)
canvas.pack()
canvas.configure(background='black')

def showPIL(pilImage):
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.LANCZOS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    canvas.update()

ALPHA_DELTA_PER_STEP = 3
ALPHA_SLEEP = 0
SLIDE_SLEEP = 5
IMAGE_DIR = '/Users/matthewgordon/personal/never_again_old/xinjiang_data/processed_images_full/'
for i in range(3):
    img = Image.open(IMAGE_DIR + str(i) + '.bmp')
    for a in range(0, 255 + ALPHA_DELTA_PER_STEP, ALPHA_DELTA_PER_STEP):
        img.putalpha(a)
        showPIL(img)
        if ALPHA_SLEEP > 0:
            sleep(ALPHA_SLEEP)
    sleep(SLIDE_SLEEP)
        #sleep(0.005)
    for a in range(255, -ALPHA_DELTA_PER_STEP, -ALPHA_DELTA_PER_STEP):
        img.putalpha(a)
        showPIL(img)

    