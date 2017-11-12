#Splitting and Merging Image Channels


import numpy as np
import cv2
import matplotlib
img =  cv2.imread('/home/kartikay/Desktop/chotu.jpg')

#The B,G,R channels of an image can be split into their individual planes when needed. Then, the individual channels can be merged back together to form a BGR image again. This can be performed by:

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
#Suppose, you want to make all the red pixels to zero, you need not split like this and put it equal to zero. You can simply use Numpy indexing which is faster.

img[:,:,2] = 0
cv2.imshow("chotu",img)
cv2.waitKey(0)

