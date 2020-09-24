import cv2
import numpy as np
from skimage import io


def url_to_image(url):
    img = io.imread(url)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

num_down = 2 # number of downsamplin steps
num_bilateral = 7 # number of bilateral filtering steps

img_rgb = url_to_image('https://static01.nyt.com/images/2020/01/28/multimedia/28xp-memekid3/28cp-memekid3-superJumbo.jpg') #reading the image

print(img_rgb.shape) #prints the dimension of the picture

#resizing so as to get optimal results after un sampling is done
img_rgb = cv2.resize(img_rgb,(800,800))

# downsample image using Gaussian pyramid
img_color = img_rgb
for _ in range(num_down):
    img_color = cv2.pyrDown(img_color)

# repreatedly apply small bilateral filter instead of applying one large filter
for _ in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

# upsample image to original size
for _ in range(num_down):
    img_color = cv2.pyrUp(img_color)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray,7)

img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)

# convert back to color, bit-AND with color image
img_edge = cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color,img_edge)

# display
stack=np.hstack([img_rgb,img_cartoon])
cv2.imshow('Stacked Images',stack)
cv2.waitKey(0)


