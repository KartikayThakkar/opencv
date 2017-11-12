import numpy as np
import cv2
import matplotlib as mp
from PIL import Image
import pylab

import cv2

#You can access a pixel value by its row and column coordinates. For BGR image, it returns an array of Blue, Green, Red values. For grayscale image, just corresponding intensity is returned.
px = img[100,100]
print px #[157 166 200]

# accessing only blue pixel
blue = img[100,100,0]
print blue #157

#You can modify the pixel values the same way.
img[100,100] = [255,255,255]
print img[100,100]   #[255 255 255]


#Better pixel accessing and editing method :

# accessing RED value
>>> img.item(10,10,2)
59

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)	#100


#Accessing Image Properties

#Image properties include number of rows, columns and channels, type of image data, number of pixels etc.
#Shape of image is accessed by img.shape. It returns a tuple of number of rows, columns and channels (if image is color):
print img.shape  #(342, 548, 3)

#Total number of pixels is accessed by img.size:
print img.size  #562248

#Image datatype is obtained by img.dtype:
print img.dtype  #uint8

