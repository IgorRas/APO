import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import cv2
import numpy as np


def add_normal_cv(img1, img2):
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)
    dst = cv2.addWeighted(image1, 0.5, image2, 0.5, 0.0)
    cv2.imshow('dst', dst)


def add_normal(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    im3 = ImageChops.add(image1, image2, scale=2.0)
    im3.show()


def multiply(img, num):
    img = cv2.imread(img, 0)
    height = img.shape[0]
    width = img.shape[1]
    n_img = np.zeros([height, width])
    for i in range(height):
        for j in range(width):
            n_img[i][j] = img[i][j]*num

    fin_img = np.clip(n_img, 0, 255)
    plt.imshow(fin_img, cmap='gray')
    plt.show()


def divide(img, num):
    img = cv2.imread(img, 0)
    height = img.shape[0]
    width = img.shape[1]
    n_img = np.zeros([height, width])
    for i in range(height):
        for j in range(width):
            n_img[i][j] = img[i][j]/num
    fin_img = np.clip(n_img.round(), 0, 255)
    plt.imshow(fin_img, cmap='gray')
    plt.show()


def bezwgl(img1, img2):
    image1 = cv2.imread(img1, 0)
    image2 = cv2.imread(img2, 0)
    height = image1.shape[0]
    width = image1.shape[1]
    n_img = np.zeros([height, width])
    for i in range(height):
        for j in range(width):
            n_img[i][j] = abs(image1[i][j] - image2[i][j])
    cv2.imwrite('copied/tettt.png', n_img)
    cv2.imshow('Difference', cv2.imread('copied/tettt.png'))
