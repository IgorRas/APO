import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
import os


def roz_hist(source, a, b):
    img = plt.imread(source)
    height = img.shape[0]
    width = img.shape[1]
    after_img_ar = np.zeros([height, width])
    before_img_ar = np.round(img*256)
    print(img.size)
    for i in range(height):
        for j in range(width):
            after_img_ar[i][j] = ((before_img_ar[i][j]-a)*(256/(b-a)))
    for i in range(height):
        for j in range(width):
            if after_img_ar[i][j] < a:
                after_img_ar[i][j] = a
            elif after_img_ar[i][j] > b:
                after_img_ar[i][j] = b

    im = Image.fromarray(after_img_ar)
    im.show()
    plt.hist(after_img_ar.ravel(), 256, [0, 256])
    plt.show()
