'''
Getting Started with OpenCV
https://towardsdatascience.com/getting-started-with-opencv-249e86bd4293

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = cv2.imread('img.png')

# print(type(image))
# print(image.shape)

# Using cv2
def show_with_cv2(img_name):
    image = cv2.imread(img_name)
    cv2.imshow('show_with_cv2', image)
    # The methods .waitkey and .destroyAllWindows are essential to run our code without crashing. The first will tell Jupyter to keep running that block until some key is pressed, and the second will close the window at the end.
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Using plt
def show_with_plt(img_name):
    img = cv2.imread(img_name)
    fig, ax = plt.subplots(1, figsize=(12,8))
    ax.axis('off')   
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img, cmap='Greys')
    plt.waitforbuttonpress(0)

# Convert image to grayscale
def convert_to_grayscale(img_name):
    image = cv2.imread(img_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    cv2.imshow('convert_to_grayscale', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# show_with_cv2("img.png")

# show_with_plt("img.png")

convert_to_grayscale("img2.png")

def only_green():
    img = cv2.imread("img2.png")
    B, G, R = cv2.split(img) 
    img = cv2.merge([B*0, G, R*0])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('only_green', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

only_green()

# HSV: Hue, Saturation, and Value
def hsv():
    img = cv2.imread("img2.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(img)  
    img = cv2.merge([np.ones_like(H)*30, S+10, V-20])
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    cv2.imshow('HSV: Hue, Saturation, and Value', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

hsv()

# We can filter some colors and make all the rest in grayscale.
def filter_colors():
    # read img and convert to HSV
    img = cv2.imread("img2.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # split dimensions
    H, S, V = cv2.split(img)
    # upper and lower boundaries
    lower = np.array([80, 0, 0]) 
    upper = np.array([120, 255, 255])
    # build mask
    mask = cv2.inRange(img, lower, upper)
    # apply mask to saturation
    S = cv2.bitwise_and(S, S, mask=mask)
    # assemble image
    img = cv2.merge([H, S, V])
    # convert to RGB and display
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

    cv2.imshow('filter_colors', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
filter_colors()