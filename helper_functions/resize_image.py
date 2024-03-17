import cv2


def create_resized_image(img):
    # Resize the image by 50% reduction
    width = img.shape[1] // 2
    height = img.shape[0] // 2
    resized_image = cv2.resize(img, (width, height))

    return resized_image
