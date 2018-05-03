from PIL import Image
import numpy as np 
import math

def playfairdec(image,playkey):
	factor = 0.5
	dim = image.size
	in_image = []
	original = image.load()
	for j in range(dim[1]):
		for i in range(dim[0]):
			in_image.append(original[i,j])
	c = 0
	m = 0
	ix = 0
	iy = 0
	jx = 0
	jy = 0
	cipher_image = []
	while(m<len(in_image)):
		x = in_image[m]
		y =	in_image[m+1]
		for i in range(16):
			for j in range(16):
				if playkey[i][j] == x:
					ix = i
					jx = j
				if playkey[i][j] == y:
					iy = i
					jy = j
		if x == y:
			if ix == 0:
				ix = 16
			if jx == 0:
				jx = 16
			cipher_image.append(playkey[ix-1][jx-1])
			cipher_image.append(playkey[ix-1][jx-1])
		elif ix == iy and jx != jy:
			if jx == 0:
				jx = 16
			if jy == 0:
				jy = 16
			cipher_image.append(playkey[ix][jx-1])
			cipher_image.append(playkey[iy][jy-1])
		elif ix != iy and jx == jy:
			if ix == 0:
				ix = 16
			if iy == 0:
				iy =16
			cipher_image.append(playkey[ix-1][jx])
			cipher_image.append(playkey[iy-1][jy])
		elif ix != iy and jx != jy:
			cipher_image.append(playkey[ix][jy])
			cipher_image.append(playkey[iy][jx])
		m += 2
	final_image = []
	c = 0
	for j in range(dim[1]):
		final_image.append([])
		for i in range(dim[0]):
			final_image[j].append(cipher_image[c])
			c += 1

	im = Image.new("L",(dim[0],dim[1]))
	im_load  = im.load()
	for i in range(dim[0]):
		for j in range(dim[1]):
			im_load[i,j] = final_image[j][i]
	im.save("lenaFinal1.png")

key = 7
np.random.seed(key)
playkey = [i for i in range(256)]
playkey = np.random.permutation(playkey)
playkey = np.array(playkey).reshape(16,16)
image = Image.open("lenaOp1.png")
playfairdec(image,playkey)