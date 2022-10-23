import cv2
import sys

im_gray = cv2.imread('C:/Users/Igor/Desktop/APO/images/Mona_Lisa_GS2.jpg', cv2.IMREAD_GRAYSCALE)
im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_RAINBOW)
while True:
    cv2.imshow("Colored", im_color)
    cv2.waitKey(0)
    sys.exit()  # to exit from all the processes
