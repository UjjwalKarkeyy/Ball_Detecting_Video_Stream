import cv2
import numpy as np

def get_limits(color):

    # Convert image to unsigned 8-bits integer
    img = np.uint8([[color]])

    # hsvFormat basically gives us the hue value of the color
    # Hue value is the degree of the color in the color wheel i.e., say we have 0 degree then it means red
    hsvFormat = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Here we subtract and add from the hue value as a single color say red isn't just red, there's a range of red
    # 100 in lowerLimit means the consideration of gray and dark
    # Whereas, 255 means consideration of pure color and brightness
    lowerLimit = hsvFormat[0][0][0] - 10, 100, 100 
    upperLimit = hsvFormat[0][0][0] - 10, 255, 255

    # Converting to np array as cv2 accepts only np arrays
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    # Returning the lower limit and upper limit back to main file
    return lowerLimit, upperLimit