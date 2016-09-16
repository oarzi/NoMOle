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
print("K2means on malignant moles")
#input_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\malignant"
#output_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\k2m-malignant"
#kmeans_on_array(input_path, output_path, 2, 'k2m')


print("K2means on benign moles")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benigncut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benign-k2m"
#kmeans_on_array(input_path, output_path, 2, 'k2m')

#########################################################################

print("malignant - color to grey scale")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignantcut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignant-grey"

#extraxt_mole_grayscale_array(input_path, output_path)

print("benign - color to grey scale")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benigncut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benign-grey"

#extraxt_mole_grayscale_array(input_path, output_path)


#########################################################################

#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignant-grey"

#malignant_symvals = symetry_test(input_path)
#f = open('MalignantSymetryValues.csv', 'a')
#[(f.write(x + ',' + y + '\n')) for x, y in malignant_symvals] average: 91.21

#print("Malignant symetry values shape:", malignant_symvals.shape)


#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benign-grey"

#benign_symvals = symetry_test(input_path)
#f = open('BenignSymetryValues.csv', 'a')
#[(f.write(x + ',' + y + '\n')) for x, y in benign_symvals] average: 104.75

#print("Benign symetry values shape:", benign_symvals.shape)


##########################################################################


###########################################################################

print("K3means on malignant moles")
#input_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\malignant"
#output_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\k3m-malignant"
#kmeans_on_array(input_path, output_path, 3, 'k3m')


print("K3means on benign moles")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benigncut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\k2m-benign"
#kmeans_on_array(input_path, output_path,2)



#############################################################################