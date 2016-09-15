import cv2
import os
import concurrent.futures
import numpy as np


def symetry_test(input_path):
    imgs = os.listdir(input_path)
    #names = [create_pic_name(filename, 'k2m', output_path + '\\')    for filename in os.listdir(input_path)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        symvals = [executor.submit(pic_symetry_test, input_path + '\\' + image).result()   for image in imgs]

    #symvals = [pic_symetry_test(input_path + '\\' + pair[1], pair[0]) for pair in z]

    return symvals


def pic_symetry_test(imagepath):
    print(imagepath)
    img = cv2.imread(imagepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(img.shape)

    x0, y0, z0 = img.shape
    right = img[:, 0:round(y0 / 2)]
    left = img[:, (round(y0 / 2) + 1):y0]
    left = cv2.remap(left, [x0-x for x in range(x0)], [y for y in range(y0)], cv2.INTER_LINEAR)

    diff = right - left

    diff_pixels = diff.reshape(-1, 3)
    sym = np.mean(diff_pixels)

    return sym



