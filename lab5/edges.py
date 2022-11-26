import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
import cv2
import PySimpleGUI as sg


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

        grad = cv2.addWeighted(abs_grad_x, 1, abs_grad_y, 1, 0)
        cv2.imshow('Gradient', grad)

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

