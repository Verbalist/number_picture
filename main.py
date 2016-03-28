import subprocess

import cv2
import numpy as np
from matplotlib import pyplot as plt

images = subprocess.check_output(['ls images'], shell=True).decode().split('\n')
images = {x.split('.')[0]: cv2.imread('images/' + x, 0) for x in images if x.startswith('g')}
graphs = {k: [[255 if x[i] == 255 else 0 for i in range(len(x))] for x in v] for k, v in images.items()}


def seeds(mas, max_i, max_j, white=255, c=10):
    def rec(i, j, c, vec):
        try:
            if mas[i][j] == white:
                mas[i][j] = c
                if vec != 1:
                    if i > 0:
                        rec(i - 1, j, c, 1)
                if vec != 2:
                    if i < max_i - 1:
                        rec(i + 1, j, c, 1)
                if vec != 3:
                    if j > 0:
                        rec(i, j - 1, c, 1)
                if vec == 4:
                    if i < max_j - 1:
                        rec(i, j + 1, c, 1)
        except IndexError as e:
            print(e, i, j, max_i, max_j)

    for _i, m in enumerate(mas):
        for _j, im in enumerate(m):
            if im == white:
                c += 10
                rec(_i, _j, c, 0)


seeds(graphs['g1'], len(graphs['g1']), len(graphs['g1'][0]))
plt.imshow(graphs['g1'], cmap='gray')
plt.show()
