import cv2
import numpy as np

#
#def moment(source):
#    img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
#    im_bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
#
#    ret, thresh = cv2.threshold(im_bw, 170, 255, 0)
#    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#    print("Number of Contours detected:", len(contours))
#    for i, cnt in enumerate(contours):
#        M = cv2.moments(cnt)
#        print(f"Moments of Contour {i + 1}:", M)


def moment(source):
    img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
    im_bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    csv = np.empty([3, 11])
    for i, cnt in enumerate(contours):
        M = cv2.moments(cnt)
        m1 = M["nu20"] + M["nu02"]
        m2 = (M["nu20"] - M["nu20"])**2 + 4*M["nu11"]**2
        m3 = (M["nu30"] - M["nu12"])**2 + (3*M["nu21"] - M["nu03"])**2
        print(m1)
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        w1 = 2 * (area/np.pi)**(1/2)
        w2 = perimeter/np.pi
        w3 = (perimeter / (2 * (area*np.pi)**(1/2))) - 1
        w9 = (2*(np.pi*area))/perimeter
        hull = cv2.convexHull(cnt)
        hull_area = cv2.contourArea(hull)
        w10 = float(area) / hull_area
        w11 = np.sqrt(4 * area / np.pi)
        csv[i] = [m1, m2, m3, area, perimeter, w1, w2, w3, w9, w10, w11]
        print(w1)

    np.savetxt("copied/foo.csv", csv, delimiter=",")
