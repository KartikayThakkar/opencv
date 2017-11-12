import numpy as np
import cv2
import matplotlib as mp
from PIL import Image
import pylab

import cv2

# windows to display image
cv2.namedWindow("Color Image/Or u can say original image")

# read the image
im = cv2.imread('chotu.jpg')

# create a grayscale version
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# save the image
cv2.imwrite('gray_foto.png', gray)

# show image
cv2.imshow("Color Image/Or u can say original image", im )

# exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()
