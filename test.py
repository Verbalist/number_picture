from PIL import Image
from PIL.ImageDraw import Draw
import PIL.ImageFont
from matplotlib import pyplot as plt
import random
from sklearn.cluster import k_means, MeanShift, estimate_bandwidth, KMeans

MEDIA_ROOT = 'images/'
im_name = 'c.jpg'
watermark = 'watermark.png'


img = Image.open(MEDIA_ROOT + str(im_name))


def get_mas(_img):
    pix = list(_img.getdata())
    a = []
    for x in range(int(len(pix)/w)):
        a.append([])
        for y in range(w):
            a[-1].append(pix[x*w + y])
    return a


color_map = {}
white_map = {}


def flood_fill(_x, _y, color, image, white=(255, 255, 255)):
    if image.getpixel((_x, _y)) != white:
        return None
    return_set = []
    contour = []
    fill_set = set()
    fill_set.add((_x, _y))
    # (a, b, c) = image.getpixel((_x, _y))
    while fill_set:
        (x, y) = fill_set.pop()
        (a, b, c) = image.getpixel((x, y))
        if not (a, b, c) == white:
            if (a, b, c) != color:
                contour.append((x, y))
            continue
        image.putpixel((x, y), color)
        return_set.append((x, y))
        if x > 1:
            fill_set.add((x - 1, y))
        if x < image.size[0] - 1:
            fill_set.add((x + 1, y))
        if y > 1:
            fill_set.add((x, y - 1))
        if y < image.size[1] - 1:
            fill_set.add((x, y + 1))
    # if not return_set:
        # print(_x, _y, image.getpixel((_x, _y)))
    return return_set, contour


def get_info_area(area):
    return {
        'max_i': max(area, key=lambda _: _[0]),
        'min_i': min(area, key=lambda _: _[0]),
        'max_j': max(area, key=lambda _: _[1]),
        'min_j': min(area, key=lambda _: _[1])
    }


def set_not_white(_img, _h, _w, white=(255, 255, 255)):
    for _i in range(_h):
        for _j in range(_w):
            if _img.getpixel((_j, _i)) == white:
                _img.putpixel((_j, _i), (254, 254, 254))


def get_c_c(_img, _h, _w, white=(255, 255, 255)):
    a = set()
    for _i in range(_h):
        for _j in range(_w):
            _pix = _img.getpixel((_j, _i))
            if _pix not in a:
                a.add(_pix)
    return a


def threshold(_img, _h, _w, t=20, white=(255, 255, 255)):
    for _i in range(_h):
        for _j in range(_w):
            _pix = _img.getpixel((_j, _i))
            if _pix != white:
                white_map[(_j, _i)] = flood_fill(_j, _i, white, _img, white=_pix)

    for _pix, area in white_map.items():
        if len(area[0]) > t:
            for x in area[1]:
                _img.putpixel(x, (0, 0, 0))

    for _pix, area in white_map.items():
        if len(area[0]) < t:
            for x in area[0]:
                _img.putpixel(x, (255, 255, 255))

        #     area.sort(key=lambda _: _[1])
        #     c = area[0][1]
        #     info = get_info_area(area)
        #     min_x = info['max_i']
        #     max_x = info['min_i']
        #     for x in area:
        #         print('x', x)
        #         if x[1] == c:
        #             if x[1] in (info['max_j'][1], info['min_j'][1]):
        #                 _img.putpixel(x, (0, 0, 0))
        #             else:
        #                 if min_x[0] >= x[0]:
        #                     min_x = x
        #                 if max_x[0] <= x[0]:
        #                     max_x = x
        #         else:
        #             print(max_x)
        #             print(min_x)
        #             if x[1] not in (info['max_j'], info['min_j']):
        #                 _img.putpixel(min_x, (0, 0, 0))
        #                 _img.putpixel(max_x, (0, 0, 0))
        #                 c = x[1]
        #                 min_x = info['max_i']
        #                 max_x = info['min_i']
            # for x in area:
            #     _img.putpixel(x, color_img_d.getpixel(x))


def set_black(_img, _h, _w, white=(255, 255, 255)):
    for _i in range(_h):
        for _j in range(_w):
            if _img.getpixel((_j, _i)) != white:
                _img.putpixel((_j, _i), (0, 0, 0))


def set_k_colors(_img, _h, _w, k):
    X = [list(x) for x in get_c_c(color_img, h, w)]
    K = KMeans(n_clusters=k)
    K.fit(X)
    color_set = {i: (int(x[0]), int(x[1]), int(x[2])) for i, x in enumerate(K.cluster_centers_)}
    color_set = {tuple(X[i]): color_set[x] for i, x in enumerate(K.predict(X))}
    for _i in range(_h):
        for _j in range(_w):
            _img.putpixel((_j, _i), color_set[_img.getpixel((_j, _i))])


def seeds(mas, _img, white=(255, 255, 255)):
    for _i, m in enumerate(mas):
        for _j, im in enumerate(m):
            if im == white:
                c = (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
                ret = flood_fill(_j, _i, c, _img)
                if ret is not None:
                    color_map[(_j, _i)] = ret


def seed_filter(img):
    pass


def set_number(_img, _draw, f_size=20):
    font = PIL.ImageFont.truetype("micross.ttf", size=f_size)

    for pixel, r_set in color_map.items():
        color = color_img.getpixel(pixel)
        for re_pix in r_set:
            _img.putpixel(re_pix, color)
        if len(r_set) > 50:
            max_i = max(r_set, key=lambda _: _[0])[0]
            min_i = min(r_set, key=lambda _: _[0])[0]
            max_j = max(r_set, key=lambda _: _[1])[1]
            min_j = min(r_set, key=lambda _: _[1])[1]
            _pix = ((max_i - min_i)/2 + min_i, (max_j - min_j)/2 + min_j)
            _draw.text(_pix, str(random.randint(1, 300)), (0, 0, 0), font=font)

        # print((x, y))

# color_img = Image.open(MEDIA_ROOT + str('5.png'))
color_img = Image.open(MEDIA_ROOT + str('c2.jpg'))
color_img_d = color_img.copy()
w, h = color_img.size

print('___ img read ___')

# bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
# ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
# labels = ms.labels_
# cluster_centers = ms.cluster_centers_


set_k_colors(color_img, h, w, 30)

print('___ set 30 colors ___')

# a = get_c_c(color_img, h, w)
# for x in a:
#     print(x)
# print(len(a))
# print('___ get count colors ___')


# set_not_white(color_img, h, w)

threshold(color_img, h, w, t=20)

# set_black(img, h, w)
# a = get_mas()
# seeds(a, img, (255, 255, 255))
# draw = Draw(img)
# set_number(img, draw, f_size=10)
#
# plt.imshow(color_img)
# plt.savefig(MEDIA_ROOT + '30_color_mask.png')
color_img.save(MEDIA_ROOT + '30_color_mask.png')
# plt.show()
