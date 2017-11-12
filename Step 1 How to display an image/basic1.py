import numpy as np
import cv2
import matplotlib as mp
from PIL import Image
import pylab

# windows to display image
cv2.namedWindow("Image")

#To Read the image
img=cv2.imread('/home/kartikay/Desktop/chotu.jpg')

#To show the image
cv2.imshow("chotu",img)

#To see pixels
h,w = img.shape[:2]
print h,w

#save image
cv2.imwrite('result.png',img)

#exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()
