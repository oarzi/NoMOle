from WorkingPys.CutPic import cut_images
from WorkingPys.K2means import k2means_on_array

print("NoMOle - start image processing")

######################################################################

print("cuting malignant images")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignant"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignantcut"
#cut_images(input_path, output_path)

print("cuting benign images")
input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benign"
output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benigncut"
cut_images(input_path, output_path)


######################################################################
#print("K2means on malignant moles")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\malignantcut"
#output_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\malignant\k2m-malignant"
#k2means_on_array(input_path, output_path)


#print("K2means on benign moles")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benigncut"
#output_path = r"C\:\\Users\ofir arzi\Dropbox\\NoMolePic\benign\k2m-benign\\"
#k2means_on_array(input_path, output_path)

#########################################################################

