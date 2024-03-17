import cv2
import numpy as np


def create_image_segmentation(img, centers, labels):
    cluster_images = dict()
    for i, center in enumerate(centers):
        # Create a mask for the current cluster by mapping with respective label
        mask = (labels == i).reshape(img.shape[:2])

        # Create an image with only pixels corresponding to the current cluster center
        cluster_image = np.zeros_like(img)
        cluster_image[mask] = img[mask]

        if np.all(center < 100):
            color = "background"
        else:
            indices = np.where(center > 150)
            if indices[0] == 0:
                color = "blue"
            elif indices[0] == 1:
                color = "green"
            elif indices[0] == 2:
                color = "red"

        # Append the cluster image to the list of cluster images
        cluster_images[color] = cluster_image

    # Display the four cluster images
    for k, cluster_image in cluster_images.items():
        cv2.imshow(f'Original image {k} pixels', cluster_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return cluster_images
