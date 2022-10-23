import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np


def roz_hist(source, a=10, b=150):
    img = Image.open(source)

    for i in range(256):
        img.histogram()[i] = np.round(((img.histogram()[i]-a) * np.min(img.histogram()))/(b-a))
    for i in range(10, 150):
        plt.bar(i, img.histogram()[i], color="red", edgecolor="red")
    plt.show()
