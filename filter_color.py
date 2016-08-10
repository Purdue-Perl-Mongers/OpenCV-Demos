import sys
import cv2
import numpy as np

if len(sys.argv) < 2:
	print 'Path to image is required'
	sys.exit()

# read in image
image = cv2.imread(sys.argv[1])

# define acceptable color range
# NOTE this must be in same color space as the image
#      and just to be confusing, RGB colors are read in reverse order
lower_color_thresh = np.array([0,0,110])
upper_color_thresh = np.array([100,100,255])

# mask will be a black and white matrix (0 and 255) where the latter
# represents colors within our threshold
mask = cv2.inRange(image, lower_color_thresh, upper_color_thresh)

# get the parts of original image corresponding to white values in mask
result = cv2.bitwise_and(image, image, mask=mask)

# show result
cv2.imshow('original', image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)
