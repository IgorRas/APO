import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import cv2
import PySimpleGUI as sg
from PIL import Image


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
        kernelx = np.array([[-1, -1, -1],
                            [0, 0, 0],
                            [1, 1, 1]])
        kernely = np.array([[1, 1, 1],
                            [0, 0, 0],
                            [-1, -1, -1]])
        abs_grad_x = cv2.filter2D(img, -1, kernelx)
        abs_grad_y = cv2.filter2D(img, -1, kernely)

        height = img.shape[0]
        width = img.shape[1]
        n_img = np.zeros([height, width])
        for i in range(height):
            for j in range(width):
                n_img[i, j] = (abs_grad_x[i, j] + abs_grad_y[i, j])
        abs_n_img = cv2.convertScaleAbs(n_img)
        cv2.imshow('Gradient', abs_n_img)

    if canny:
        layout = [
            [sg.Text('Próg min:'), sg.InputText(size=(4, 10))],
            [sg.Text('Próg max:'), sg.InputText(size=(4, 10))],
            [sg.Submit()]
        ]
        n_window = sg.Window('Podaj dane', layout)
        event, values = n_window.read()
        mini = int(values[0])
        maxi = int(values[1])
        n_window.close()
        grad = cv2.Canny(img, mini, maxi)
        cv2.imshow('Gradient', grad)


def thresholding_interactive(source, options):
    img = cv2.imread(source, 0)
    otsu = options[0]
    adaptive = options[1]

    if otsu:
        tht, img1 = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)

        fig = plt.figure(figsize=(10, 7))
        fig.add_subplot(2, 1, 1)
        plt.imshow(img, cmap='gray')
        fig.add_subplot(2, 2, 1)
        plt.imshow(img1, cmap='gray')
        fig.add_subplot(2, 1, 2)
        plt.hist(img1.ravel(), 256, [0, 256])
        plt.show()
    if adaptive:
        layout = [
            [sg.Radio('Mean', "RADIO1", default=True),
             sg.Radio('Gaussian', "RADIO1", default=False)],
            [sg.Submit()]
        ]
        n_window = sg.Window('Podaj dane', layout)
        event, values = n_window.read()
        mean = values[0]
        gaussian = values[1]
        n_window.close()
        if mean:
            img1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY, 5, 0)
        else:
            img1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)

        fig = plt.figure(figsize=(10, 7))
        fig.add_subplot(2, 1, 1)
        plt.imshow(img, cmap='gray')
        fig.add_subplot(2, 2, 1)
        plt.imshow(img1, cmap='gray')
        fig.add_subplot(2, 1, 2)
        plt.hist(img1.ravel(), 256, [0, 256])
        plt.show()
