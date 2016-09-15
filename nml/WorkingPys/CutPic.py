import cv2
import os

from WorkingPys.CreatePicName import create_pic_name


def cut_images(input_path, output_path):
    imgs = os.listdir(input_path)
    names = [create_pic_name(filename, 'cut', output_path + '\\')
             for filename in os.listdir(input_path)]

    z = zip(names, imgs)

    [cut_image(input_path + '\\' + pair[1], pair[0]) for pair in z]

    return True


def cut_image(imgpath, imagename):
    print(imgpath)
    print(imagename)
    img = cv2.imread(imgpath)
    #print(img.shape)
    x, y, z = img.shape
    img = img[round(0.09 * x): round(0.91 * x), round(0.09 * y): round(0.91 * y)]
    cv2.imwrite(imagename, img)

    return True