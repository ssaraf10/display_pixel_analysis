import cv2
import numpy as np


def find_pixels_k_clusters(img, num_clusters=4):
    pixel_values = img.reshape((-1, 3)).astype(np.float32)

    # Apply K-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert the centers to uint8
    centers = np.uint8(centers)

    print(f"Centers data: {centers}")
    # print(f"Labels data: {labels}, {labels.size}")
    return labels, centers
