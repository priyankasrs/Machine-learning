from PIL import Image
import numpy as np 
def entropy(image):
	dim = image.size
	out_image = np.reshape(image,(1,dim[0]*dim[1]))
	dim2 = out_image.size
	out_image = out_image[0]
	symset = list(set(out_image))
	numsim = len(symset)
	probab = [np.size(out_image[out_image == i])/(1.0*dim2) for i in symset]
	ent = np.sum([p*np.log2(1.0/p) for p in probab])
	print ent

im = Image.open("lenaOp1.png").convert("L")
entropy(im)