from PIL import Image
import os,sys
def preProcess(inpath):
	"Meant for preprocessing the image. Encyption step"
	im=Image.open(inpath).convert('L')
	pixels=list(im.getdata())
	dim = im.size
	numrows = dim[0]
	numcols = dim[1]
	for i in xrange(numrows): 
		for j in xrange(numcols):
			inp=y=r=(im.getpixel((i, j)))											#Get the pixel intensity
			x=r % (pow(2,3))														#Extract 3 LSBs
			r-=x 																	#Extract 5 MSBs
			r<<=3 																	#Move 4th and 5th bits to 7th and 8th postions
			r%=256 																	#Retain only 8 LSBs
			inp^=r 																	#Xor with original input
			r>>=6 																	#Move 7th and 8th bits to first two positions
			inp^=r 																	#Xor with original input
			inp%=256 																#Retain only the last 8 bits
			
			numbits = 4 															
			reversal = inp
			ls4 = (reversal%pow(2,4))                        
			reversal = reversal - ls4                                               #Extract 4 MSBs
			reversal >>= 4 															#Move them to 4 LSB positions
			rev = sum(1<<(numbits-1-i) for i in range(numbits) if reversal>>i&1)    #Reverse the 4 LSBs
			rev <<= 4 																#Move them to their original postions
			rev += ls4																#Obtain the processed input
			im.putpixel((i, j),rev)
	im.save("lena1.png")

inpath="lena.jpg"
preProcess(inpath)