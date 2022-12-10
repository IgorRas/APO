import cv2
import numpy as np


def erosion(source):
    img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
    im_bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((3, 3), np.uint8)
    erosion1 = cv2.morphologyEx(im_bw, cv2.MORPH_ERODE, kernel)
    cv2.imshow('Original', im_bw)
    cv2.imshow('Erosion', erosion1)


def dilate(source):
    img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
    im_bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((3, 3), np.uint8)
    erosion1 = cv2.morphologyEx(im_bw, cv2.MORPH_DILATE, kernel)
    cv2.imshow('Original', im_bw)
    cv2.imshow('Dilation', erosion1)


def open(source):
    img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
    im_bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((3, 3), np.uint8)
    erosion1 = cv2.morphologyEx(im_bw, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Original', im_bw)
    cv2.imshow('Opened', erosion1)


def close(source):
    img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
    im_bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((3, 3), np.uint8)
    erosion1 = cv2.morphologyEx(im_bw, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Original', im_bw)
    cv2.imshow('Closed', erosion1)
