from WorkingPys.K2means import k2means_on_array

print("NoMOle - start image processing")

######################################################################

print("K2means on malignant moles")
input_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\malignant"
output_path = r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\malignant"
k2means_on_array(input_path, output_path)


#print("K2means on benign moles")
#input_path = r"C:\Users\ofir arzi\Dropbox\NoMolePic\benign\benign\\"
#output_path = r"C\:\\Users\ofir arzi\Dropbox\\NoMolePic\benign\k2m-benign\\"
#k2means_on_array(input_path, output_path)

#########################################################################

