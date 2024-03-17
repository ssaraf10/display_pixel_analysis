import cv2
import numpy as np


def find_contour_stats(cnt):
    stats = dict()
    rect = cv2.minAreaRect(cnt)
    stats["center"], size, angle = rect
    width, height = size
    stats["width"] = width
    stats["height"] = height
    stats["size"] = (width+height)/2
    stats["area"] = cv2.contourArea(cnt)
    # stats["box"] = np.intp(cv2.boxPoints(cnt))

    return stats
