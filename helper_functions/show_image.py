import cv2


def show_image_resized(img):
    height, width = img.shape[:2]
    ratio = height / width
    new_width = 1200
    new_height = int(new_width * ratio)

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image", new_width, new_height)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
