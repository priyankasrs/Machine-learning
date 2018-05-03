from PIL import Image
import os,sys
def preProcess(inpath):
	"Decyption step for reverse processing"
	im=Image.open(inpath).convert('L')
	pixels=list(im.getdata())
	dim = im.size
	numrows = dim[0]
	numcols = dim[1]
	for i in xrange(numrows): 
		for j in xrange(numcols):
			inp=(im.getpixel((i, j)))

			numbits = 4 																
			reversal = inp
			ls4 = (reversal%pow(2,4))												#Extract 4 LSBs
			reversal = reversal - ls4												#Extract 4 MSBs
			reversal >>= 4 															#Bring 4 MSBs to 4 LSB postions
			rev = sum(1<<(numbits-1-i) for i in range(numbits) if reversal>>i&1)	#Reverse the 4 LBS
			rev <<= 4 																#Revert them to their original postions
			rev += ls4																#Add 4 LSBs to get Intended result 


			r=inp=y=rev 															
			x=r % (pow(2,3))														#Extract 3 LSBs
			r-=x 																	#Extract 5 MSBs
			r<<=3 																	#Bring 4th and 5th bits to 7th and 8th positions
			r%=256																	#Retain 7th and 8th bits and discard higher positions 
			inp^=r 																	#Xor this with the original input
			r>>=6	 																#Move 7th and 8th bits to 2 LSB positions 
			inp^=r 																	#Xor with original input
			inp%=256 																#Retain only 8 bits in the processed result
			im.putpixel((i, j),inp) 												#Modify the pixel value
	im.save("lenaFinal.png")

inpath="lenaFinal1.png"
preProcess(inpath)