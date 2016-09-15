import cv2
import os

from WorkingPys.CreatePicName import create_pic_name


def cut_images(input_path, output_path):
    cuts = [cut_image(input_path + '\\' + filename) for filename in os.listdir(input_path)]
    names = [create_pic_name(filename, 'cuts', output_path + '\\')
             for filename in os.listdir(input_path)]

    print(names)
    z = zip(names, cuts)

    [cv2.imwrite(pair[0], pair[1]) for pair in z]
    return True

def cut_image(imgpath):
    print(imgpath)
    img = cv2.imread(imgpath)
    #print(img.shape)
    x, y, z = img.shape
    img = img[round(0.09 * x): round(0.91 * x), round(0.09 * y): round(0.91 * y)]

    return img