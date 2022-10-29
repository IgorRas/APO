import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
import PySimpleGUI as sg


def neg(source):
    img = cv2.imread(source, 0)
    height = img.shape[0]
    width = img.shape[1]
    n_img = np.zeros([height, width])
    for i in range(height):
        for j in range(width ):
            n_img[i, j] = abs(255 - img[i, j])

    fig = plt.figure(figsize=(10, 7))
    fig.add_subplot(2, 1, 1)
    plt.imshow(n_img, cmap='gray')
    fig.add_subplot(2, 1, 2)
    plt.hist(n_img.ravel(), 256, [0, 256])
    plt.show()


def prog2(source, min_val, max_val, is_bin):
    if is_bin:
        prog_bin(source, min_val, max_val)
    else:
        prog_nonbin(source, min_val, max_val)


def prog1(source, val, is_bin):
    img = cv2.imread(source, 0)
    height = img.shape[0]
    width = img.shape[1]
    n_img = np.zeros([height, width])

    if is_bin:
        for i in range(height):
            for j in range(width):
                if img[i, j] <= val:
                    n_img[i, j] = 0
                elif img[i, j] >= val:
                    n_img[i, j] = 255
                else:
                    n_img[i, j] = img[i, j]
    else:
        for i in range(height):
            for j in range(width):
                if img[i, j] <= val:
                    n_img[i, j] = 0
                elif img[i, j] >= val:
                    n_img[i, j] = img[i, j]
                else:
                    n_img[i, j] = img[i, j]

    fig = plt.figure(figsize=(10, 7))
    fig.add_subplot(2, 1, 1)
    plt.imshow(n_img, cmap='gray')
    fig.add_subplot(2, 1, 2)
    plt.hist(n_img.ravel(), 256, [0, 256])
    plt.show()


def prog_nonbin(source, min_val, max_val):
    img = cv2.imread(source, 0)
    height = img.shape[0]
    width = img.shape[1]
    n_img = np.zeros([height, width])
    for i in range(height):
        for j in range(width):
            if img[i, j] <= min_val:
                n_img[i, j] = min_val
            elif img[i, j] >= max_val:
                n_img[i, j] = max_val
            else:
                n_img[i, j] = img[i, j]

    fig = plt.figure(figsize=(10, 7))
    fig.add_subplot(2, 1, 1)
    plt.imshow(n_img, cmap='gray')
    fig.add_subplot(2, 1, 2)
    plt.hist(n_img.ravel(), 256, [0, 256])
    plt.show()



def prog_bin(source, min_val, max_val):
    img = cv2.imread(source, 0)
    height = img.shape[0]
    width = img.shape[1]
    n_img = np.zeros([height, width])
    for i in range(height):
        for j in range(width):
            if img[i, j] <= min_val:
                n_img[i, j] = 0
            elif img[i, j] >= max_val:
                n_img[i, j] = 255
            else:
                n_img[i, j] = img[i, j]

    fig = plt.figure(figsize=(10, 7))
    fig.add_subplot(2, 1, 1)
    plt.imshow(n_img, cmap='gray')
    fig.add_subplot(2, 1, 2)
    plt.hist(n_img.ravel(), 256, [0, 256])
    plt.show()
