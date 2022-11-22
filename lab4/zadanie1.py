import cv2
import numpy as np
import matplotlib.pyplot as plt


def smoothing( source, options):
    img = cv2.imread(source, -1)
    sred = options[3]
    sred_z_wag = options[4]
    gauss = options[5]
    border_constant = options[7]
    border_reflect = options[8]
    border_wrap = options[9]

    mask = np.zeros([3, 3])

    if sred:
        for i in range(3):
            for j in range(3):
                mask[i][j] = 1

    if sred_z_wag:
        waga = options[6]
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    mask[i][j] = waga
                else:
                    mask[i][j] = 1

    if gauss:
        mask = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

    mask = mask.astype(float)/9

    if border_constant:
        constant = int(options[10])
        image = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=constant)
        fin = cv2.filter2D(image, -1, mask)
    if border_reflect:
        fin = cv2.filter2D(img, -1, mask, borderType=cv2.BORDER_REFLECT)
    if border_wrap:
        image = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_WRAP)
        fin = cv2.filter2D(image, -1, mask)

    print(mask)

    fin = cv2.cvtColor(fin, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(fin), plt.title('After')
    plt.xticks([]), plt.yticks([])
    plt.show()


def sharpen(source, options):
    img = cv2.imread(source, -1)
    lap1 = options[3]
    lap2 = options[4]
    lap3 = options[5]
    border_constant = options[6]
    border_reflect = options[7]
    border_wrap = options[8]

    mask = np.zeros([3, 3])

    if lap1:
        mask = np.array([[0, -1, 0],
                         [-1, 5, -1],
                         [0, -1, 0]])

    if lap2:
        mask = np.array([[-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]])

    if lap3:
        mask = np.array([[1, -2, 1],
                         [-2, 5, -2],
                         [1, -2, 1]])

    if border_constant:
        constant = int(options[9])
        image = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=constant)
        fin = cv2.filter2D(image, -1, mask)
    if border_reflect:
        fin = cv2.filter2D(img, -1, mask, borderType=cv2.BORDER_REFLECT)
    if border_wrap:
        image = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_WRAP)
        fin = cv2.filter2D(image, -1, mask)

    print(mask)

    fin = cv2.cvtColor(fin, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(fin), plt.title('After')
    plt.xticks([]), plt.yticks([])
    plt.show()


def edges(source, options):
    img = cv2.imread(source, -1)
    directions = np.zeros(8)
    for i in range(8, 16):
        directions[i-8] = options[i]
    border_constant = options[16]
    border_reflect = options[17]
    border_wrap = options[18]

    masks = np.array([[[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]],
                   [[-2, -1, 0],
                    [-1, 0, 1],
                    [0, 1, 2]],
                   [[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]],
                   [[0, -1, -2],
                    [1, 0, -1],
                    [2, 1, 0]],
                   [[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]],
                   [[2, 1, 0],
                    [-1, 0, -1],
                    [0, -1, -2]],
                   [[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]],
                   [[0, 1, 2],
                    [-1, 0, 1],
                    [-2, -1, 0]]
                   ])

    index = np.where(directions == True)
    mask = np.array(masks[index])
    mask.shape = (3, 3)
    print(mask)

    if border_constant:
        constant = int(options[19])
        image = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=constant)
        fin = cv2.filter2D(image, -1, mask)
    if border_reflect:
        fin = cv2.filter2D(img, -1, mask, borderType=cv2.BORDER_REFLECT)
    if border_wrap:
        image = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_WRAP)
        fin = cv2.filter2D(image, -1, mask)

    fin = cv2.cvtColor(fin, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(fin), plt.title('After')
    plt.xticks([]), plt.yticks([])
    plt.show()

