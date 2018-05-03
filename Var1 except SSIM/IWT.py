import numpy as np 
from PIL import Image
import math
def lwt2(inpath):
	fim1 = Image.open(inpath).convert("L")
	dim = fim1.size
	r = dim[0]
	c = dim[1]
	even = np.zeros((r,c/2), dtype=np.int)
	#First level decompostion
	#1 Even dimension
	for j in range(r):
		a = 1
		for k in range(int(c/2)):
			even[j][k] = fim1.getpixel((j,a))
			a += 2
	#1 Odd dimension
	odd = np.zeros((r,c/2), dtype = np.int)
	for j in range(r):
		a = 0
		for k in range(c/2):
			odd[j][k] = fim1.getpixel((j,a))
			a += 2
	dim2 = odd.shape
	lenr = dim2[0]
	lenc = dim2[1]
	
	fhigh = []
	flow = []
	#1 Dimensional Haar
	for j in range(lenr):
		fhigh.append([])
		flow.append([])
		for k in range(lenc):
			fhigh[j].append(odd[j][k] - even[j][k]) 
			flow[j].append(even[j][k] + math.floor(fhigh[j][k]/2))
	len2r = len(flow)
	len2c = len(flow[0])
	leven = []
	lodd = []
	heven = []
	hodd = []
	for j in range(len2c):
		a=1
		leven.append([])
		heven.append([])
		for k in range(len2r/2):
			#Even Separation of 1 Dimension
			leven[j].append(flow[a][j])
			heven[j].append(fhigh[a][j])
			a += 2
	leven = np.transpose(leven)
	heven = np.transpose(heven)
	#Odd separation of one dimension
	for j in range(len2c):
		a = 0
		lodd.append([])
		hodd.append([])
		for k in range(len2r/2):
			lodd[j].append(flow[a][j])
			hodd[j].append(fhigh[a][j])
			a +=2
	lodd = np.transpose(lodd)
	hodd = np.transpose(hodd)
	#2D Haar
	len12r = len(lodd)
	len12c = len(lodd[0])
	f2lhigh = []
	f2llow = []
	f2hhigh = []
	f2hlow = []
	for j in range(len12r):
		f2lhigh.append([])
		f2llow.append([])
		f2hhigh.append([])
		f2hlow.append([])
		for k in range(len12c):
			#Second level LH
			f2lhigh[j].append(lodd[j][k] - leven[j][k])
			#Second level LL
			f2llow[j].append(leven[j][k] + math.floor(f2lhigh[j][k]/2))
			#Second level HH
			f2hhigh[j].append(hodd[j][k] - heven[j][k])
			#Second level HL
			f2hlow[j].append(heven[j][k] + math.floor(f2hhigh[j][k]/2))
	return f2llow,f2lhigh,f2hlow,f2hhigh
	
def ilwt2(ll,lh,hl,hh):
	leven = []
	lodd = []
	heven = []
	hodd = []
	dim = [len(ll), len(ll[0])]
	for i in range(dim[0]):
		leven.append([])
		lodd.append([])
		heven.append([])
		hodd.append([])
		for j in range(dim[1]):
			leven[i].append( ll[i][j] - math.floor( lh[i][j] / 2) )
			lodd[i].append( lh[i][j] + leven[i][j] )
			heven[i].append( hl[i][j] - math.floor( hh[i][j] / 2 ) )
			hodd[i].append( hh[i][j] + heven[i][j] )
	fhigh = []
	flow = []
	numrows = len(hodd)
	numcols = len(hodd[0])
	l = 0
	k = 0
	for i in range(numrows*2):
		fhigh.append([])
		flow.append([])
		for j in range(numcols):
			if i%2 == 0:
				fhigh[i].append(hodd[k][j])
				flow[i].append(lodd[k][j])
			else:
				fhigh[i].append(heven[l][j])
				flow[i].append(leven[l][j])
		if i%2 == 0:
			k += 1
		else:
			l += 1

	even = []
	odd = []
	numrows = len(fhigh)
	numcols = len(fhigh[0])
	for i in range(numrows):
		even.append([])
		odd.append([])
		for j in range(numcols):
			even[i].append(flow[i][j] - np.floor(fhigh[i][j] / 2))
			odd[i].append(even[i][j] + fhigh[i][j])
	odd = np.transpose(odd)
	even = np.transpose(even)
	num = len(odd)
	j = 0
	k = 0
	final = []
	for i in range(num*2):
		if i%2 == 0:
			final.append(odd[j])
			j += 1
		else:
			final.append(even[k])
			k += 1
	final = np.array(final)
	dim = final.shape
	image = Image.new("L",(dim[0],dim[1]))
	final = np.reshape(final,(dim[0]*dim[1],1))
	image.putdata(final)
	image.save("C:\Miscellaneous\Project\Codes\Python Codes\OutputIWT.png")

ll,lh,hl,hh = lwt2("C:\Miscellaneous\Project\Codes\Python Codes\lena.jpg")	
#ilwt2("C:\Miscellaneous\Project\Codes\Python Codes")
ilwt2(ll,lh,hl,hh)
#C:\Users\PrasannaVenkatesan\Desktop\Op.tif