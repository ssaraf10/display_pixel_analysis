import cv2
from helper_functions.contour_stats import find_contour_stats
from pixels_analyzer.filter_pixels_by_area import filter_contours_by_area


def find_pixel_contours(img, conversion_factor, color):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image to create a binary mask for each cluster
    _, binary_image = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by size
    filtered_contours, pixel_coords = filter_contours_by_area(contours)

    # Display contours on top image
    contour_image = cv2.drawContours(img.copy(), filtered_contours, -1, (0, 255, 0), 3)
    # # Display the original image with contours
    # cv2.imshow(f'{color}', contour_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return filtered_contours, pixel_coords, contour_image
