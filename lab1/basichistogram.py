import matplotlib.pyplot as plt
import cv2
from PIL import Image


def hist_mono(source):

    fig = plt.figure(figsize=(10, 7))
    rows = 2
    columns = 1

    img = cv2.imread(source, 0)
    # original image
    fig.add_subplot(rows, columns, 1)
    plt.title('Original image')
    plt.imshow(img, cmap="gray")

    # histogram of image
    fig.add_subplot(rows, columns, 2)
    plt.title('Histogram')

    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def hist_color1(source):  # openCV
    img = cv2.imread(source)
    fig = plt.figure(figsize=(10, 7))
    rows = 4
    columns = 1

    # Calculate histogram without mask
    hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img], [1], None, [256], [0, 256])
    hist3 = cv2.calcHist([img], [2], None, [256], [0, 256])

    fig.add_subplot(rows, columns, 1)
    plt.title('Original image')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    fig.add_subplot(rows, columns, 2)
    plt.plot(hist1, color='darkblue'),
    fig.add_subplot(rows, columns, 3)
    plt.plot(hist2, color="green"),
    fig.add_subplot(rows, columns, 4)
    plt.plot(hist3, color="red")

    plt.show()


def hist_color(source):
    img = Image.open(source)
    fig = plt.figure(figsize=(10, 10))
    rows = 4
    columns = 1

    # Calculate histogram without mask
    histogram = img.histogram()
    hist1 = histogram[0:256]
    hist2 = histogram[256:512]
    hist3 = histogram[512:768]

    fig.add_subplot(rows, columns, 1)
    plt.title('Original image')
    plt.imshow(img)
    fig.add_subplot(rows, columns, 2)
    for i in range(0, 256):
        plt.bar(i, hist1[i], color="red", edgecolor="red")
    fig.add_subplot(rows, columns, 3)
    for i in range(0, 256):
        plt.bar(i, hist2[i], color="green", edgecolor="green")
    fig.add_subplot(rows, columns, 4)
    for i in range(0, 256):
        plt.bar(i, hist3[i], color="darkblue", edgecolor="darkblue")

    plt.show()
