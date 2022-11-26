import cv2
import numpy as np
import matplotlib.pyplot as plt


def median(source, options):
    img = cv2.imread(source, -1)
    border_constant = options[4]
    border_reflect = options[5]
    border_wrap = options[6]

    if options[0]:
        size = 3
        border = 1
    if options[1]:
        size = 5
        border = 2
    if options[2]:
        size = 7
        border = 3
    if options[3]:
        size = 9
        border = 4

    if border_constant:
        constant = int(options[7])
        image = cv2.copyMakeBorder(img, border, border, border, border, cv2.BORDER_CONSTANT, value=(constant, constant, constant))
        fin = cv2.medianBlur(image, size)
    if border_reflect:
        image = cv2.copyMakeBorder(img, border, border, border, border, cv2.BORDER_REFLECT)
        fin = cv2.medianBlur(image, size)
    if border_wrap:
        image = cv2.copyMakeBorder(img, border, border, border, border, cv2.BORDER_WRAP)
        fin = cv2.medianBlur(image, size)

    fin = cv2.cvtColor(fin, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(fin, cmap='gray'), plt.title('After')
    plt.xticks([]), plt.yticks([])
    plt.show()