from PIL import Image
import numpy as np 
def preprocess(in_arr):
	k=0
	dim = in_arr.size
	for i in range(dim[0]):
		for j in range(dim[1]):
			if in_arr[i][j] >= 0:
				out_arr[0][k] = in_arr[i][j]
				k += 1
	if k%2 != 0:
		out_arr[0][k] = 0
	return out_arr
	 