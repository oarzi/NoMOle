from WorkingPys.CutPic import cut_images
from WorkingPys.K2means import *
from WorkingPys.SymetryTest import symetry_test

print("NoMOle - start image processing")

######################################################################

print("cuting malignant images")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignant"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignantcut"
#cut_images(input_path, output_path)

print("cuting benign images")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benign"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benigncut"
#cut_images(input_path, output_path)


######################################################################
#print("K2means on malignant moles")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignantcut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\k2m-malignant"
#k2means_on_array(input_path, output_path)


#print("K2means on benign moles")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benigncut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\k2m-benign"
#k2means_on_array(input_path, output_path)

#########################################################################

#print("malignant - color to grey scale")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignantcut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignant-grey"

#extraxt_mole_grayscale_array(input_path, output_path)

#print("benign - color to grey scale")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benigncut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benign-grey"

#extraxt_mole_grayscale_array(input_path, output_path)


#########################################################################

#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignant-grey"

#malignant_symvals = symetry_test(input_path)
#f = open('MalignantSymetryValues.csv', 'a')
#[(f.write(x + ',' + y + '\n')) for x, y in malignant_symvals]

#print("Malignant symetry values shape:", malignant_symvals.shape)


#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benign-grey"

#benign_symvals = symetry_test(input_path)
#f = open('BenignSymetryValues.csv', 'a')
#[(f.write(x + ',' + y + '\n')) for x, y in benign_symvals]

#print("Benign symetry values shape:", benign_symvals.shape)

