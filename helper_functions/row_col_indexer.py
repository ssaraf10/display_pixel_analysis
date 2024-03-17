import numpy as np


def sort_array(arr, column_number):
    sorted_coords = arr[arr[:, column_number].argsort()]
    return sorted_coords


def add_rowcol_index(arr, column_number):
    threshold = 5
    a = arr[:, column_number]
    b = np.hstack((arr[:1, column_number], arr[:-1, column_number]))
    diff = np.abs(a-b) > threshold
    result_array = np.zeros(diff.shape)
    counter = 0

    for i, value in enumerate(diff):
        if value:
            counter += 1
        result_array[i] = counter

    if result_array[:1][0] == 0:
        result_array = result_array+1

    arr = np.column_stack((arr, result_array))

    return arr
