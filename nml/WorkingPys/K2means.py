import cv2
import os
import numpy as np
from WorkingPys.CreatePicName import create_pic_name


def k2means_on_array(input_path, output_path):
    k2ms = [k2means(input_path + '\\' + filename) for filename in os.listdir(input_path)]
    names = [create_pic_name(filename, 'k2m', output_path + '\\')
             for filename in os.listdir(input_path)]
    '''files = os.listdir(input_path)
    k2ms = k2means(input_path + '\\' + files[137])
    names = create_pic_name(files[137], 'k2m', output_path)'''

    z = zip(names, k2ms)

    [cv2.imwrite(pair[0], pair[1]) for pair in z]
    return True


def k2means(imgpath):
    print(imgpath)
    img = cv2.imread(imgpath)
    #print(img.shape)
    x, y, z = img.shape
    img = img[round(0.1 * x): round(0.9 * x), round(0.1 * y): round(0.9 * y)]
    #print(img.shape)
    z = img.reshape((-1,3))

    # convert to np.float32
    z = np.float32(z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    ret,label,center=cv2.kmeans(z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    return res2
