from WorkingPys.K2means import extract_mole_grayscale
from WorkingPys.SymetryTest import pic_symetry_test

import os

def analyze_mole(image_path):
    extract_mole_grayscale(imagepath=image_path,
                           imagename=r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\analyze\temp")

    symval = pic_symetry_test(r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\analyze\temp")

    os.remove(r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\analyze\temp")

    return abs(symval - 91.21) > abs(symval - 104.75)