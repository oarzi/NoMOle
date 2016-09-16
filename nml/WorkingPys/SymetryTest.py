import cv2
import os
import concurrent.futures
import numpy as np


def symetry_test(input_path):
    imgs = os.listdir(input_path)
    #names = [create_pic_name(filename, 'k2m', output_path + '\\')    for filename in os.listdir(input_path)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        symvals = [(image, executor.submit(pic_symetry_test, input_path + '\\' + image).result())   for image in imgs]

    #symvals = [pic_symetry_test(input_path + '\\' + pair[1], pair[0]) for pair in z]

    symvals = np.asarray(symvals)

    return symvals


def pic_symetry_test(imagepath):
    print(imagepath)
    img = cv2.imread(imagepath)
    #print(img.shape)

    x0, y0, z0 = img.shape

    left = img[:, 0:round(y0 / 2)]
    if round(y0 / 2) < y0 - round(y0 / 2):
        right = img[:, round(y0 / 2): (y0 - 1)]
    elif round(y0 / 2) > y0 - round(y0 / 2):
        right = img[:, round(y0 / 2):y0]
        left = img[:, 0:(round(y0 / 2) - 1)]
    else:
        right = img[:, round(y0 / 2):y0]

    flipped = cv2.flip(right, 1)

    #print(right.shape)
    #print(flipped.shape)
    diff = left - flipped

    diff_pixels = diff.reshape(-1, 3)
    sym = np.mean(diff_pixels)

    return sym



