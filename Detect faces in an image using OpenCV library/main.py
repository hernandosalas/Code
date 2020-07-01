'''
Title:
Detect faces in an image using OpenCV library

pip install opencv-python

Here is the link for face detection: https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
'''

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('test2.jpg')

# Detect faces
faces = face_cascade.detectMultiScale(img, 1.1, 4)

# Draw rectangle around the faces
# (255,0,0) is the color of the rectangle we want to draw. You play with it and change the color.
# (2) is the thickness of the line. You can change the value and see how it looks.
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Show the result
cv2.imshow("face_detected.png", img)
cv2.waitKey(0)

# Export the result
# cv2.imwrite("face_detected.png", img) 