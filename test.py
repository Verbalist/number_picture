from PIL import Image
from PIL.ImageDraw import Draw
import PIL.ImageFont
from matplotlib import pyplot as plt
from main import flood_fill
import random

MEDIA_ROOT = 'images/'
im_name = 'c.jpg'
watermark = 'watermark.png'


img = Image.open(MEDIA_ROOT + str(im_name))
color_img = Image.open(str('test3.jpg'))
w, h = img.size

pix = list(img.getdata())

a = []
for x in range(int(len(pix)/w)):
    a.append([])
    for y in range(w):
        a[-1].append(pix[x*w + y])


color_map = {}


def seeds(mas, _img, white=(255, 255, 255)):

    for _i, m in enumerate(mas):
        for _j, im in enumerate(m):
            if im == white:
                c = (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
                ret = flood_fill(_j, _i, c, _img)
                if ret is not None:
                    color_map[(_j, _i)] = ret


def set_number(img, _draw, f_size=20):
    font = PIL.ImageFont.truetype("micross.ttf", size=f_size)

    for pixel, r_set in color_map.items():
        color = color_img.getpixel(pixel)
        for re_pix in r_set:
            img.putpixel(re_pix, (255, 255, 255))
        if len(r_set) > 50:
            print(color)
            max_i = max(r_set, key=lambda _: _[0])[0]
            min_i = min(r_set, key=lambda _: _[0])[0]
            max_j = max(r_set, key=lambda _: _[1])[1]
            min_j = min(r_set, key=lambda _: _[1])[1]
            _pix = ((max_i - min_i)/2 + min_i, (max_j - min_j)/2 + min_j)
            _draw.text(_pix, str(random.randint(1, 300)), (0, 0, 0), font=font)

        # print((x, y))


seeds(a, img, (255, 255, 255))
draw = Draw(img)
set_number(img, draw)

plt.imshow(img)
plt.show()
