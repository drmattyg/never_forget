import random
from PIL import Image
from lib import LCD_1inch28
import os
import time
# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0

IMG_DIR = '/home/pi/fmn/img'

FADE_STEPS = 100
IMAGE_TIME = 10 # sec
FADE_TIME = 10 # sec
FADE_SLEEP = FADE_TIME/FADE_STEPS
class Fader:
    def __init__(self, im1, im2, fade_steps, precompute=False):
        self.im1 = im1
        self.im2 = im2
        self.im_black = Image.new(mode=im1.mode, size=im1.size)
        self.fade_steps = fade_steps
        self.max_step = int(fade_steps / 2)
        self.n = 0
        self.precompute = precompute
        if precompute:
                print('precomputing')
                self.imgs = self.do_precompute()

    def do_precompute(self):
       imgs = [x for x in self]
       return imgs 

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.fade_steps:
            raise StopIteration
        self.n += 1
        if self.n <= self.max_step:
            return Image.blend(self.im1, self.im_black, alpha=(self.n - 1) / (self.max_step - 1))
        else:
            return Image.blend(self.im_black, self.im2, alpha=(self.n - self.max_step) / (self.max_step - 1))

    @staticmethod
    def from_filenames(fn1, fn2, fade_steps=FADE_STEPS, img_dir=IMG_DIR):
        return Fader(Image.open(os.path.join(img_dir, fn1)), Image.open(os.path.join(img_dir, fn2)), fade_steps=fade_steps)

if __name__ == '__main__':

    #disp = LCD_1inch28.LCD_1inch28(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_1inch28.LCD_1inch28()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    imgs = os.listdir(IMG_DIR)
    random.shuffle(imgs)
    while True:
        for n in range(len(imgs) - 1):
            fader = Fader.from_filenames(imgs[n], imgs[n+1], FADE_STEPS)
            disp.ShowImage(fader.im1)
            time.sleep(IMAGE_TIME)
            if fader.precompute:
                fader = fader.imgs
                
            for im in fader:
                time.sleep(FADE_SLEEP)
                disp.ShowImage(im)
        fader = Fader.from_filenames(imgs[-1], imgs[0])
        for im in fader:
            time.sleep(FADE_SLEEP)
            disp.ShowImage(im)



