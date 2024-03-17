from pathlib import Path
import cv2
import numpy as np

from helper_functions.resize_image import create_resized_image
from helper_functions.show_image import show_image_resized
from plot_functions.rgb_hsv_image_plotter import plot_pixels_RGB, plot_pixels_hsv
from thresholding_functions.dbscan_clustering import perform_dbscan_clustering
from thresholding_functions.image_segmentation_RGB import create_image_segmentation
from thresholding_functions.k_means_clustering import find_pixels_k_clusters

folder_path = Path("./display_images")

for img_path in folder_path.rglob("*.jpg"):
    if "retina" in img_path.name:
        print(img_path)
        # Load the original image
        source_img = cv2.imread(img_path.as_posix())
        # Size of the original image:
        print(f"Size of the original image: {source_img.size}")

        # Reduce size of image by 50%
        resized_image = create_resized_image(source_img)
        print(f"Size of the original image: {resized_image.size}")

        # plot_pixels_RGB(img_path)
        # plot_pixels_hsv(img_path)

        # Find 4 Clusters of pixel colors in the image corresponding to Background, Red, Blue, and Green pixels
        labels, centers = find_pixels_k_clusters(img=resized_image, num_clusters=4)

        # Find segmented images corresponding to R, G, and B pixels:
        rgb_image_dict = create_image_segmentation(resized_image, centers, labels)
