__author__ = 'verbalist'

import numpy as np
import cv2
from matplotlib import pyplot as plt
import hashlib

img2 = cv2.imread('img_proc.jpg')
# img = cv2.imread('test2.jpg')
# img2 = cv2.pyrMeanShiftFiltering(img,  50, 30, 3)
# cv2.imwrite('test4.png', img2)
# img2 = cv2.imread('test4.png')

def is_distance(obj1, obj2):
    obj = obj2 - obj1
    for x in obj:
        if x != 0:
            return False
    return True

def distance(obj2, obj1):
    return sum(obj2 - obj1)

class RGB():

    def __init__(self, mas):
        self.r = mas[0]
        self.g = mas[1]
        self.b = mas[2]
        self.mas = [x for x in mas]

    def __eq__(self, other):
        if self.r == other.r and self.g == other.g and self.b == other.b:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.r, self.g, self.b))

    def __str__(self):
        return 'r: {0}, g: {1}, b: {2}'.format(self.r, self.g, self.b)

    def is_white(self):
        if self.r == 255 and self.g == 255 and self.b == 255:
            return True
        else:
            return False



# mas = [RGB(img2[0][0])]
colors = {}
set_colors = set()
for i, row in enumerate(img2):
    for j, x in enumerate(row):
        rgb = RGB(x)
        # if rgb == mas[-1] and not rgb.is_white():
        #     print(rgb)
        if rgb in set_colors:
            colors[rgb].append([i, j])
        else:
            colors[rgb] = [[i, j]]
            set_colors.add(rgb)
        # if rgb not in colors:
        #     colors.add(rgb)
mas = []
for k, v in colors.items():
    if len(v) > 400:
        print(k, ':', len(v))
        mas.append(k.mas)

import math
cv2.imshow('image', img2)
n = math.ceil(math.sqrt(len(mas)))
for i, x in enumerate(mas):
    plt.subplot(n, n, i + 1)
    plt.imshow(np.array([[np.array([x[2], x[1], x[0]]) for _ in range(11)] for _1 in range(11)]))

plt.show()