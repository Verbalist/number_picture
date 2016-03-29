import subprocess
import random
import cv2
import numpy as np
from matplotlib import pyplot as plt


def flood_fill(_x, _y, color, image, white=(255, 255, 255)):
    if image.getpixel((_x, _y)) != white:
        return None
    return_set = []
    fill_set = set()
    fill_set.add((_x, _y))
    (a, b, c) = image.getpixel((_x, _y))
    while fill_set:
        (x, y) = fill_set.pop()
        (a, b, c) = image.getpixel((x, y))
        if not (a, b, c) == white:
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
    return return_set


def seeds(mas, img, white=255):

    # def rec(i, j, vec):
    #     try:
    #
    #
    #         # print(vec)
    #         # if mas[i][j] == white:
    #         #     # mas[i][j] = color_mas[i][j]
    #         #     mas[i][j] = c
    #         #     if vec != 1:
    #         #         if i > 0:
    #         #             rec(i - 1, j, 2)
    #         #     if vec != 2:
    #         #         if i < max_i - 1:
    #         #             rec(i + 1, j, 1)
    #         #     if vec != 3:
    #         #         if j > 0:
    #         #             rec(i, j - 1, 4)
    #         #     if vec != 4:
    #         #         if j < max_j - 1:
    #         #             rec(i, j + 1, 3)
    #     except IndexError as e:
    #         print(e, i, j, max_i, max_j)
    #     except RuntimeError as e:
    #         print(e, i, j, max_i, max_j)

    for _i, m in enumerate(mas):
        for _j, im in enumerate(m):
            # c += 5
            if im == white:
                # rec(_i, _j, 0)
                floodFill(_j, _i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), img)


if __name__ == '__main__':
    images = subprocess.check_output(['ls images'], shell=True).decode().split('\n')
    images = {x.split('.')[0]: cv2.imread('images/' + x, 0) for x in images if x.startswith('g')}
    graphs = {k: [[255 if x[i] == 255 else 0 for i in range(len(x))] for x in v] for k, v in images.items()}
    try:
        seeds(graphs['g1'], len(graphs['g1']), len(graphs['g1'][0]))
    except Exception as e:
        print(type(e))
        pass
    # seeds(graphs['g2'], *images['g2'].shape)
    plt.imshow(graphs['g1'], cmap='gray')
    plt.show()
