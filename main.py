import subprocess
import random
import cv2
import numpy as np
from matplotlib import pyplot as plt





def get_threshold():
    pass









# if __name__ == '__main__':
#     images = subprocess.check_output(['ls images'], shell=True).decode().split('\n')
#     images = {x.split('.')[0]: cv2.imread('images/' + x, 0) for x in images if x.startswith('g')}
#     graphs = {k: [[255 if x[i] == 255 else 0 for i in range(len(x))] for x in v] for k, v in images.items()}
#     try:
#         seeds(graphs['g1'], len(graphs['g1']), len(graphs['g1'][0]))
#     except Exception as e:
#         print(type(e))
#         pass
#     # seeds(graphs['g2'], *images['g2'].shape)
#     plt.imshow(graphs['g1'], cmap='gray')
#     plt.show()
