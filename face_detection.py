import sys
import cv2

if len(sys.argv) < 2:
	print 'Path to image is required'
	sys.exit()

# read in image
image = cv2.imread(sys.argv[1])

# face cascade bundled with OpenCV
classifier = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

# convert image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# run classifier
# try tweaking some parameters
params = {
	# proportion to scale in each resize step
	#'scaleFactor': 1.2,
	# nearby matches in sliding window
	#'minNeighbors': 4,
	# minimum match dimensions
	#'minSize': (50,50),
	# maximum match dimensions
	#'maxSize': (300,300),
}
results = classifier.detectMultiScale(image_gray, **params)

# draw results on original image
for x, y, w, h in results:
	cv2.rectangle(image, (x, y), (x+w, y+h), (0,0,255))

cv2.imshow('result', image)
cv2.waitKey(0)
