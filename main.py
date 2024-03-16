from pathlib import Path
import cv2
import numpy as np
from helper_functions.show_image import show_image_resized
from plot_functions.rgb_hsv_image_plotter import plot_pixels_RGB, plot_pixels_hsv
from thresholding_functions.dbscan_clustering import perform_dbscan_clustering


folder_path = Path("./display_images")

for img_path in folder_path.rglob("*.*"):
    print(img_path)
    if "retina" in img_path.name:
        source_img = cv2.imread(img_path.as_posix())
        width = source_img.shape[1] // 2
        height = source_img.shape[0] // 2
        resized_image = cv2.resize(source_img, (width, height))
        # show_image_resized(img=source_img)
        # plot_pixels_RGB(img_path)
        # plot_pixels_hsv(img_path)
        pixel_values = resized_image.reshape((-1, 3)).astype(np.float32)

        # Define the number of clusters (K)
        K = 4

        # Apply K-means clustering
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(pixel_values, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Convert the centers to uint8
        centers = np.uint8(centers)

        print(centers)
        # Assign each pixel to its nearest cluster centroid
        segmented_image = centers[labels.flatten()]

        # Reshape the segmented image back to the original shape
        segmented_image = segmented_image.reshape(resized_image.shape)

        # Convert the segmented image to grayscale
        gray_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)

        # Threshold the grayscale image to create a binary mask for each cluster
        _, binary_image = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)

        # Find contours in the binary images
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours on the original image
        output_image = resized_image.copy()
        cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)

        # Display the result
        cv2.imshow('Contours', output_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
