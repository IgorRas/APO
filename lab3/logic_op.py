import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import cv2
import numpy as np


def op_and(img1, img2):
    image1 = cv2.imread(img1, 0)
    image2 = cv2.imread(img2, 0)

    height = image1.shape[0]
    width = image1.shape[1]
    n_img = np.zeros([height, width])

    for i in range(height):
        for j in range(width):
            n_img[i][j] = image1[i][j] & image2[i][j]

    plt.imshow(n_img, cmap='gray')
    plt.show()


def op_or(img1, img2):
    image1 = cv2.imread(img1, 0)
    image2 = cv2.imread(img2, 0)

    height = image1.shape[0]
    width = image1.shape[1]
    n_img = np.zeros([height, width])

    for i in range(height):
        for j in range(width):
            n_img[i][j] = image1[i][j] | image2[i][j]

    plt.imshow(n_img, cmap='gray')
    plt.show()


def op_xor(img1, img2):
    image1 = cv2.imread(img1, 0)
    image2 = cv2.imread(img2, 0)

    height = image1.shape[0]
    width = image1.shape[1]
    n_img = np.zeros([height, width])

    for i in range(height):
        for j in range(width):
            n_img[i][j] = image1[i][j] ^ image2[i][j]

    plt.imshow(n_img, cmap='gray')
    plt.show()