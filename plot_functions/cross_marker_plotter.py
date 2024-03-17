import cv2


def draw_cross_marker(point, img):
    x, y = point
    cv2.line(img, (x - 10, y), (x + 10, y), (0, 0, 255), 2)
    cv2.line(img, (x, y - 10), (x, y + 10), (0, 0, 255), 2)

    return img


def show_cross_markers(img, point1, point2):
    img = draw_cross_marker(point1, img)
    img = draw_cross_marker(point2, img)
    cv2.imshow('Contours', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
