import cv2
import os
from WorkingPys.K2means import extract_mole_grayscale
from WorkingPys.CreatePicName import create_pic_name
from cvToPyPlot import cv_to_pyplot
from matplotlib import pyplot as plt
from WorkingPys.SymetryTest import pic_symetry_test
import concurrent
import numpy as np


#input_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\malignant"
#imgs = os.listdir(input_path)
#output_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\malignant-grey"
#names = [create_pic_name(filename, 'grey', output_path + '\\')
#         for filename in os.listdir(input_path)]

#z = zip(names, imgs)

#[extract_mole_grayscale(input_path + '\\' + pair[1], pair[0]) for pair in z]

#input_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\benign"
#imgs = os.listdir(input_path)
#output_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\benign-grey"
#names = [create_pic_name(filename, 'grey', output_path + '\\')
#         for filename in os.listdir(input_path)]

#z = zip(names, imgs)

#[extract_mole_grayscale(input_path + '\\' + pair[1], pair[0]) for pair in z]


#####################################
#input_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\malignant-grey\m1grey.jpg"

img = cv2.imread(input_path)
print(img.shape)

x0, y0, z0 = img.shape
right = img[:, 0:round(y0 / 2)]
left = img[:, (round(y0 / 2) + 1):y0]
left = cv2.remap(left, [x0 - x for x in range(x0)], [y for y in range(y0)], cv2.INTER_LINEAR)


plt.subplot(211), plt.imshow(cv_to_pyplot(img)),plt.title('ORIGINAL')
plt.subplot(212), plt.imshow(cv_to_pyplot(left)), plt.title('LEFT')

plt.show()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

diff = right - left
diff_pixels = diff.reshape(-1, 3)
sym = np.mean(diff_pixels)


input_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\malignant-grey"
imgs = os.listdir(input_path)
names = [create_pic_name(filename, 'grey', output_path + '\\')
         for filename in os.listdir(input_path)]

z = zip(names, imgs)

symvals = [pic_symetry_test(input_path + '\\' + pair[1], pair[0]) for pair in z]