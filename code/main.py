from PIL import Image

FADE_STEPS = 20
class Fader:
    def __init__(self, im1, im2, fade_steps):
        self.im1 = im1
        self.im2 = im2
        self.im_black = Image.new(mode=im1.mode, size=im1.size)
        self.fade_steps = fade_steps
        self.max_step = int(fade_steps / 2)
        self.n = 0

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
    def from_filenames(fn1, fn2, fade_steps=FADE_STEPS):
        return Fader(Image.open(fn1), Image.open(fn2), fade_steps=fade_steps)
