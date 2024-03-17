from pathlib import Path
import cv2
import numpy as np
from helper_functions.resize_image import create_resized_image
from plot_functions.cross_marker_plotter import show_cross_markers
from scale_bar.scale_bar_points import obtain_two_points


def euclidian_distance(point1, point2):
    # Calculate the Euclidean distance between the two points
    distance = np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    print("Euclidean distance between selected points:", distance)
    return distance


def pixel_distance_to_um_conversion(img):
    # Obtain scale bar endpoints pixel coordinates
    point_1, point_2 = obtain_two_points(img)

    # Show selected cross-markers on original image
    show_cross_markers(img, point_1, point_2)

    # Calculate the distance between those 2 pixel coordinates
    pixel_distance = euclidian_distance(point1=point_1, point2=point_2)

    # Manually enter the scale bar value from the image
    scale_bar_value = float(input("Enter Scale Bar Value: "))

    # Convert pixels to microns
    conversion_factor_to_um = scale_bar_value / pixel_distance
    return conversion_factor_to_um


def main():
    folder_path = Path("../display_images")
    print(folder_path)
    for img_path in folder_path.rglob("*.jpg"):
        if "retina" in img_path.name:
            print(img_path)
            source_img = cv2.imread(img_path.as_posix())
            # Reduce image size by 50%
            resized_img = create_resized_image(source_img)

            # Calculate the pixel_to_um conversion factor
            conversion_factor = pixel_distance_to_um_conversion(resized_img)
            print(f"Calculated conversion factor is: 1 pixel = {round(conversion_factor, 2)} um")


if __name__ == "__main__":
    main()
