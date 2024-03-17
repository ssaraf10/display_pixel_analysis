import numpy as np
from helper_functions.contour_stats import find_contour_stats


def filter_contours_by_area(contours_unfiltered):
    contours_size = []
    contours_dict = dict()
    contours_size_dict = dict()
    contour_coords = []
    for i, cnt in enumerate(contours_unfiltered):
        stats = find_contour_stats(cnt)
        if stats["area"] > 500:
            contours_size.append(stats["area"])
            contours_size_dict[i] = stats["area"]
            contours_dict[i] = cnt
            Cx, Cy = stats["center"]
            width = stats["width"]
            height = stats["height"]
            contour_coords.append([Cx, Cy, width, height])

    # contours_size = np.array(contours_size)
    # range_contours_size = np.ptp(contours_size)
    # print(f"range of contours area: {range_contours_size}")
    # percentile_value = np.percentile(contours_size, 50)

    filtered_contours = []
    for k, v in contours_size_dict.items():
        # print(f"Key is {k}, and Value is {v}")
        if v >= 500:
            filtered_contours.append(contours_dict[k])

    contour_coords = np.array(contour_coords)
    return filtered_contours, contour_coords
