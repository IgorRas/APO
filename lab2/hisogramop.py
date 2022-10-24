import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
import os


def roz_hist_max(source, a, b):
    img = plt.imread(source)
    height = img.shape[0]
    width = img.shape[1]
    after_img_ar = np.zeros([height, width])
    before_img_ar = np.round(img*255)
    a = np.min(before_img_ar[np.nonzero(before_img_ar)])
    b = np.max(before_img_ar[np.nonzero(before_img_ar)])

    print(img.size)
    print(before_img_ar)
    for i in range(height):
        for j in range(width):
            after_img_ar[i][j] = ((before_img_ar[i][j]-a)*(255/(b-a)))
    for i in range(height):
        for j in range(width):
            if after_img_ar[i][j] < 0:
                after_img_ar[i][j] = 0
            elif after_img_ar[i][j] > 255:
                after_img_ar[i][j] = 255

    im = Image.fromarray(after_img_ar)
    im.show()
    plt.hist(after_img_ar.ravel(), 256, [0, 256])
    plt.show()


def roz_hist(source, a, b):
    img = plt.imread(source)
    height = img.shape[0]
    width = img.shape[1]
    after_img_ar = np.zeros([height, width])
    before_img_ar = np.round(img*255)

    print(img.size)
    print(before_img_ar)
    for i in range(height):
        for j in range(width):
            after_img_ar[i][j] = ((before_img_ar[i][j]-a)*(255/(b-a)))
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


def equalize_cv(source):
    img = cv2.imread(source, 0)
    equ = cv2.equalizeHist(img)
    res = np.hstack((img, equ))  # stacking images side-by-side
    cv2.imwrite('copied/res.png', res)


def equalize(source):
    img = cv2.imread(source, 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = np.cumsum(hist)
    nj = (cdf - cdf.min()) * 255
    N = cdf.max() - cdf.min()
    cdf_normalized = nj / N
    cdf_normalized = cdf_normalized.astype('uint8')

    temp_img = img.flatten()
    img_arr = cdf_normalized[temp_img]
    img_arr = np.reshape(img_arr, img.shape)
    img_fin = Image.fromarray(img_arr)
    print(img_arr)
    img_fin.show()
    # print(img2)
