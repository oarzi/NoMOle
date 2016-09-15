import cv2
import os
import numpy as np
import concurrent.futures
from WorkingPys.CreatePicName import create_pic_name


def k2means_on_array(input_path, output_path):
    imgs = os.listdir(input_path)
    names = [create_pic_name(filename, 'k2m', output_path + '\\')
             for filename in os.listdir(input_path)]

    z = zip(names, imgs)

    [k2means(input_path + '\\' + pair[1], pair[0]) for pair in z]

    return True

def do_k2_means(imgpath, imgname):
    print(imgpath)
    print(imgname)

    img = cv2.imread(imgpath)
    x, y, z = img.shape  # height X width X RGB
    z = img.reshape((-1, 3))  # height * width X RGB

    # convert to np.float32
    z = np.float32(z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    ret, label, center = cv2.kmeans(z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    #label: height * width X 1

    return ret, label, center


def k2means(imgpath, imgname):
    ret, label, center = do_k2_means(imgpath, imgname)
    img = cv2.imread(imgpath)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape(img.shape)

    cv2.imwrite(imgname, res2)
    return True


def extraxt_mole_grayscale_array(input_path, output_path):
    imgs = os.listdir(input_path)
    names = [create_pic_name(filename, 'grey', output_path + '\\')
             for filename in os.listdir(input_path)]

    z = zip(names, imgs)

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        [executor.submit(extract_mole_grayscale, input_path + '\\' + pair[1], pair[0]) for pair in z]

    #[extract_mole_grayscale(input_path + '\\' + pair[1], pair[0]) for pair in z]

    return True


def extract_mole_grayscale(imagepath, imagename):
    ret, label, center = do_k2_means(imagepath, imagename)

    img = cv2.imread(imagepath)
    z = img.reshape((-1, 3))
    # convert to np.float32
    z = np.float32(z)
    #ones = np.nonzero(label);
    #zeros = np.where(label == 0)

    #TODO - try enumerate
    x = list(enumerate(label))
    center_index1, center_label1 = x[round(len(x) / 2) - 25]
    center_index2, center_label2 = x[round(len(x) / 2)]
    center_index3, center_label3 = x[round(len(x) / 2) + 25]

    l = (center_label1[0] + center_label2[0] + center_label3[0])/3
    l = l > 0.5
    pick_label = 1 - l

    for index, pixel in x:
        if pixel[0] == pick_label:
           z[index] = [255, 255, 255]

    filtered_image = z.reshape(img.shape)
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)



    # Now convert back into uint8, and make original image
    #center = np.uint8(center)
    #res = center[label.flatten()]
    #res2 = res.reshape(img.shape)

    cv2.imwrite(imagename, filtered_image)
    return True
