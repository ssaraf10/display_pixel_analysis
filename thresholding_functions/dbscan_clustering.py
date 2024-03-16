import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


def perform_dbscan_clustering(image):
    img_reshape = image.reshape((-1, 3))

    # Standardize the pixel values
    img_reshape = StandardScaler().fit_transform(img_reshape.astype(float))

    # Perform DBSCAN clustering
    db = DBSCAN(eps=0.3, min_samples=50).fit(img_reshape)
    labels = db.labels_

    # Extract contours from clustered regions
    contours = []
    for label in np.unique(labels):
        if label == -1:
            continue  # Skip noise points
        mask = (labels == label)
        _, cnts, _ = cv2.findContours(np.uint8(mask.reshape(image.shape[:-1])), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours.extend(cnts)

    # Draw contours on the original image
    output_image = image.copy()
    cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Contours', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
