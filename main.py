import subprocess

import cv2
import numpy as np
from matplotlib import pyplot as plt
#
# img = cv2.imread('lena.jpg',0)
# edges = cv2.Canny(img,225,225)
#
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#
# plt.show()


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test2.jpg')
spatialRadius = 35
colorRadius = 30
# plt.imshow(img)
pyramidLevels = 3
img2 = cv2.pyrMeanShiftFiltering(img,  60, colorRadius, pyramidLevels)
plt.subplot(2, 3, 1), plt.imshow(img)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# ret, thresh = cv2.threshold(gray, 0, 2500, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# print(type(ret), type(thresh))
# plt.subplot(121),
# plt.imshow(thresh, cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(121),plt.imshow(thresh, cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# cv2.Sobel(img, re_img, 1, 1)
# plt.imshow(re_img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# compute the Scharr gradient magnitude representation of the images
# in both the x and y direction
# x = 6
# gradX = cv2.Sobel(gray, ddepth = x, dx = 1, dy = 0, ksize = -1)
# gradY = cv2.Sobel(gray, ddepth = x, dx = 0, dy = 1, ksize = -1)
# gradient = cv2.subtract(gradX, gradY)
# # gradient = cv2.convertScaleAbs(gradient)
# plt.subplot(1,3,1),  plt.imshow(gradient)
# plt.subplot(1,3,2), plt.imshow(cv2.blur(gradient, (9, 9)))
# blur = cv2.blur(gradient, (9, 9))
# # ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY)
# plt.subplot(1,3,3), plt.imshow(blur)

# plt.subplot(2,2,1), plt.imshow(img)
# plt.subplot(2,2,2), plt.imshow(gradient)
# plt.subplot(2,2,3), plt.imshow(cv2.convertScaleAbs(gradX))
# plt.subplot(2,2,4), plt.imshow(cv2.convertScaleAbs(gradY))

# plt.show()
# noise removal
# kernel = np.ones((3, 3), np.uint8)
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)
#
# sure background area
# sure_bg = cv2.dilate(opening,kernel, iterations=100)
#
# Finding sure foreground area
# dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# for i, x in enumerate(range(70, 0, -5)):
#     print(x/100*dist_transform.max())
#     ret, sure_fg = cv2.threshold(dist_transform, x*dist_transform.max(), 2500, 0)
#
#     # Finding unknown region
#     sure_fg = np.uint8(sure_fg)
#     unknown = cv2.subtract(sure_bg, sure_fg)
#     ret, markers = cv2.connectedComponents(sure_fg)
#     # print(markers, markers)
#     # Add one to all labels so that sure background is not 0, but 1
#     markers = markers+1
#
#     # Now, mark the region of unknown with zero
#     markers[unknown==255] = 0
#     markers = cv2.watershed(img, markers)
#     img[markers == -1] = [255, 0, 0]
#     plt.subplot(4, 4, i), \
#     plt.imshow(img.copy(), cmap = 'gray')
#     plt.title(round(x/100,2))



# import random
#
# n = 20
# a = [[1 if random.random() < 0.1 else 0 for _ in range(n)] for __ in range(n)]
# for x in a:
#     print(*x)
#
# images = subprocess.check_output(['ls images'], shell=True).decode().split('\n')
# images = {x.split('.')[0]: cv2.imread('images/' + x, 0) for x in images if x.startswith('g')}
# graphs = {k: [[255 if x[i] == 255 else 0 for i in range(len(x))] for x in v] for k, v in images.items()}
#
#
# def seeds(mas, max_i, max_j, white=255, c=10):
#     def rec(i, j, c, vec):
#         try:
#             if mas[i][j] == white:
#                 mas[i][j] = c
#                 if vec != 1:
#                     if i > 0:
#                         rec(i - 1, j, c, 1)
#                 if vec != 2:
#                     if i < max_i - 1:
#                         rec(i + 1, j, c, 1)
#                 if vec != 3:
#                     if j > 0:
#                         rec(i, j - 1, c, 1)
#                 if vec == 4:
#                     if i < max_j - 1:
#                         rec(i, j + 1, c, 1)
#         except IndexError as e:
#             print(e, i, j, max_i, max_j)
#
#     for _i, m in enumerate(mas):
#         for _j, im in enumerate(m):
#             if im == white:
#                 c += 10
#                 rec(_i, _j, c, 0)
#
#
# seeds(graphs['g1'], len(graphs['g1']), len(graphs['g1'][0]))
# plt.imshow(graphs['g1'], cmap='gray')
# plt.show()
