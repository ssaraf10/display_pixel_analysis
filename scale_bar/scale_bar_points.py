import cv2
import numpy as np
from pathlib import Path


# Global variables to store the selected points
point1 = None
point2 = None

# Mouse click event callback function
def mouse_click(event, x, y, flags, param):
    global point1, point2

    # If left mouse button is clicked, record the coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        if point1 is None:
            point1 = (x, y)
        elif point2 is None:
            point2 = (x, y)


def obtain_two_points(img):
    cv2.imshow('Select Two Points', img)
    cv2.setMouseCallback('Select Two Points', mouse_click)

    # Loop to select two endpoints of scale bar
    while True:
        if point1 is not None and point2 is not None:
            break
        cv2.waitKey(10)

    print(f"Point 1: {point1}, Point 2: {point2}")

    return point1, point2


# # Create a line between the two points
# line_mask = np.zeros_like(image)
# cv2.line(line_mask, point1, point2, (255, 255, 255), thickness=1)
#
# # Find non-zero pixels in the line mask
# num_pixels = np.count_nonzero(line_mask[:,:,0])
#
# print("Total number of pixels between selected points:", num_pixels)
#
# # Display the line on the image
# line_image = cv2.addWeighted(image, 0.7, line_mask, 0.3, 0)
# cv2.imshow('Line Between Points', line_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
