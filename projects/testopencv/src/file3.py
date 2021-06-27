import cv2

import numpy as np
face_cascade=cv2.CascadeClassifier("C:\\Users\\hp\\projects\\testopencv\\frontalFace10\\haarcascade_frontalface_default.xml")

img1=cv2.imread("Capture.png")
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
	img=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
	img2=cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow('frame',img)
cv2.imshow('frame2',img2)
cv2.waitKey(0)

cv2.destroyAllWindows()
