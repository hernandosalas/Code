# $ pip install opencv-python
# $ pin install numpy

# Download haar cascade
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

import cv2
import numpy as np
from skimage import io


def url_to_image(url):
    img = io.imread(url)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = url_to_image('https://static01.nyt.com/images/2020/01/28/multimedia/28xp-memekid3/28cp-memekid3-superJumbo.jpg') #reading the image
img = cv2.resize(img,(500,500)) #resize image to 500x500


copy = img.copy() #make copy of img
gray = cv2.cvtColor(copy,cv2.COLOR_BGR2GRAY) # converting the image to gray
eyes = cascade.detectMultiScale(gray,1.3,5) # for detecting the eyes in the image
for (ex,ey,ew,eh) in eyes: #dimensions for rectangle
    cv2.rectangle(copy,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # image,dim from, dim to, color of rect, width of rect

stack = np.hstack([img,copy])
cv2.imshow('Output',stack)
cv2.waitKey(0)

