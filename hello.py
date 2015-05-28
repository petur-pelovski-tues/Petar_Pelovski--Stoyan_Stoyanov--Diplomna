import cv2
import numpy as np
import time
import RPi.GPIO as GPIO
GPIO.setup(11, GPIO.out)
GPIO.setup(7, GPIO.out)

cap = cv2.VideoCapture(1)

white = 0
proba = 0
x = 0
i = 1
white = 0
left = 0
left-benchmark = 150


while(1):
	i = 1
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


	# define range of white color in HSV
	# change it according to your need !
	sensitivity = 40
	lower_white = np.array([0,0,255-sensitivity])
	upper_white = np.array([255,sensitivity,255])

	# Threshold the HSV image to get only white colors
	mask = cv2.inRange(hsv, lower_white, upper_white)

	cv2.imshow('frame',hsv)
	cv2.imshow('mask',mask)
	#print mask.size
	while i == 1:
		if(mask[200,x]==(255.0)):
			white = white + 1
		else:	

			if white > 3:
				left = x
				white = 0
			else:
				white = 0
			x = x + 1
		if x >= 640:
			i = 2
			x = 0
			k = 27
			time.sleep(0.3)
			time.sleep(0.3)
			if left < left-benchmark:
				GPIO.output(7, True)
				GPIO.output(11, True)
				GPIO.output(11, False)
				proba = 1		
			if left > left-benchmark:
				GPIO.output(7, False)
				GPIO.output(11, True)
				GPIO.output(11, False)
				proba = 1

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
