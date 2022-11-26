import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
import cv2


def edges(source, options):
    img = cv2.imread(source, 0)
    sobel = options[0]
    prewitt = options[1]
    canny = options[2]

    if sobel:
        ddepth = cv2.CV_16S
        grad_x = cv2.Sobel(img, ddepth, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(img, ddepth, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)

        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

        cv2.imshow('Gradient', grad)

    if prewitt:
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        abs_grad_x = cv2.filter2D(img, -1, kernelx)
        abs_grad_y = cv2.filter2D(img, -1, kernely)

        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        cv2.imshow('Gradient', grad)

    if canny:
        grad = cv2.Canny(img, 100, 200)
        cv2.imshow('Gradient', grad)

