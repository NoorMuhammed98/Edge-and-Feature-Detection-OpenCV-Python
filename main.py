import numpy as np
import cv2
from matplotlib import pyplot as plt
from copy import deepcopy

def wind(image):
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

crops=cv2.imread('crops.png',1)

edges=cv2.Canny(crops,100,200)
wind(edges)
