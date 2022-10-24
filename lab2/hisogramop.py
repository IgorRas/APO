import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
import os


def roz_hist(source, a, b):
    img = plt.imread(source)
    img_cv2 = cv2.imread(source)
    height = img.shape[0]
    width = img.shape[1]
    img_ar = np.zeros([height, width])
    for i in range(height):
        for j in range(width):
            img_ar[i][j] = ((img[i][j]-a)*(1/(b-a)))

    name = os.path.basename(source)[:-4]
    new_filename = f'copied/{name + str(np.random.randint(1, 100))}.png'
    plt.imsave(new_filename, img, cmap='gray')
    temp_img = plt.imread(new_filename)
    temp_img2 = np.round(temp_img * 256)
    print(new_filename)

    fig = plt.figure(figsize=(10, 7))
    rows = 3
    columns = 1

    fig.add_subplot(rows, columns, 1)
    plt.imshow(img_cv2, cmap='gray')

    fig.add_subplot(rows, columns, 2)
    plt.imshow(temp_img, cmap='gray')

    fig.add_subplot(rows, columns, 3)
    plt.hist(temp_img2.ravel(), 256, [0, 255])
    plt.show()
