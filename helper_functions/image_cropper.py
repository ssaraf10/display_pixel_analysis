def crop_img(source_img, TL_coord, BR_coord, offset):
    cropped_img = source_img[TL_coord[1]-offset:BR_coord[1]+offset, TL_coord[0]-offset:BR_coord[0]+offset]

    return cropped_img
