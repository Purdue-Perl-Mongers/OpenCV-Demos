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

# departing from filter_color example from here...

# last two parameters mean:
# - external borders (in case one contour contains another, take the outermoset)
# - compress number of points (slightly less precision, much less data)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) == 0:
	print 'No contours'
	sys.exit()

# find extremities
# contours is of the form:
# [ [ [[x, y]], ... ], ... ]
for i, c in enumerate(contours):
	point = c[0][0]

	# initialize with first point
	if i == 0:
		min_point = point.copy()
		max_point = point.copy()
		continue

	for j in range(2):
		if point[j] < min_point[j]:
			min_point[j] = point[j]
		elif point[j] > max_point[j]:
			max_point[j] = point[j]

# crop image
# y1:y2, x1:x2
result = image[min_point[1]:max_point[1], min_point[0]:max_point[0]]

# display result
cv2.imshow('result', result)
cv2.waitKey(0)
