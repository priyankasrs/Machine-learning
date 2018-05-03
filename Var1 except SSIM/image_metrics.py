import numpy as np 
import math
from PIL import Image
def psnr_mse(img1,img2):
	dim0 = img1.size
	dim1 = img2.size
	psnr = 0
	mse = 0
	for i in range(dim0[0]):
		for j in range(dim0[1]):
			mse += ((img1.getpixel((i,j)) - img2.getpixel((i,j)))**2)
	mse = mse/float(dim0[0]*dim0[1])
	print "MSE:",mse
	if mse != 0:
		psnr = 10 * math.log(((255**2)/mse),10)
	else:
		psnr = float("inf")
	print "PSNR:",psnr

def entropy(image):
	dim = image.size
	out_image = np.reshape(image,(1,dim[0]*dim[1]))
	dim2 = out_image.size
	out_image = out_image[0]
	symset = list(set(out_image))
	numsim = len(symset)
	probab = [np.size(out_image[out_image == i])/(1.0*dim2) for i in symset]
	ent = np.sum([p*np.log2(1.0/p) for p in probab])
	print "Entropy:",ent

def mae(image1,image2):
	print "MAE:",np.mean(abs(image1 - image2))

def corr2(image1,image2):
	mean1 = np.mean(image1)
	mean2 = np.mean(image2)
	dim = image1.shape
	corrnum = 0
	corrden1 = 0.0
	corrden2 = 0.0
	for i in range(dim[0]):
		for j in range(dim[1]):
			corrnum += (image1[i][j]-mean1)*(image2[i][j]-mean2)
			corrden1 += ((image1[i][j]-mean1)**2)
			corrden2 += ((image2[i][j]-mean2)**2)
	corrden = ((corrden1)*(corrden2))**0.5
	print "Correlation:",corrnum/corrden

def cov1(a, b):

    a_mean = np.mean(a)
    b_mean = np.mean(b)

    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))

    return sum/(len(a)-1)

def ssim(image1,image2):
	mean1 = np.mean(image1)
	mean2 = np.mean(image2)
	var1 = np.var(image1)
	var2 = np.var(image2)
	cov = np.cov(image1,image2)
	cov = cov[0][255]
	#cov = cov1(image1,image2)
	print cov
	c1 = (0.01*255)**2
	c2 = (0.03*255)**2
	ss = ((2 * mean1 * mean2 + c1) * (2 * cov + c2))/((mean1 ** 2 + mean2 ** 2 + c1) * (var1 ** 2 + var2 ** 2 + c2))
	print "SSIM:",ss

im1 = Image.open("lena.jpg").convert("L")
im2 = Image.open("lenaFinal.png").convert("L")
psnr_mse(im1,im2)
im = Image.open("C:\Miscellaneous\Project\Codes\Python Codes\Ver3 0412\lenaOp.png")
image1 = np.array(im1)
image2 = np.array(im2)
image3 = np.array(im)
print "For Original Image"
entropy(im1)
print "For Encrypted Image"
entropy(im)
mae(image1,image2)
corr2(image1,image3)
ssim(image1,image2)