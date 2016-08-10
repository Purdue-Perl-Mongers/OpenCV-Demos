import cv2

# pass either device id (0 usually for webcam) or path to a video file
cam = cv2.VideoCapture(0)

# face cascade bundled with OpenCV
classifier = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

while True:
	# read in frame
	retval, frame = cam.read()

	# convert to grayscale
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# run classifier
	results = classifier.detectMultiScale(
		frame_gray,
		# let's assume face will be close/big if in front of webcam
		minSize=(300,300)
	)

	# dray results
	for x, y, w, h in results:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255))

	# display
	cv2.imshow('webcam', frame)

	# wait 1 second for keypress before looping, quit if keypress is 'q'
	if cv2.waitKey(1) == ord('q'):
		break

# not really necessary to call explicitly if exiting program, but for completeness of example...
cam.release()
